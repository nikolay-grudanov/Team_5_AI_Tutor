---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.58
tokens: 7380
characters: 1902
timestamp: 2025-12-24T03:07:26.408193
finish_reason: stop
---

Особенно часто мы используем две фикстуры, упомянутые в списке, выводимом предыдущей командой, — monkeypatch и capsys. Вот краткое их описание, которое вы увидите в терминале:

capsys
    enables capturing of writes to sys.stdout/sys.stderr and makes captured output available via ``capsys.readouterr()`` method calls which return a ``(out, err)`` tuple.
monkeypatch
    The returned ``monkeypatch`` funcarg provides these helper methods to modify objects, dictionaries or os.environ::

    monkeypatch.setattr(obj, name, value, raising=True)
    monkeypatch.delattr(obj, name, raising=True)
    monkeypatch.setitem(mapping, name, value)
    monkeypatch.delitem(obj, name, raising=True)
    monkeypatch.setenv(name, value, prepend=False)
    monkeypatch.delenv(name, value, raising=True)
    monkeypatch.syspath_prepend(path)
    monkeypatch.chdir(path)

All modifications will be undone after the requesting test function has finished. The ``raising`` parameter determines if a KeyError or AttributeError will be raised if the set/deletion operation has no target.

Фикстура capsys захватывает всю информацию, выводимую в ходе теста в потоки stdout и stderr. Пытались ли вы когда-нибудь проверить, что выводит какая-либо команда в консоль или журнал при модульном тестировании? Реализовать это правильно весьма непросто и иногда требует отдельного плагина или библиотеки для внесения временных изменений (патчинга) во внутреннее содержание Python и его последующего изучения.

Вот две тестовые функции для проверки информации, выведенной в потоки stdout и stderr соответственно:

import sys

def stderr_logging():
    sys.stderr.write('stderr output being produced')

def stdout_logging():
    sys.stdout.write('stdout output being produced')

def test_verify_stderr(capsys):
    stderr_logging()
    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'stderr output being produced'