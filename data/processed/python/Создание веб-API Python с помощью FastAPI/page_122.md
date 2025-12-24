---
source_image: page_122.png
page_number: 122
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.11
tokens: 8313
characters: 1289
timestamp: 2025-12-24T02:19:12.550921
finish_reason: stop
---

return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

Первый метод, get(), принимает идентификатор в качестве аргумента метода и возвращает соответствующую запись из базы данных, в то время как метод get_all() не принимает аргументов и возвращает список всех записей, имеющихся в базе данных.

Обновить

Давайте создадим метод для обработки процесса обновления существующей записи:

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k:v for k,v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

В этом блоке кода метод update принимает ID и ответственную схему Pydantic, которая будет содержать поля, обновленные из запроса PUT отправленного клиентом. Обновленное тело запроса сначала анализируется в словаре, а затем фильтруется для удаления значений None.
Как только это будет сделано, он вставляется в запрос на обновление, который, наконец, выполняется методом update() Beanie.