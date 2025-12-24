---
source_image: page_252.png
page_number: 252
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.13
tokens: 7512
characters: 1977
timestamp: 2025-12-24T03:07:34.266985
finish_reason: stop
---

к другим фикстурам! Необходимо описать требуемую фикстуру как аргумент (аналогично тестовой функции или тестовому методу), чтобы фреймворк внедрял ее при выполнении.

Вот как выглядит новая фикстура, создающая (и возвращающая) файл:

@ pytest.fixture
def keyring_file(mon_keyring, tmpdir):
    def generate_file(default=False):
        keyring = tmpdir.join('keyring')
        keyring.write_text(mon_keyring(default=default))
        return keyring.strpath
    return generate_file

Пройдем по этому коду строка за строкой. Декоратор pytest.fixture сообщает фреймворку, что данная функция является фикстурой, далее описывается собственно фикстура с двумя фикстурами, mon_keyring и tmpdir, в качестве аргументов. Первую из них мы создали ранее в файле test_keyring.py, а вторая — встроенная фикстура из фреймворка pytest (больше о встроенных фикстурах вы узнаете в следующем разделе). Фикстура tmpdir позволяет использовать временный каталог, удаляемый по завершении теста, далее создается файл keyring и записывается текст, сгенерированный фикстурой mon_keyring с аргументом default. Наконец, она возвращает абсолютный путь созданного файла для использования тестом.

Вот как тестовая функция могла бы использовать эту фикстуру:

def test_keyring_file_contents(keyring_file):
    keyring_path = keyring_file(default=True)
    with open(keyring_path) as fp:
        contents = fp.read()
    assert "AQBvaBFZAAAAABAA9VHgwCg3rWn8fMaX8KL01A==" in contents

Теперь вы уже хорошо представляете себе, что такое фикстуры, где их можно описать и как использовать в тестах. В следующем разделе рассмотрим некоторые из наиболее удобных встроенных фикстур, входящих в состав фреймворка pytest.

Встроенные фикстуры

В предыдущем разделе мы вкратце упомянули одну из множества встроенных фикстур, доступных в pytest, — фикстуру tmpdir. В этом фреймворке есть еще много фикстур. Полный список доступных фикстур можно просмотреть с помощью следующей команды:

$ (testing) pytest -q --fixtures