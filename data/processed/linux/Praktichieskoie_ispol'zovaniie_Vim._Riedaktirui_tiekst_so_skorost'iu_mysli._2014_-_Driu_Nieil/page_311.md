---
source_image: page_311.png
page_number: 311
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.82
tokens: 5694
characters: 1908
timestamp: 2025-12-24T04:16:12.002332
finish_reason: stop
---

⇒ $ cd code/ctags
⇒ $ ls
    anglophone.rb francophone.rb speaker.rb
⇒ $ ctags *.rb
⇒ $ ls
    anglophone.rb francophone.rb speaker.rb tags

Обратите внимание, что программа ctags создала простой текстовый файл с именем tags. Он содержит алфавитный указатель ключевых слов из трех исходных файлов, проанализированных с помощью ctags.

Анатомия индексного файла

Давайте заглянем внутрь только что созданного файла tags. Отметьте, что некоторые строки были усечены, чтобы уместить их по ширине страницы:

ctags/tags-abridged
http://media.pragprog.com/titles/dnvim/code/ctags/tags-abridged

!_TAG_FILE_FORMAT      2   /extended format/
!_TAG_FILE_SORTED      1   /0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR   Darren Hiebert //
!_TAG_PROGRAM_NAME     Exuberant Ctags //
!_TAG_PROGRAM_URL      http://ctags.sourceforge.net /official site/
!_TAG_PROGRAM_VERSION  5.8 //
Anglophone  anglophone.rb /^class Anglophone < Speaker$;/;"   c
Francophone francophone.rb /^class Francophone < Speaker$;/;"   c
Speaker speaker.rb     /^class Speaker$;/;"   c
initialize speaker.rb   /^ def initialize(name)$;/;"   f
speak   anglophone.rb   /^ def speak$;/;"   f   class:Anglophone
speak   francophone.rb  /^ def speak$;/;"   f   class:Francophone
speak   speaker.rb      /^ def speak$;/;"   f   class:Speaker

Индексный файл начинается несколькими строками с метаданными. Вслед за ними следует список ключевых слов, по одному в каждой строке. Каждый элемент списка содержит ключевое слово, а также имя файла и адрес в файле, где это ключевое слово встречается. Ключевые слова отсортированы в алфавитном порядке, поэтому Vim (или любой другой текстовый редактор) может быстро отыскивать их в файле, используя поиск методом дихотомии.

Ключевые слова адресуются шаблонами, а не номерами строк

Спецификация формата индексного файла определяет, что роль адреса может играть любая команда Ex¹. В этом качестве вполне