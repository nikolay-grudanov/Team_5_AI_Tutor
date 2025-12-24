#!/usr/bin/env python3
"""
Скрипт для извлечения текста из PDF файлов с использованием модели HunyuanOCR (1B) от Tencent.

Исправления:
- Используется правильный класс AutoModelForVision2Seq.
- Исправлен баг с двойной токенизацией (добавлен tokenize=False).
- Добавлена поддержка FP16 для GPU.

Требования:
pip install git+https://github.com/huggingface/transformers@82a06db03535c49aa987719ed0746a76093b1ec4
pip install torch pillow pdf2image accelerate

Системные требования:
sudo apt-get install poppler-utils  # Ubuntu
brew install poppler                # MacOS
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional
import logging
import traceback

# Импорты
from PIL import Image
import torch
from transformers import AutoModelForVision2Seq, AutoProcessor
from pdf2image import convert_from_path

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler("pdf_extraction.log")],
)
logger = logging.getLogger(__name__)


class HunyuanOCRExtractor:
    """Класс для извлечения текста из PDF с использованием HunyuanOCR."""

    def __init__(self, model_name: str = "Tencent/HunyuanOCR"):
        self.model_name = model_name
        self.model = None
        self.processor = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Используется устройство: {self.device}")

    def load_model(self):
        """Загрузка модели и процессора."""
        try:
            logger.info(f"Загрузка модели {self.model_name}...")
            
            # Определяем тип данных в зависимости от устройства и поддержки bfloat16
            if self.device == "cuda":
                # Проверяем поддержку bfloat16 на GPU
                if torch.cuda.is_bf16_supported():
                    dtype = torch.bfloat16
                    logger.info("GPU поддерживает bfloat16, используется torch.bfloat16")
                else:
                    dtype = torch.float16
                    logger.warning("GPU не поддерживает bfloat16, используется fallback на torch.float16")
            else:
                dtype = torch.float32
                logger.info("Для CPU используется torch.float32")
            
            # Сбрасываем предыдущие значения
            self.model = None
            self.processor = None
            
            self.model = AutoModelForVision2Seq.from_pretrained(
                self.model_name,
                torch_dtype=dtype,
                device_map="auto" if self.device == "cuda" else None,
                trust_remote_code=True
            )
            
            # --- ИСПРАВЛЕНИЕ ДЛЯ CPU ---
            # Если мы на CPU, принудительно конвертируем ВСЕ параметры в float32.
            # Это гарантирует согласованность типов и предотвращает ошибки BFloat16 vs Float.
            if self.device == "cpu":
                logger.info("Конвертация всех параметров модели в float32 для CPU...")
                for param in self.model.parameters():
                    param.data = param.data.to(dtype=torch.float32)
                
                # КРИТИЧЕСКИЙ ПАТЧ: предотвращаем hardcoded cast к bfloat16 в модели
                self._patch_vit_forward()
                
                self.model.eval() # Переводим в режим инференса
            
            self.processor = AutoProcessor.from_pretrained(
                self.model_name,
                trust_remote_code=True
            )
            
            # Проверяем, что модель и процессор успешно загружены
            if self.model is None:
                raise RuntimeError("Модель не была загружена (self.model is None)")
            if self.processor is None:
                raise RuntimeError("Процессор не был загружен (self.processor is None)")
            
            # Debug-логирование типов данных после загрузки
            logger.info(f"Модель успешно загружена (устройство: {self.device})")
            logger.info(f"Тип данных модели: {self.model.dtype}")
            
            # Логируем информацию о типах параметров для отладки
            param_dtypes = set()
            for param in self.model.parameters():
                param_dtypes.add(param.dtype)
            logger.info(f"Типы параметров модели: {param_dtypes}")
                
        except Exception as e:
            logger.error(f"Ошибка при загрузке модели: {e}")
            # Сбрасываем значения в случае ошибки
            self.model = None
            self.processor = None
            raise



    def pdf_to_images(self, pdf_path: str, dpi: int = 300) -> List[Image.Image]:
        """Конвертация PDF в изображения."""
        try:
            # Проверяем существование файла
            if not Path(pdf_path).exists():
                raise FileNotFoundError(f"PDF файл не найден: {pdf_path}")
            
            logger.info(f"Конвертация PDF {pdf_path} в изображения...")
            images = convert_from_path(pdf_path, dpi=dpi)
            
            if not images:
                raise ValueError("Не удалось извлечь изображения из PDF")
                
            logger.info(f"Получено {len(images)} изображений из PDF")
            return images
        except Exception as e:
            logger.error(f"Ошибка при конвертации PDF в изображения: {e}")
            logger.error(traceback.format_exc())
            raise

    def extract_text_from_image(self, image: Image.Image) -> str:
        """
        Извлечение текста из одного изображения.
        """
        try:
            # Проверка, что модель и процессор загружены
            if self.model is None or self.processor is None:
                logger.info("Модель или процессор не загружены, выполняем загрузку...")
                self.load_model()
                # Повторная проверка после попытки загрузки
                if self.model is None or self.processor is None:
                    logger.error("Не удалось загрузить модель или процессор")
                    return ""
            
            # 1. Подготовка промпта (Chat Template)
            messages = [
                {
                    "role": "user",
                    "content": [{"type": "image"}, {"type": "text", "text": "OCR this text."}],
                }
            ]

            # 2. Применение шаблона
            # ВАЖНО: tokenize=False, чтобы получить строку, которую поймет processor
            text_input = self.processor.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )

            # 3. Препроцессинг (Текст -> Токены, Картинка -> Пиксели)
            inputs = self.processor(images=[image], text=[text_input], return_tensors="pt")

            # 4. Перенос данных на устройство и конвертация типов
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Принудительно конвертируем pixel_values к float32 для CPU
            # Это предотвращает ошибку из-за hardcoded cast к bfloat16 внутри модели
            if self.device == "cpu":
                inputs["pixel_values"] = inputs["pixel_values"].to(torch.float32)
            else:
                # Для CUDA используем dtype модели
                inputs["pixel_values"] = inputs["pixel_values"].to(self.model.dtype)

            # 5. Генерация
            with torch.no_grad():
                output_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=2048,  # Максимальная длина текста на выходе
                    do_sample=False,  # Greedy decoding (детерминировано)
                    temperature=0.0,
                    use_cache=True,
                )

            # 6. Декодирование ответа
            # Нам нужно убрать из ответа сам вопрос (промпт)
            input_len = inputs["input_ids"].shape[1]
            generated_ids = output_ids[0][input_len:]

            # Проверяем, что есть что декодировать
            if len(generated_ids) == 0:
                logger.warning("Модель не сгенерировала текста")
                return ""

            extracted_text = self.processor.decode(generated_ids, skip_special_tokens=True)
            return extracted_text.strip()

        except Exception as e:
            logger.error(f"Ошибка при извлечении текста из изображения: {e}")
            logger.error(traceback.format_exc())
            return ""

    def extract_text_from_pdf(self, pdf_path: str, output_dir: Optional[str] = None) -> str:
        """Обработка одного PDF файла."""
        try:
            if self.model is None or self.processor is None:
                logger.info("Модель или процессор не загружены, выполняем загрузку...")
                self.load_model()
                # Повторная проверка после попытки загрузки
                if self.model is None or self.processor is None:
                    logger.error("Не удалось загрузить модель или процессор")
                    return ""

            images = self.pdf_to_images(pdf_path)
            full_text = ""
            pdf_name = Path(pdf_path).stem

            logger.info(f"Начало извлечения текста из {len(images)} страниц...")

            for i, image in enumerate(images, 1):
                logger.info(f"Обработка страницы {i}/{len(images)}")
                page_text = self.extract_text_from_image(image)

                if page_text:
                    full_text += f"\n--- СТРАНИЦА {i} ---\n"
                    full_text += page_text + "\n"
                    logger.info(f"Страница {i}: успешно извлечено {len(page_text)} символов")
                else:
                    logger.warning(f"Страница {i}: текст не найден или произошла ошибка")

            # Сохранение результата
            if output_dir is None:
                output_path = Path(pdf_path).parent
            else:
                output_path = Path(output_dir)
                output_path.mkdir(parents=True, exist_ok=True)

            output_file = output_path / f"{pdf_name}.txt"

            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(full_text)
                logger.info(f"Текст сохранен в файл: {output_file}")
            except Exception as e:
                logger.error(f"Ошибка при сохранении файла: {e}")
                raise

            return full_text
        except Exception as e:
            logger.error(f"Ошибка при обработке PDF файла {pdf_path}: {e}")
            logger.error(traceback.format_exc())
            return ""

    def process_directory(self, input_dir: str, output_dir: Optional[str] = None) -> None:
        """Пакетная обработка директории."""
        try:
            input_path = Path(input_dir)

            if not input_path.exists():
                logger.error(f"Директория не существует: {input_dir}")
                return

            if output_dir is None:
                output_dir = str(input_path)

            pdf_files = list(input_path.glob("*.pdf"))

            if not pdf_files:
                logger.warning(f"В директории {input_dir} не найдено PDF файлов")
                return

            logger.info(f"Найдено {len(pdf_files)} PDF файлов для обработки")

            successful_count = 0
            failed_count = 0

            for pdf_file in pdf_files:
                try:
                    logger.info(f"--- Запуск обработки файла: {pdf_file.name} ---")
                    result = self.extract_text_from_pdf(str(pdf_file), output_dir)
                    if result:  # Если результат не пустой, считаем обработку успешной
                        successful_count += 1
                        logger.info(f"Файл {pdf_file.name} успешно обработан")
                    else:
                        failed_count += 1
                        logger.warning(f"Файл {pdf_file.name} обработан с ошибками или пустой результат")
                except Exception as e:
                    failed_count += 1
                    logger.error(f"Сбой обработки файла {pdf_file}: {e}")
                    logger.error(traceback.format_exc())
                    continue
            
            logger.info(f"Обработка директории завершена. Успешно: {successful_count}, с ошибками: {failed_count}")
        except Exception as e:
            logger.error(f"Критическая ошибка при обработке директории {input_dir}: {e}")
            logger.error(traceback.format_exc())


def main():
    parser = argparse.ArgumentParser(
        description="Извлечение текста из PDF файлов с использованием HunyuanOCR"
    )
    parser.add_argument("--input", type=str, default="pdf-for-test", help="Путь к PDF или папке")
    parser.add_argument("--output", type=str, help="Папка для сохранения (опционально)")
    parser.add_argument("--model", type=str, default="Tencent/HunyuanOCR", help="ID модели на HF")

    args = parser.parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        logger.error(f"Входной путь не существует: {args.input}")
        sys.exit(1)

    extractor = HunyuanOCRExtractor(args.model)

    try:
        if input_path.is_file():
            if input_path.suffix.lower() != ".pdf":
                logger.error("Указанный файл не является PDF")
                sys.exit(1)
            extractor.extract_text_from_pdf(str(input_path), args.output)
        elif input_path.is_dir():
            extractor.process_directory(str(input_path), args.output)
        else:
            logger.error("Некорректный путь")
            sys.exit(1)

        logger.info("=== Вся обработка завершена успешно ===")

    except KeyboardInterrupt:
        logger.info("Операция прервана пользователем")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
