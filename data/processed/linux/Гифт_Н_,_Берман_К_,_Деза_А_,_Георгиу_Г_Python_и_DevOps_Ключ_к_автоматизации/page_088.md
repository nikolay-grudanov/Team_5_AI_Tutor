---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.83
tokens: 7498
characters: 2114
timestamp: 2025-12-24T03:03:18.577256
finish_reason: stop
---

Файлы часто используют для настройки приложения во время выполнения, в Unix-системах файлы в соответствии с соглашением называются по расширению, заканчивающемуся на rc. Два распространенных примера: файл .vimrc текстового редактора Vim и файлы .bashrc командной оболочки Bash. Хранить эти файлы можно в различных местах. В программах часто описывается иерархия каталогов для их поиска. Например, утилита может сначала проверить переменную среды, в которой описано, какой файл rc использовать, а если таковой нет, проверить текущий каталог, затем домашний каталог активного пользователя. В примере 2.2 мы попробуем найти файл rc в этих местах. Для этого возьмем переменную file, значение которой Python автоматически задает при запуске кода Python из файла. В эту переменную заносится путь относительно действующего рабочего каталога, а не абсолютный/полный путь. Python не дополняет автоматически пути до абсолютного, как принято в Unix-системах, так что придется сделать это самим, прежде чем воспользоваться этим путем для формирования пути поиска файла rc. Аналогично Python не дополняет автоматически пути в переменных среды, так что и это нам придется сделать явно.

Пример 2.2. Метод find_rc

def find_rc(rc_name=".examplerc"):

    # Проверяем переменную среды
    var_name = "EXAMPLERC_DIR"
    if var_name in os.environ: ①
        var_path = os.path.join(f"${var_name}", rc_name) ②
        config_path = os.path.expandvars(var_path) ③
        print(f"Checking {config_path}")
        if os.path.exists(config_path): ④
            return config_path

    # Ищем в рабочем каталоге
    config_path = os.path.join(os.getcwd(), rc_name) ⑤
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Ищем в домашнем каталоге пользователя
    home_dir = os.path.expanduser("~/") ⑥
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Ищем в каталоге выполняемого файла
    file_path = os.path.abspath(__file__) ⑦
    parent_path = os.path.dirname(file_path) ⑧