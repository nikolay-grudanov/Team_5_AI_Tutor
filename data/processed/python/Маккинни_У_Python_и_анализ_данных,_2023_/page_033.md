---
source_image: page_033.png
page_number: 33
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.31
tokens: 7527
characters: 1988
timestamp: 2025-12-24T02:40:44.511222
finish_reason: stop
---

Установка необходимых пакетов

Теперь, когда менеджер Miniconda установлен, самое время установить основные пакеты, которые понадобятся нам в этой книге. Первый шаг — сделать conda-forge подразумеваемым по умолчанию каналом получения пакетов. Для этого выполните в оболочке следующие команды:

(base) $ conda config --add channels conda-forge
(base) $ conda config --set channel_priority strict

Далее создадим новую «среду» conda для Python 3.10 командой conda create:

(base) $ conda create -y -n pydata-book python=3.10

По завершении установки активируйте среду командой conda activate:

(base) $ conda activate pydata-book
(pydata-book) $

Команду conda activate нужно использовать при каждом открытии нового терминала. В любой момент можно получить информацию об активной среде conda, выполнив в терминале команду conda info.

Далее установим необходимые пакеты (вместе с их зависимостями) командой conda install:

(pydata-book) $ conda install -y pandas jupyter matplotlib

Мы будем использовать и некоторые другие пакеты, но установить их можно позже. Есть два способа установки пакетов: командами conda install и pip install. При работе с Miniconda предпочтительнее использовать conda install, но некоторые пакеты через conda недоступны, поэтому если conda install $package_name не работает, попробуйте $package_name.

Если вы хотите сразу установить все пакеты, которые нам понадобятся по ходу дела, то можете выполнить такую команду:

conda install lxml beautifulsoup4 html5lib openpyxl \
    requests sqlalchemy seaborn scipy statsmodels \
    patsy scikit-learn pyarrow pytables numba

В Windows в качестве символа продолжения строки используйте знак крышки ^ вместо знака \, применяемого в Linux и macOS.

Для обновления пакетов служит команда conda update:

conda update package_name

pip также поддерживает обновление, нужно только задать флаг --upgrade:

pip install --upgrade package_name

В этой книге вам не раз представится возможность попробовать эти команды в деле.