---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.75
tokens: 7556
characters: 1978
timestamp: 2025-12-24T08:53:26.001914
finish_reason: stop
---

Поиск символов с помощью регулярных выражений

Регулярные выражения — это строковые шаблоны, соответствующие определенным поисковым строкам. Например, шаблон '[^A-Z\s]' в строке 11 — это регулярное выражение, которое сообщает Python о том, что необходимо найти любой символ, не являющийся буквой от 'A' до 'Z' в верхнем регистре или пробельным символом (таким, как пробел, табуляция или символ новой строки).

11. nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

Функция re.compile() создает объект шаблона регулярного выражения (далее для краткости — объект шаблона), с которым могут работать другие функции модуля re. Мы будем использовать этот объект для удаления любых небуквенных символов из шифротекста в разделе "Функция hackSimpleSub()".

С помощью регулярных выражений можно выполнять самые разнообразные манипуляции со строками. Дополнительная информация о регулярных выражениях доступна по следующему адресу:
https://automatetheboringstuff.com/chapter7/

Функция main()

Как и в предыдущих программах взлома, рассмотренных в книге, шифротекст хранится в переменной message, которая передается функции hackSimpleSub() в строке 18.

13. def main():
14.     message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrp x ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrrramm'
15.
16.     # Определяем варианты дешифрования шифротекста
17.     print('Hacking...')
18.     letterMapping = hackSimpleSub(message)

Вместо того чтобы возвращать дешифрованное сообщение или значение None, если дешифрование невозможно, функция hackSimpleSub() возвращает пересечение словарей шифробукв, из которого удалены дешифрованные буквы. (О том, как создается такое пересечение, мы поговорим далее.)