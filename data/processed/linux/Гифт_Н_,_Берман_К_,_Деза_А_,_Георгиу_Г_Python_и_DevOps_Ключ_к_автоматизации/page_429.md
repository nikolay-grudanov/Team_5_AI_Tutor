---
source_image: page_429.png
page_number: 429
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.24
tokens: 7397
characters: 1816
timestamp: 2025-12-24T03:12:09.560129
finish_reason: stop
---

data=todo_data) as resp:
    assert resp.status == 200

@scenario(weight=10)
async def _test_update_todo(session):
    base_url= molotov.get_var('base_url')
    # Выводим список всех todo
    async with session.get(base_url + '/todos') as resp:
        res = await resp.json()
        assert resp.status == 200, resp.status
        # Выбираем случайный элемент todo и обновляем его
        # с помощью запроса PUT
        todo_id = random.choice(res)['id']
        todo_data = json.dumps({'text':
            'Updated existing todo during Taurus/molotov load test'})
        async with session.put(base_url + '/todos/' + todo_id,
            data=todo_data) as resp:
            assert resp.status == 200

@scenario(weight=10)
async def _test_delete_todo(session):
    base_url= molotov.get_var('base_url')
    # Выводим список всех todo
    async with session.get(base_url + '/todos') as resp:
        res = await resp.json()
        assert resp.status == 200, resp.status
        # Выбираем случайный элемент todo и обновляем его
        # с помощью запроса PUT
        todo_id = random.choice(res)['id']
        async with session.delete(base_url + '/todos/' + todo_id) as resp:
            assert resp.status == 200

Этот сценарий включает четыре функции, снабженные декораторами scenario, для выполнения их с помощью Molotov. Они тестируют различные конечные точки API CRUD REST. Веса определяют долю общей длительности теста, отводимую на каждый из сценариев. Например, длительность вызова функции _test_list_todos составляет здесь примерно 50 % времени, _test_create_todo — около 30 % времени, а _test_update_todo и _test_delete_todo будут выполняться примерно по 10 % времени каждая.

Собираем локальный образ Docker:

$ docker build -t cdk-loadtest .

Создаем локальный каталог artifacts:

$ mkdir artifacts