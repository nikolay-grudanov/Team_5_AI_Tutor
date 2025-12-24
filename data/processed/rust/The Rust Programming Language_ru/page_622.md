---
source_image: page_622.png
page_number: 622
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.16
tokens: 11415
characters: 804
timestamp: 2025-12-24T10:44:28.744649
finish_reason: stop
---

Листинг 20-23: Отправка и получение значений перечисления Message и выход из цикла, если Worker получает перечисление Message::Terminate

Чтобы встроить в код перечисление Message, нужно изменить Job на Message в двух местах: в объявлении ThreadPool и сигнатуре Worker::new. Метод execute у ThreadPool должен отправлять задания, завёрнутые в вариант Message::NewJob. Затем в Worker::new, где Message получен из канала, задание (job) будет обработано, если получен вариант NewJob и поток выйдет из цикла, если получен вариант Terminate.

С такими изменениями код компилируется и продолжит функционировать так же, как и после кода 20-20. Но мы получим предупреждение, потому что мы не создаём сообщения типа Terminate. Давайте исправим это предупреждение, изменив нашу реализацию Drop как в листинге 20-25.