---
source_image: page_564.png
page_number: 564
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.68
tokens: 11674
characters: 1610
timestamp: 2025-12-24T02:00:53.734904
finish_reason: stop
---

go = True

def spin(msg, signal): ②
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status)) ④
        time.sleep(.1)
        if not signal.go: ⑤
            break
        write(' ' * len(status) + '\x08' * len(status)) ⑥

def slow_function(): ⑦
    # имитируем ожидание завершения длительной операции ввода-вывода
    time.sleep(3) ⑧
    return 42

def supervisor(): ⑨
    signal = Signal()
    spinner = threading.Thread(target=spin,
        args=('thinking!', signal))
    print('spinner object:', spinner) ⑩
    spinner.start() ⑪
    result = slow_function() ⑫
    signal.go = False ⑬
    spinner.join() ⑭
    return result

def main():
    result = supervisor() ⑮
    print('Answer:', result)

if __name__ == '__main__':
    main()

1 Этот класс определяет простой изменяемый объект с атрибутом go, который понадобится для управления потоком извне.
2 Эта функция будет выполняться в отдельном потоке. Аргумент signal — экземпляр определенного выше класса Signal.
3 Это бесконечный цикл, потому что функция itertools.cycle перебирает заданную последовательность по кругу.
4 Хитрость, позволяющая выполнить анимацию в текстовом режиме: возвращаем курсор назад, печатая символы забоя (\x08).
5 Если атрибут go не равен True, выходим из цикла.
6 Очищаем строку состояния, затирая ее пробелами и возвращая курсор в начало строки.
7 Допустим, что здесь происходит какое-то долгое вычисление.
8 Вызов sleep блокирует главный поток, но — и это очень важно — GIL осво-