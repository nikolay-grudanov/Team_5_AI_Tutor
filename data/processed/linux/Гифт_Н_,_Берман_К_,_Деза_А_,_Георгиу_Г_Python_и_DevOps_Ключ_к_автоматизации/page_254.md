---
source_image: page_254.png
page_number: 254
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.52
tokens: 7475
characters: 2001
timestamp: 2025-12-24T03:07:36.377612
finish_reason: stop
---

def test_verify_stdout(capsys):
    stdout_logging()
    out, err = capsys.readouterr()
    assert out == 'stdout output being produced'
    assert err == ''

Фикстура capsys выполняет весь патчинг, настройки и вспомогательные операции по извлечению информации, выведенной в потоки stdout и stderr в ходе теста. Содержимое очищается для каждого нового теста, гарантируя тем самым заполнение переменных правильными значениями.

Но чаще всего, наверное, мы используем фикстуру monkeypatch. При тестировании встречаются ситуации, когда мы не можем похвастаться контролем над тестируемым кодом, и, чтобы добиться конкретного поведения модуля или функции, необходим патчинг. В экосистеме Python существует немало библиотек для патчинга и имитационного моделирования (имитационные объекты (mocks) — это вспомогательные функции, предназначенные для задания поведения пропатченных объектов), но monkeypatch достаточно хороша для того, чтобы вам не нужно было устанавливать отдельную библиотеку.

Следующая функция выполняет системную команду для захвата информации с устройства, после чего производит синтаксический разбор полученного и возвращает свойство (сообщаемое командой blkid ID_PART_ENTRY_TYPE):

import subprocess

def get_part_entry_type(device):
    """
    Производит синтаксический разбор ``ID_PART_ENTRY_TYPE`` из "низкоуровневых" выходных данных (игнорирует кэш) с типом выходных данных ``udev``.
    """
    stdout = subprocess.check_output(['blkid', '-p', '-o', 'udev', device])
    for line in stdout.split('\n'):
        if 'ID_PART_ENTRY_TYPE=' in line:
            return line.split('=')[-1].strip()
    return ''

Чтобы протестировать ее, задайте желаемое поведение в атрибуте check_output модуля subprocess. Вот как выглядит тестовая функция, использующая фикстуру monkeypatch:

def test_parses_id_entry_type(monkeypatch):
    monkeypatch.setattr(
        'subprocess.check_output',
        lambda cmd: '\nID_PART_ENTRY_TYPE=aaaaa')
    assert get_part_entry_type('/dev/sda') == 'aaaa'