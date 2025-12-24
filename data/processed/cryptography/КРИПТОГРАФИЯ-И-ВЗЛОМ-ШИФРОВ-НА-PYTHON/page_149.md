---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.17
tokens: 7288
characters: 1414
timestamp: 2025-12-24T08:49:32.514424
finish_reason: stop
---

```python
print(plaintext + '|')
pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # Функция расшифровки перестановочного шифра будет имитировать
    # столбцы и строки таблицы, в которые вписан простой текст,
    # используя список строк. Сначала вычислим несколько значений.
    # Количество столбцов в перестановочной таблице
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # Количество строк в таблице
    numOfRows = key
    # Количество "заштрихованных" ячеек в последнем столбце
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # Каждая строка в списке plaintext представляет столбец
    plaintext = [''] * numOfColumns
    # Переменные column и row указывают, в какую ячейку должен
    # быть помещен символ зашифрованного сообщения
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1  # указывает на следующий столбец
        # Если больше нет столбцов ИЛИ мы оказались в "заштрихованной"
        # ячейке, перейти к первому столбцу следующей строки
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)

# Если файл transpositionDecrypt.py выполняется как программа
# (а не импортируется как модуль), вызвать функцию main()
if __name__ == '__main__':
    main()
```