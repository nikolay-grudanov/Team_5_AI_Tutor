---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.10
tokens: 7390
characters: 1741
timestamp: 2025-12-24T03:03:18.171084
finish_reason: stop
---

print(f"\tlast accessed: {last_access}")
    print(f"\tsize: {size}")
    elif os.path.isdir(child_path): ⑥
        walk_path(child_path) ⑦

if __name__ == '__main__':
    fire.Fire()

① os.listdir возвращает содержимое каталога.

② Формируем полный путь элемента, находящегося в родительском каталоге.

③ Проверяем, не соответствует ли этот путь файлу.

④ Получаем время последнего обращения к данному файлу.

⑤ Получаем размер данного файла.

⑥ Проверяем, не соответствует ли этот путь каталогу.

⑦ Обходим дерево, начиная с этого каталога.

С помощью подобных сценариев можно находить большие файлы или файлы, к которым пока что не обращались, а затем сообщать о них пользователю, перемещать или удалять их.

Обход дерева каталогов с помощью os.walk

Модуль os включает удобную функцию os.walk для обхода деревьев каталогов, которая возвращает генератор, который, в свою очередь, на каждой итерации возвращает кортеж, состоящий из текущего пути, списка каталогов и списка файлов. В примере 2.4 мы перепишем функцию walk_path из примера 2.3, применив функцию os.walk. Как вы видели в предыдущем примере, при использовании os.walk не нужно проверять, какие пути соответствуют файлам, или повторно вызывать функцию для каждого подкаталога.

Пример 2.4. Переписываем функцию walk_path
def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")