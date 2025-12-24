"""
Скрипт для конвертации PDF документов в PNG изображения.
Обрабатывает все PDF файлы из директории pdf_source_files
и сохраняет изображения страниц в data/raw с сохранением структуры папок.

----

Системные требования:
- Linux: `sudo apt-get install poppler-utils`
- macOS: `brew install poppler`
- Windows: скачать poppler binary и добавить в PATH

"""

import logging
from pathlib import Path
import sys
from typing import List, Tuple

try:
    from pdf2image import convert_from_path
except ImportError:
    print("Ошибка: библиотека pdf2image не установлена.")
    print("Установите её командой: pip install pdf2image")
    print("Также требуется poppler-utils: apt-get install poppler-utils (Linux) или brew install poppler (macOS)")
    sys.exit(1)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/pdf_conversion.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PDFConverter:
    """Класс для конвертации PDF-документов в изображения.

    Класс обеспечивает рекурсивный поиск PDF-файлов в указанной директории,
    их постраничную конвертацию в изображения формата PNG с заданным разрешением
    и сохранение результатов в целевой директории с сохранением структуры подпапок.
    Также ведётся подробная статистика обработки.

    Attributes:
        source_dir (Path): Путь к директории с исходными PDF-файлами.
        target_dir (Path): Путь к директории для сохранения изображений.
        dpi (int): Разрешение изображений в точках на дюйм (DPI).
        stats (dict): Словарь со статистикой обработки файлов и страниц.
    """

    def __init__(self, source_dir: str = "pdf_source_files",
                 target_dir: str = "data/raw",
                 dpi: int = 100):
        """Инициализирует конвертер с указанными параметрами.

        Args:
            source_dir (str): Директория, в которой будут искаться исходные PDF-файлы.
                По умолчанию — 'pdf_source_files'.
            target_dir (str): Директория, в которую будут сохраняться изображения.
                По умолчанию — 'data/raw'.
            dpi (int): Разрешение для конвертации PDF в изображения. Чем выше значение,
                тем лучше качество, но больше размер файлов.

        Пример:
            >>> converter = PDFConverter(source_dir="docs", target_dir="output", dpi=200)
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.dpi = dpi

        # Статистика обработки
        self.stats = {
            'total_pdfs': 0,      # Всего найдено PDF-файлов
            'processed_pdfs': 0,  # Успешно обработанных PDF-файлов
            'failed_pdfs': 0,     # PDF-файлов, при обработке которых произошла ошибка
            'total_pages': 0,     # Общее количество обработанных страниц
            'failed_pages': 0     # Количество страниц, при сохранении которых произошла ошибка
        }

    def validate_directories(self) -> bool:
        """Проверяет существование и корректность исходной директории.

        Проверяет, существует ли директория с исходными PDF-файлами и является ли она директорией
        (а не файлом). Записывает ошибку в лог, если проверка не пройдена.

        Returns:
            bool: True, если директория существует и является каталогом, иначе — False.
        """
        if not self.source_dir.exists():
            logger.error(f"Исходная директория {self.source_dir} не существует")
            return False

        if not self.source_dir.is_dir():
            logger.error(f"{self.source_dir} не является директорией")
            return False

        return True

    def create_target_directory(self, relative_path: Path, pdf_name: str) -> Path:
        """Создаёт целевую директорию для сохранения изображений страниц PDF-файла.

        Создаёт директорию по пути: target_dir / relative_path / pdf_name.
        При необходимости создаются все промежуточные директории.

        Args:
            relative_path (Path): Относительный путь к поддиректории внутри source_dir,
                сохраняющий структуру исходных папок.
            pdf_name (str): Имя PDF-файла без расширения, используемое как имя папки
                для сохранения страниц.

        Returns:
            Path: Объект Path, указывающий на созданную директорию.

        Пример:
            Если relative_path = 'reports/2023', а pdf_name = 'annual', то будет создана
            директория: data/raw/reports/2023/annual
        """
        target_path = self.target_dir / relative_path / pdf_name
        target_path.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Создана директория: {target_path}")
        return target_path

    def find_all_pdfs(self) -> List[Tuple[Path, Path]]:
        """Рекурсивно находит все PDF-файлы в исходной директории.

        Обходит всю директорию source_dir и все её поддиректории, отбирая файлы с расширением .pdf.

        Returns:
            List[Tuple[Path, Path]]: Список кортежей, каждый из которых содержит:
                - полный путь к PDF-файлу (Path)
                - относительный путь к его директории от source_dir (Path)

        Пример:
            [
                (Path('pdf_source_files/report.pdf'), Path('')),
                (Path('pdf_source_files/eu/contract.pdf'), Path('eu'))
            ]
        """
        pdf_files = []

        for pdf_path in self.source_dir.rglob("*.pdf"):
            # Вычисляем относительный путь от source_dir
            relative_path = pdf_path.parent.relative_to(self.source_dir)
            pdf_files.append((pdf_path, relative_path))

        return pdf_files

    def convert_pdf_to_images(self, pdf_path: Path, output_dir: Path) -> bool:
        """Конвертирует один PDF-файл в последовательность изображений (по одной на страницу).

        Каждая страница сохраняется как отдельный PNG-файл с оптимизацией.
        Имена файлов формируются как 'page_001.png', 'page_002.png' и т.д.

        Args:
            pdf_path (Path): Полный путь к PDF-файлу, который нужно конвертировать.
            output_dir (Path): Директория, в которую будут сохранены изображения.

        Returns:
            bool: True, если конвертация прошла успешно (все страницы сохранены),
                False, если произошла ошибка при конвертации или сохранении.

        Примечания:
            - Используется модуль pdf2image для конвертации.
            - Конвертация выполняется в многопоточном режиме (4 потока).
            - Изображения сохраняются в формате PNG с включённой оптимизацией.
        """
        try:
            logger.info(f"Начало обработки: {pdf_path}")

            # Конвертация PDF в изображения
            images = convert_from_path(
                str(pdf_path),
                dpi=self.dpi,
                fmt='png',
                thread_count=4  # Использование многопоточности для ускорения
            )

            total_pages = len(images)
            logger.info(f"Получено {total_pages} страниц из {pdf_path.name}")

            # Сохранение изображений
            for i, image in enumerate(images, start=1):
                try:
                    # Формирование имени файла с ведущими нулями
                    page_number = str(i).zfill(3)
                    output_path = output_dir / f"page_{page_number}.png"

                    # Сохранение изображения
                    image.save(output_path, "PNG", optimize=True)
                    logger.debug(f"Сохранена страница: {output_path}")

                    self.stats['total_pages'] += 1

                except Exception as e:
                    logger.error(f"Ошибка при сохранении страницы {i} файла {pdf_path.name}: {e}")
                    self.stats['failed_pages'] += 1

            logger.info(f"✓ Успешно обработан: {pdf_path.name} ({total_pages} страниц)")
            return True

        except Exception as e:
            logger.error(f"✗ Ошибка при обработке файла {pdf_path}: {e}")
            return False

    def convert_all(self) -> None:
        """Конвертирует все найденные PDF-файлы в изображения.

        Основной метод класса. Выполняет следующие шаги:
        1. Проверяет существование исходной директории.
        2. Находит все PDF-файлы рекурсивно.
        3. Для каждого PDF-файла:
            - Создаёт целевую поддиректорию.
            - Конвертирует файл в изображения.
            - Обновляет статистику.
        4. Выводит итоговую статистику обработки.

        Если PDF-файлы не найдены, выводится предупреждение.
        """
        # Проверка директорий
        if not self.validate_directories():
            logger.error("Не удалось валидировать директории")
            return

        # Поиск всех PDF файлов
        logger.info("Поиск PDF файлов...")
        pdf_files = self.find_all_pdfs()

        if not pdf_files:
            logger.warning(f"В директории {self.source_dir} не найдено PDF файлов")
            return

        self.stats['total_pdfs'] = len(pdf_files)
        logger.info(f"Найдено {self.stats['total_pdfs']} PDF файлов для обработки")
        logger.info(f"DPI: {self.dpi}")
        logger.info("=" * 80)

        # Обработка каждого файла
        for pdf_path, relative_path in pdf_files:
            # Создание целевой директории
            pdf_name = pdf_path.stem  # Имя файла без расширения
            output_dir = self.create_target_directory(relative_path, pdf_name)

            # Конвертация PDF в изображения
            success = self.convert_pdf_to_images(pdf_path, output_dir)

            if success:
                self.stats['processed_pdfs'] += 1
            else:
                self.stats['failed_pdfs'] += 1

            logger.info("-" * 80)

        # Вывод итоговой статистики
        self.print_statistics()

    def print_statistics(self) -> None:
        """Выводит итоговую статистику обработки в лог.

        Отображает количество обработанных и неудачных файлов, общее количество
        созданных страниц и количество ошибок при сохранении страниц.
        Также выводится информационное сообщение об успешном завершении
        или предупреждение, если были ошибки.
        """
        logger.info("=" * 80)
        logger.info("СТАТИСТИКА ОБРАБОТКИ")
        logger.info("=" * 80)
        logger.info(f"Всего PDF файлов:        {self.stats['total_pdfs']}")
        logger.info(f"Успешно обработано:      {self.stats['processed_pdfs']}")
        logger.info(f"Ошибок при обработке:    {self.stats['failed_pdfs']}")
        logger.info(f"Всего страниц создано:   {self.stats['total_pages']}")
        logger.info(f"Ошибок при сохранении:   {self.stats['failed_pages']}")
        logger.info("=" * 80)

        if self.stats['processed_pdfs'] == self.stats['total_pdfs']:
            logger.info("✓ Все файлы успешно обработаны!")
        else:
            logger.warning(f"⚠ Не удалось обработать {self.stats['failed_pdfs']} файлов")



def main():
    """Основная функция для запуска конвертации."""
    # Создание директории для логов если её нет
    Path("logs").mkdir(exist_ok=True)
    
    logger.info("Запуск скрипта конвертации PDF в PNG")
    logger.info("=" * 80)
    
    # Создание экземпляра конвертера
    # Можно настроить параметры: source_dir, target_dir, dpi
    converter = PDFConverter(
        source_dir="pdf_source_files",
        target_dir="data/raw",
        dpi=300
    )
    
    # Запуск конвертации
    converter.convert_all()
    
    logger.info("Скрипт завершён")


if __name__ == "__main__":
    main()
