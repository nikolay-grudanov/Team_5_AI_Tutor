---
source_image: page_754.png
page_number: 754
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.86
tokens: 7780
characters: 2437
timestamp: 2025-12-24T01:30:35.528372
finish_reason: stop
---

>>> import sub.lower.mod3    # Пакет пространства имен, вложенный
    #   в пакет пространства имен
dir2\sub\lower\mod3
c:\code> C:\Python37\python
>>> import sub                # Тот же самый эффект при постепенном доступе
>>> import sub.mod2
dir2\sub\mod2
>>> import sub.lower.mod3
dir2\sub\lower\mod3
>>> sub.lower                # Пакет пространства имен с единственным каталогом
<module 'sub.lower' (namespace)>
>>> sub.lower.__path__
_NamespacePath(['C:\\code\\ns\\dir2\\sub\\lower'])

В приведенном выше взаимодействии sub представляет собой пакет пространства имен, расщепленный на два каталога, а sub.lower — пакет пространства имен с единственным каталогом, который вложен в внутрь порции sub, физически размещенной в dir2. Вдобавок sub.lower — также пакет пространства имен, эквивалентный обычно-му пакету без файла __init__.py.

Такое поведение вложения сохраняется независимо от того, является компонент более низкого уровня модулем, обычным пакетом или еще одним пакетом пространства имен — выступая в качестве новых путей поиска для операций импортирования, пакеты пространств имен позволяют свободно вкладывать внутрь себя все перечисленные компоненты:

c:\code> mkdir ns\dir1\sub\pkg
c:\code> type ns\dir1\sub\pkg\__init__.py
print(r'dir1\sub\pkg\__init__.py')
c:\code> C:\Python37\python
>>> import sub.mod2           # Вложенный модуль
dir2\sub\mod2
>>> import sub.pkg             # Вложенный обычный пакет
dir1\sub\pkg\__init__.py
>>> import sub.lower.mod3      # Вложенный пакет пространства имен
dir2\sub\lower\mod3
>>> sub                        # Модули, пакеты и пространства имен
<module 'sub' (namespace)>
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>
>>> sub.pkg
<module 'sub.pkg' from 'C:\\code\\ns\\dir1\\sub\\pkg\\__init__.py'>
>>> sub.lower
<module 'sub.lower' (namespace)>
>>> sub.lower.mod3
<module 'sub.lower.mod3' from 'C:\\code\\ns\\dir2\\sub\\lower\\mod3.py'>

Чтобы лучше понять суть, исследуйте файлы и каталоги рассмотренного примера. Легко заметить, что пакеты пространств имен плавно интегрированы в предшествующие модели импортирования и расширяют их новой функциональностью.

Файлы по-прежнему имеют приоритет над каталогами

Как объяснялось ранее, одна из целей файлов __init__.py в обычных пакетах состоит в том, чтобы объявить каталог пакетом. Наличие файла __init__.py сообщает Python о том, что необходимо использовать каталог, а не переходить дальше в поисках