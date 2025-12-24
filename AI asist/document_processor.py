"""
Модуль для работы с документами и их обработки.

Функции:
- Загрузка документов из файлов (TXT, MD, PDF)
- Разбиение документов на чанки
- Очистка и нормализация текста
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple
import logging

from config import (
    DOCUMENTS_DIR,
    MIN_DOCUMENT_LENGTH,
    MAX_CHUNK_LENGTH,
    CHUNK_OVERLAP,
    SAMPLE_MATERIALS
)

logger = logging.getLogger(__name__)

# Попытка импортировать pypdf для работы с PDF
try:
    from pypdf import PdfReader
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    logger.warning("pypdf не установлен. Поддержка PDF недоступна.")


class DocumentProcessor:
    """
    Класс для обработки учебных материалов.
    
    Методы:
    - load_documents: загрузить документы из директории
    - split_into_chunks: разбить текст на перекрывающиеся части
    - clean_text: очистить и нормализовать текст
    - save_documents: сохранить обработанные документы
    """
    
    def __init__(self):
        """Инициализация обработчика документов."""
        self.documents = []
        self.chunks = []
        logger.info("DocumentProcessor инициализирован")
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Очистить текст от лишних символов и пробелов.
        
        Args:
            text: исходный текст
            
        Returns:
            очищенный текст
        """
        # Удаление лишних пробелов
        text = re.sub(r'\s+', ' ', text)
        
        # Удаление специальных символов (кроме букв, цифр, пунктуации)
        text = re.sub(r'[^\w\s\.\,\!\?\-\(\)\:;/]', '', text, flags=re.UNICODE)
        
        # Удаление пробелов в начале и конце
        text = text.strip()
        
        return text
    
    @staticmethod
    def split_into_chunks(
        text: str,
        max_length: int = MAX_CHUNK_LENGTH,
        overlap: int = CHUNK_OVERLAP
    ) -> List[str]:
        """
        Разбить текст на перекрывающиеся чанки.
        
        Args:
            text: исходный текст для разбиения
            max_length: максимальная длина одного чанка
            overlap: размер перекрытия между чанками
            
        Returns:
            список чанков
        """
        if len(text) <= max_length:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            # Определение конца текущего чанка
            end = min(start + max_length, len(text))
            
            # Если это не последний чанк, попытаться разбить по предложению
            if end < len(text):
                # Поиск последней точки перед концом чанка
                last_period = text.rfind('.', start, end)
                if last_period > start:
                    end = last_period + 1
            
            chunks.append(text[start:end].strip())
            
            # Движение к следующему чанку с перекрытием
            start = end - overlap if end - overlap > start else end
        
        return chunks
    
    def load_documents(self, directory: Path = DOCUMENTS_DIR) -> List[Dict]:
        """
        Загрузить документы из директории.

        Args:
            directory: директория с документами

        Returns:
            список словарей с документами
        """
        self.documents = []
        
        # Поддерживаемые расширения файлов
        supported_formats = {'.txt', '.md', '.pdf'}
        
        if not directory.exists():
            logger.warning(f"Директория {directory} не существует")
            return self.documents
        
        for file_path in directory.glob('*'):
            if file_path.suffix.lower() in supported_formats:
                try:
                    # Обработка PDF
                    if file_path.suffix.lower() == '.pdf':
                        if not PDF_AVAILABLE:
                            logger.warning(f"Пропуск {file_path.name}: pypdf не установлен")
                            continue
                        
                        content = self._extract_pdf_text(file_path)
                    else:
                        # Обработка TXT и MD
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                    
                    # Очистка текста
                    cleaned_content = self.clean_text(content)
                    
                    # Проверка минимальной длины
                    if len(cleaned_content) < MIN_DOCUMENT_LENGTH:
                        logger.warning(
                            f"Документ {file_path.name} слишком короткий, пропущен"
                        )
                        continue
                    
                    doc = {
                        'source': file_path.name,
                        'content': cleaned_content,
                        'length': len(cleaned_content),
                        'format': file_path.suffix.lower()
                    }
                    
                    self.documents.append(doc)
                    logger.info(f"Загружен документ: {file_path.name} ({file_path.suffix})")
                    
                except Exception as e:
                    logger.error(f"Ошибка при загрузке {file_path.name}: {e}")
        
        logger.info(f"Всего загружено документов: {len(self.documents)}")
        return self.documents
    
    @staticmethod
    def _extract_pdf_text(file_path: Path) -> str:
        """
        Извлечь текст из PDF файла.
        
        Args:
            file_path: путь к PDF файлу
            
        Returns:
            текст из PDF
        """
        if not PDF_AVAILABLE:
            return ""
        
        try:
            reader = PdfReader(file_path)
            text = ""
            
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Страница {page_num + 1} ---\n{page_text}"
            
            return text
        except Exception as e:
            logger.error(f"Ошибка при чтении PDF {file_path.name}: {e}")
            return ""
        
        logger.info(f"Всего загружено документов: {len(self.documents)}")
        return self.documents
    
    def load_sample_materials(self) -> List[Dict]:
        """
        Загрузить примеры учебных материалов.
        
        Returns:
            список словарей с материалами
        """
        self.documents = []
        
        for subject, content in SAMPLE_MATERIALS.items():
            cleaned_content = self.clean_text(content)
            
            doc = {
                'source': f'{subject}.txt',
                'content': cleaned_content,
                'length': len(cleaned_content),
                'subject': subject
            }
            
            self.documents.append(doc)
            logger.info(f"Загружен пример материала: {subject}")
        
        return self.documents
    
    def create_chunks(self) -> List[Dict]:
        """
        Создать чанки из всех загруженных документов.
        
        Returns:
            список чанков с метаинформацией
        """
        self.chunks = []
        
        for doc_idx, doc in enumerate(self.documents):
            # Разбиение документа на чанки
            text_chunks = self.split_into_chunks(doc['content'])
            
            for chunk_idx, chunk in enumerate(text_chunks):
                chunk_obj = {
                    'id': f"doc_{doc_idx}_chunk_{chunk_idx}",
                    'content': chunk,
                    'source': doc['source'],
                    'chunk_index': chunk_idx,
                    'doc_index': doc_idx,
                    'length': len(chunk)
                }
                
                # Добавление дополнительной метаинформации если есть
                if 'subject' in doc:
                    chunk_obj['subject'] = doc['subject']
                
                self.chunks.append(chunk_obj)
        
        logger.info(f"Создано чанков: {len(self.chunks)}")
        return self.chunks
    
    def get_chunks(self) -> List[Dict]:
        """
        Получить текущие чанки.
        
        Returns:
            список чанков
        """
        return self.chunks
    
    def get_documents(self) -> List[Dict]:
        """
        Получить загруженные документы.
        
        Returns:
            список документов
        """
        return self.documents


def process_documents_pipeline():
    """
    Полный пайплайн обработки документов.
    
    Returns:
        список чанков готовых для индексирования
    """
    processor = DocumentProcessor()
    
    # Попытка загрузить документы из директории
    processor.load_documents()
    
    # Если документов нет, загрузить примеры
    if not processor.get_documents():
        logger.info("Загрузка примеров учебных материалов")
        processor.load_sample_materials()
    
    # Создание чанков
    chunks = processor.create_chunks()
    
    return processor, chunks
