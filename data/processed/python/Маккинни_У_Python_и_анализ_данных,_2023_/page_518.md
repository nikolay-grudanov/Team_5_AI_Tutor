---
source_image: page_518.png
page_number: 518
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.45
tokens: 7669
characters: 2348
timestamp: 2025-12-24T02:54:43.014185
finish_reason: stop
---

profile_default. Следовательно, в моей Linux-системе полный путь к конфигурационному файлу IPython по умолчанию будет таким:

/home/wesm/.ipython/profile_default/ipython_config.py

Для инициализации этого файла в своей системе выполните в терминале команду

ipython profile create default

Не стану останавливаться на технических деталях содержимого этого файла. По счастью, все параметры в нем подробно прокомментированы, так что оставляю их изучение и изменение читателю. Еще одна полезная возможность — поддержка сразу нескольких профилей. Допустим, имеется альтернативная конфигурация IPython для конкретного приложения или проекта. Чтобы создать новый профиль, нужно всего лишь ввести такую строку:

ipython profile create secret_project

Затем отредактируйте конфигурационные файлы во вновь созданном каталоге profile_secret_project и запустите IPython следующим образом:

$ ipython --profile=secret_project
Python 3.8.0 | packaged by conda-forge | (default, Nov 22 2019, 19:11:19)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.

IPython profile: secret_project

Как всегда, дополнительные сведения о профилях и конфигурировании можно найти в документации по IPython в сети.
Конфигурирование Jupyter устроено несколько иначе, потому что его блокноты можно использовать не только с Python, но и с другими языками. Чтобы создать аналогичный конфигурационный файл Jupyter, выполните команду:

jupyter notebook --generate-config

Она создаст конфигурационный файл .jupyter/jupyter_notebook_config.py по умолчанию в подкаталоге вашего начального каталога. Вы можете отредактировать его и переименовать, например:

$ mv ~/.jupyter/jupyter_notebook_config.py ~/.jupyter/my_custom_config.py

Тогда при запуске Jupyter добавьте аргумент --config:

jupyter notebook --config=~/.jupyter/my_custom_config.py

В.8. Заключение

Когда будете прорабатывать примеры кода в этой книге и обогащать свои навыки программирования на Python, рекомендую постоянно интересоваться экосистемами IPython и Jupyter. Эти проекты создавались специально, чтобы повысить продуктивность пользователя, поэтому работать с ними проще, чем на самом языке Python с его вычислительными библиотеками.
А на сайте nbviewer (https://nbviewer.jupyter.org/) вы найдете много интересных Jupyter-блокнотов.