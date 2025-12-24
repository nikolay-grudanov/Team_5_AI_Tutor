---
source_image: page_566.png
page_number: 566
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.84
tokens: 7312
characters: 1430
timestamp: 2025-12-24T11:00:34.889076
finish_reason: stop
---

Для того чтобы встроить тип Message, нужно поменять Job на Message в двух местах: в определении типа ThreadPool ① и в сигнатуре функции Worker::new ③. Метод execute структуры ThreadPool должен отправлять задания, завернутые в вариант Message::NewJob ②. Тогда в функции Worker::new, там, где сообщение поступает из канала ④, задание будет обрабатываться ⑥, если получен вариант NewJob ⑤, и поток будет выходить из цикла ⑧, если получен вариант Terminate ⑦.

Благодаря этим изменениям исходный код будет компилироваться и продолжать функционировать так же, как и после листинга 20.21. Но мы получим предупреждение, потому что мы не создаем никаких сообщений типа Terminate. Давайте устраним это предупреждение, изменив реализацию типажа Drop так, чтобы она выглядела как в листинге 20.25.

Листинг 20.25. Отправка сообщения Message::Terminate работникам перед вызовом метода join для каждого потока worker

src/lib.rs
impl Drop for ThreadPool {
    fn drop(&mut self) {
        println!("Всем работникам отправляется сообщение о завершении.");

        for _ in &mut self.workers {
            self.sender.send(Message::Terminate).unwrap();
        }

        println!("Все работники выключаются.");

        for worker in &mut self.workers {
            println!("Выключается работник {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}