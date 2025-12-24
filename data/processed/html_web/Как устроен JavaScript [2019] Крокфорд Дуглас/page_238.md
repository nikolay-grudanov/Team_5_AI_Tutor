---
source_image: page_238.png
page_number: 238
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.65
tokens: 7423
characters: 1926
timestamp: 2025-12-24T09:59:55.078315
finish_reason: stop
---

25.7 Как работает транспиляция

• Инструкция call позволяет вызывать функцию и игнорировать ее возвращаемое значение:

    call my little impure side effect causer()

В Neo есть if и else. Есть также else if в качестве замены инструкции switch. Если условное выражение не выдает булево значение, происходит сбой. Лживые значения отсутствуют.

    if my hero = "monster"
        call blood curdling scream()
    else if my hero = "butterfly" \/ my hero = "unicorn"
        call do not make a sound()
    else
        call sing like a rainbow()

• Инструкция loop заменяет инструкции do, for и while. Я хочу, чтобы вы перестали применять циклы. Инструкция loop — это простой бесконечный цикл. Для выхода нужно использовать break или return. У циклов не бывает меток. Циклы могут быть вложенными. В них не могут создаваться новые функции.

• Исключения заменяются сбоями. У функции может быть обработчик сбоя. Инструкция try отсутствует.

    def my little function: f x the unknown {
        return risky operation(x the unknown)
    failure
        call launch all missiles()
        return null
    }

• Инструкция fail сообщает о сбое. Она не принимает объект исключения или какое-то другое сообщение. Если нужно сообщить причину сбоя, ее следует зарегистрировать до инструкции fail каким-либо иным способом.

• У модуля может быть несколько инструкций import:

    import имя: текстовый литерал

• У модуля может быть одна инструкция export:

    export выражение

Пример

В Neo используется реверсная функция свертки reduce reverse. Она допускает ранний выход и работает в обратном направлении. Принимает три аргумента: массив array, функцию обратного вызова callback function и исходное значение initial value. Функция обратного вызова получает четыре значения: текущее значение свертки, текущий элемент массива, число индекса текущего элемента и функцию выхода. Если функции обратного вызова callback function потребуется