---
source_image: page_297.png
page_number: 297
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.49
tokens: 11663
characters: 1762
timestamp: 2025-12-24T01:48:07.068103
finish_reason: stop
---

Поговорим

Для доказательства этого положения я обычно приводу следующий класс Java.

Пример 9.15. Confidential.java: класс Java с закрытым полем secret

public class Confidential {

    private String secret = «»;

    public Confidential(String text) {
        secret = text.toUpperCase();
    }
}

Здесь я сохраняю текст в поле secret, предварительно преобразовав его в верхний регистр, чтобы значение этого поля гарантированно было записано заглавными буквами.

Собственно демонстрация заключается в выполнении скрипта expose.py интерпретатором Jython. Этот скрипт применяет интроспекцию (в терминологии Java — «отражение»), чтобы получить значение закрытого поля. Код показан в примере 9.16.

Пример 9.16. expose.py: Jython-код для чтения содержимого закрытого поля другого класса

import Confidential

message = Confidential('top secret text')
secret_field = Confidential.getDeclaredField('secret')
secret_field.setAccessible(True)   # замок взломан!
print 'message.secret =', secret_field.get(message)

Выполнив пример 9.16, получим:

$ jython expose.py
message.secret = TOP SECRET TEXT

Строка 'TOP SECRET TEXT' прочитана из закрытого поля secret класса Confidential.

Никакой черной магии тут нет: скрипт expose.py применяет API отражения Java, чтобы получить ссылку на закрытое поле с именем 'secret', а затем вызывает метод 'secret_field.setAccessible(True)', чтобы сделать его доступным для чтения. Разумеется, то же самое можно сделать и в коде на Java (только придется написать в три раза больше строк, см. файл Expose.java в репозитории кода к этой книге по адресу https://github.com/fluentpython/example-code).

Решающий вызов.setAccessible(True) завершится с ошибкой, только если скрипт Jython или главная программа Java (например, Expose.class)