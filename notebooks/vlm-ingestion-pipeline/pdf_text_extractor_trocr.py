#!/usr/bin/env python3
"""
Скрипт для извлечения текста из PDF файлов с использованием модели TrOCR от Microsoft.
Альтернативный вариант, если HunyuanOCR не работает стабильно.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional
import logging

# Импорты
from PIL import Image
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from pdf2image import convert_from_path

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('pdf_extraction_trocr.log')
    ]
)
logger = logging.getLogger(__name__)

class TrOCRExtractor:
    """Класс для извлечения текста из PDF с использованием TrOCR."""
    
    def __init__(self, model_name: str = "microsoft/trocr-base-printed"):
        self.model_name = model_name
        self.model = None
        self.processor = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Используется устройство: {self.device}")
        
    def load_model(self):
        """Загрузка модели и процессора."""
        try:
            logger.info(f"Загрузка модели {self.model_name}...")
            
            self.processor = TrOCRProcessor.from_pretrained(self.model_name)
            self.model = VisionEncoderDecoderModel.from_pretrained(self.model_name)
            
            if self.device == "cuda":
                self.model = self.model.to(self.device)
                
            logger.info("Модель успешно загружена")
        except Exception as e:
            logger.error(f"Ошибка при загрузке модели: {e}")
            raise
    
    def pdf_to_images(self, pdf_path: str, dpi: int = 300) -> List[Image.Image]:
        try:
            logger.info(f"Конвертация PDF {pdf_path} в изображения...")
            images = convert_from_path(pdf_path, dpi=dpi)
            logger.info(f"Получено {len(images)} изображений из PDF")
            return images
        except Exception as e:
            logger.error(f"Ошибка при конвертации PDF в изображения: {e}")
            raise
    
    def extract_text_from_image(self, image: Image.Image) -> str:
        """
        Извлечение текста из одного изображения с помощью TrOCR.
        """
        try:
            # Преобразование изображения в RGB, если необходимо
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Обработка изображения
            pixel_values = self.processor(images=image, return_tensors="pt").pixel_values
            
            if self.device == "cuda":
                pixel_values = pixel_values.to(self.device)
            
            # Генерация текста
            with torch.no_grad():
                generated_ids = self.model.generate(pixel_values)
            
            # Декодирование
            extracted_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
            return extracted_text.strip()
            
        except Exception as e:
            logger.error(f"Ошибка при извлечении текста из изображения: {e}")
            # Вывод стека ошибки для отладки
            import traceback
            logger.error(traceback.format_exc())
            return ""
    
    def extract_text_from_pdf(self, pdf_path: str, output_dir: Optional[str] = None) -> str:
        if self.model is None or self.processor is None:
            self.load_model()
        
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
                logger.info(f"Страница {i}: извлечено {len(page_text)} символов")
            else:
                logger.warning(f"Не удалось извлечь текст со страницы {i} (пустой результат)")
        
        if output_dir is None:
            output_path = Path(pdf_path).parent
        else:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
        
        output_file = output_path / f"{pdf_name}.txt"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_text)
            logger.info(f"Текст сохранен в файл: {output_file}")
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла: {e}")
            raise
        
        return full_text
    
    def process_directory(self, input_dir: str, output_dir: Optional[str] = None) -> None:
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
        
        for pdf_file in pdf_files:
            try:
                logger.info(f"Обработка файла: {pdf_file}")
                self.extract_text_from_pdf(str(pdf_file), output_dir)
                logger.info(f"Успешно обработан файл: {pdf_file}")
            except Exception as e:
                logger.error(f"Ошибка при обработке файла {pdf_file}: {e}")
                continue

def main():
    parser = argparse.ArgumentParser(description="Извлечение текста из PDF файлов с использованием TrOCR")
    parser.add_argument("--input", type=str, default="pdf-for-test")
    parser.add_argument("--output", type=str)
    parser.add_argument("--model", type=str, default="microsoft/trocr-base-printed")
    
    args = parser.parse_args()
    input_path = Path(args.input)
    
    if not input_path.exists():
        logger.error(f"Входной путь не существует: {args.input}")
        sys.exit(1)
    
    extractor = TrOCRExtractor(args.model)
    
    try:
        if input_path.is_file():
            extractor.extract_text_from_pdf(str(input_path), args.output)
        elif input_path.is_dir():
            extractor.process_directory(str(input_path), args.output)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()