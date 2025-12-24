---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.58
tokens: 7298
characters: 1489
timestamp: 2025-12-24T03:03:22.989231
finish_reason: stop
---

По завершении процесса функция subprocess.run возвращает экземпляр CompletedProcess. В данном случае мы выполняем инструкцию командной оболочки ls с аргументом -l для просмотра содержимого текущего каталога. С помощью параметра capture_output указываем, что необходимо захватить содержимое потоков вывода stdout и stderr. А затем обращаемся к результатам с помощью cp.stdout. Если выполнить команду ls в несуществующем каталоге, вызвав ошибку, мы увидим результаты в cp.stderr:

In [3]: cp = subprocess.run(['ls','/doesnotexist'],
    capture_output=True,
    universal_newlines=True)
In [4]: cp.stderr
Out[4]: 'ls: /doesnotexist: No such file or directory\n'

Лучше сразу включить в команду обработку ошибок с помощью параметра check. Если он равен true, в случае сообщения от подпроцесса об ошибке будет генерироваться исключение:

In [5]: cp = subprocess.run(['ls', '/doesnotexist'],
    capture_output=True,
    universal_newlines=True,
    check=True)
------------------------------------------------------------
CalledProcessError                                 Traceback (most recent call last)
<ipython-input-23-c0ac49c40fee> in <module>
----> 1 cp = subprocess.run(['ls', '/doesnotexist'],
      capture_output=True,
      universal_newlines=True,
      check=True)

~/.pyenv/versions/3.7.0/lib/python3.7/subprocess.py ...
    466        if check and retcode:
    467            raise CalledProcessError(retcode, process.args,
--> 468                output=stdout, stderr=stderr)