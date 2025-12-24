---
source_image: page_477.png
page_number: 477
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.73
tokens: 7566
characters: 1707
timestamp: 2025-12-24T01:22:09.069127
finish_reason: stop
---

манде задействован новый запускающий модуль Windows, появившийся в Python 3.3; в третьей команде указан полный путь к каталогу с Python, если другие две схемы не работают. В приложении А второго тома приведены добавочные сведения об аргументе -m, а в приложении Б второго тома — о запускающем модуле Windows.

c:\code> python -m pydoc -b
Server ready at http://localhost:62135/
Server commands: [b]rowser, [q]uit
server> q
Server stopped

c:\code> py -3 -m pydoc -b
Server ready at http://localhost:62144/
Server commands: [b]rowser, [q]uit
server> q
Server stopped

c:\code> C:\python33\python -m pydoc -b
Server ready at http://localhost:62153/
Server commands: [b]rowser, [q]uit
server> q
Server stopped

Результатом ввода одной из таких команд будет запуск PyDoc как локально выполняющегося веб-сервера на выделенном (но по умолчанию произвольно выбираемом из числа неиспользуемых) порте и открытию веб-браузера, который действует в качестве клиента и отображает страницу со ссылками на документацию для всех модулей, импортируемых в пути поиска модулей (включая каталог, где запущен PyDoc). Интерфейс веб-страницы верхнего уровня PyDoc представлен на рис. 15.1.

![Стартовая индексная страница верхнего уровня HTML-интерфейса PyDoc с единым браузером в Python 3.2 и последующих версиях, который стал заменой клиента с графическим пользовательским интерфейсом из более ранних версий Python, начиная с Python 3.3](https://i.imgur.com/3Q5z5QG.png)

Рис. 15.1. Стартовая индексная страница верхнего уровня HTML-интерфейса PyDoc с единым браузером в Python 3.2 и последующих версиях, который стал заменой клиента с графическим пользовательским интерфейсом из более ранних версий Python, начиная с Python 3.3