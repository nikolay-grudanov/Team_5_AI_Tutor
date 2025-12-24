---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.36
tokens: 7528
characters: 2146
timestamp: 2025-12-24T09:58:34.772177
finish_reason: stop
---

Нынешние объекты JavaScript Date содержат множество методов. Большинство из них — это просто получатели и установщики (get- и set-методы):

getDate        setDate
getDay          setFullYear
getFullYear     setHours
getHours        setMilliseconds
getMilliseconds setMinutes
getMinutes      setMonth
getMonth        setSeconds
getSeconds      setTime
getTime         setUTCDate
getTimezoneOffset setUTCFullYear
getUTCDate      setUTCHours
getUTCDay       setUTCMilliseconds
getUTCFullYear  setUTCMinutes
getUTCHours     setUTCMonth
getUTCMilliseconds setUTCSeconds
getUTCMinutes   setYear
getUTCMonth
getUTCSeconds
getYear

Есть метод getDate, который возвращает день месяца из объекта Date. Сразу бросается в глаза то, что слово Date имеет в одном и том же методе два совершенно разных значения. Усугубляет путаницу метод getDay, который возвращает день недели.

Метод getMonth вносит правку в месяц, делая исходным нулевое значение, поскольку программистам нравится работать со всем, что начинается с нуля. Получается, что getMonth возвращает числа от 0 до 11. Метод getDate не вносит правку в день, поэтому он возвращает числа от 1 до 31. Это разночтение порождает массу ошибок.

Методы getYear и setYear после 1999 года работают неправильно и больше не должны использоваться. Язык Java был выпущен в 1995 году и содержал методы дат, которые должны были дать сбой в 2000 году. Неужели разработчики языка ничего не слышали о проблеме 2000 года? Или они сомневались, что Java переползет на рынке через этот рубеж? Возможно, это так и останется тайной. Но нам уже известно, что язык Java необъяснимым образом выжил и что в языке JavaScript была допущена точно такая же ошибка. Вместо этих методов всегда нужно использовать методы getFullYear и setFullYear.

Date демонстрирует весьма неудачные приемы классического программирования. В объекте что-то должно инкапсулироваться. Формами взаимодействия с объектами должны быть транзакции и другие высокоуровневые действия. Date дает весьма низкоуровневое представление с get- и set-методами для каждого отдельно взятого компонента времени. При таком подходе объекты используются крайне нерационально.