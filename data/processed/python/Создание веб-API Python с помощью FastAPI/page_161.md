---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.59
tokens: 8294
characters: 1036
timestamp: 2025-12-24T02:20:08.029507
finish_reason: stop
---

Сначала определим функцию, которая выполняет арифметические операции. В модуле тестов добавьте следующее:

```python
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return b - a

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> int:
    return b // a
```

Теперь, когда мы определили операции для тестирования, мы создадим функции, которые будут обрабатывать эти тесты. В тестовых функциях определяется операция, которая должна быть выполнена. Ключевое слово assert используется для проверки того, что вывод в левой части соответствует результат операции в правой части. В нашем случае мы будем проверять, равны ли арифметические операции их соответствующим результатам.

Добавьте следующее в модуль tests:

```python
def test_add() -> None:
    assert add(1, 1) == 2

def test_subtract() -> None:
    assert subtract(2, 5) == 3

def test_multiply() -> None:
    assert multiply(10, 10) == 100

def test_divide() -> None:
    assert divide(25, 100) == 4
```