---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.09
tokens: 7599
characters: 2034
timestamp: 2025-12-24T03:02:58.311269
finish_reason: stop
---

Можно также сохранять данные из Python в формате YAML:

In [22]: with open('verify-apache.yml', 'w') as opened_file:
    ...:     yaml.dump(verify_apache, opened_file)
    ...:
    ...:
    ...:
    ...:

Еще один язык, широко применяемый для представления структурированных данных, — XML (Extensible Markup Language, расширяемый язык разметки). В нем используются иерархические документы, состоящие из маркированных элементов. Исторически так сложилось, что многие веб-системы задействовали XML для передачи данных, в частности, для RSS-каналов. С помощью RSS-каналов отслеживают обновления веб-сайтов и оповещают о них пользователей, а также отслеживают публикации статей в различных источниках. RSS-каналы применяют страницы в формате XML. Python включает библиотеку xml, предназначенную для работы с XML-документами и умеющую отображать иерархические структуры XML-документов как древовидные структуры данных. Узлы дерева играют роль элементов XML, а иерархия моделируется с помощью взаимосвязи «родительский элемент — дочерний элемент». Самый верхний родительский узел называется корневым элементом. Произвести синтаксический разбор XML-документа RSS и получить его корневой элемент можно следующим образом:

In [1]: import xml.etree.ElementTree as ET
In [2]: tree = ET.parse('http_feeds.feedburner.com_oreilly_radar_atom.xml')

In [3]: root = tree.getroot()

In [4]: root
Out[4]: <Element '{http://www.w3.org/2005/Atom}feed' at 0x11292c958>

Обход дерева можно выполнить посредством прохода в цикле дочерних узлов:

In [5]: for child in root:
    ...:     print(child.tag, child.attrib)
    ...:
{http://www.w3.org/2005/Atom}title {}
{http://www.w3.org/2005/Atom}id {}
{http://www.w3.org/2005/Atom}updated {}
{http://www.w3.org/2005/Atom}subtitle {}
{http://www.w3.org/2005/Atom}link {'href': 'https://www.oreilly.com'}
{http://www.w3.org/2005/Atom}link {'rel': 'hub',
    'href': 'http://pubsubhubbub.appspot.com/'}
{http://www.w3.org/2003/01/geo/wgs84_pos#}long {}
{http://rssnamespace.org/feedburner/ext/1.0}emailServiceId {}