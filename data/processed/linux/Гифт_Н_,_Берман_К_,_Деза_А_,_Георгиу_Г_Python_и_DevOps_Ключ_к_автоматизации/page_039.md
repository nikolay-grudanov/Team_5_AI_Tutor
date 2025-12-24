---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.45
tokens: 7302
characters: 1359
timestamp: 2025-12-24T03:01:53.389692
finish_reason: stop
---

...
The count is 0
The count is 1
The count is 2
>>>

Главное — задать условие выхода из такого цикла, в противном случае он будет выполняться до тех пор, пока программа не завершится аварийно. Для этого можно, например, задать такое условное выражение, которое в конце концов окажется равным False. Либо воспользоваться оператором break для выхода из цикла с помощью вложенного условного оператора:

>>> count = 0
>>> while True:
...     print(f"The count is {count}")
...     if count > 5:
...         break
...     count += 1
...
...
The count is 0
The count is 1
The count is 2
The count is 3
The count is 4
The count is 5
The count is 6
>>>

Обработка исключений

Исключения — ошибки, которые могут привести к фатальному сбою программы, если их не обработать должным образом (перехватить). Благодаря их перехвату с помощью блока try-except программа может продолжить работу. Для создания такого блока необходимо добавить отступы к блоку, в котором может возникнуть исключение, поместить перед ним оператор try, а после него — оператор except. За ним будет следовать блок кода, который должен выполняться при возникновении ошибки:

>>> thinkers = ['Plato', 'PlayDo', 'Gumby']
>>> while True:
...     try:
...         thinker = thinkers.pop()
...         print(thinker)
...     except IndexError as e:
...         print("We tried to pop too many thinkers")