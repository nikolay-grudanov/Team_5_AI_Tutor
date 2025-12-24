---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.04
tokens: 7385
characters: 1700
timestamp: 2025-12-24T03:03:18.201282
finish_reason: stop
---

Пути как объекты: библиотека pathlib

Библиотека pathlib позволяет представлять пути в виде объектов, а не строк. В примере 2.5 мы перепишем пример 2.2, используя pathlib вместо os.path.

Пример 2.5. Переписываем функцию find_rc
def find_rc(rc_name=".examplerc"):

    # Проверяем переменную среды
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name) ①
    if example_dir:
        dir_path = pathlib.Path(example_dir) ②
        config_path = dir_path / rc_name ③
        print(f"Checking {config_path}")
        if config_path.exists(): ④
            return config_path.as_postix() ⑤

    # Ищем в текущем рабочем каталоге
    config_path = pathlib.Path.cwd() / rc_name ⑥
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postix()

    # Ищем в домашнем каталоге пользователя
    config_path = pathlib.Path.home() / rc_name ⑦
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postix()

    # Ищем в каталоге выполняемого файла
    file_path = pathlib.Path(__file__).resolve() ⑧
    parent_path = file_path.parent ⑨
    config_path = parent_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postix()

    print(f"File {rc_name} has not been found")

① На момент написания данной книги библиотека pathlib не дополняет переменные среды до абсолютного пути. Поэтому мы берем значение переменной из os.environ.

② Создаем объект pathlib.Path, соответствующий используемой операционной системе.

③ Новые объекты pathlib.Path можно создавать, указывая после родительского пути прямые косые черты и соответствующие строковые значения.