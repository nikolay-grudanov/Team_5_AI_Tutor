---
source_image: page_565.png
page_number: 565
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.94
tokens: 7246
characters: 1297
timestamp: 2025-12-24T11:00:31.626625
finish_reason: stop
---

src/lib.rs

enum Message {
    NewJob(Job),
    Terminate,
}

Это перечисление Message будет либо вариантом NewJob, содержащим задание, которое поток должен выполнить, либо вариантом Terminate, побуждающим поток выйти из цикла и остановиться.

Нужно настроить канал для использования значений типа Message вместо Job, как показано в листинге 20.24.

Листинг 20.24. Отправка и получение значений типа Message и выход из цикла, если Worker получает сообщение Message::Terminate

src/lib.rs

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Message>,
}

// --пропуск--

impl ThreadPool {
    // --пропуск--

    pub fn execute<F>(&self, f: F)
        where
            F: FnOnce() + Send + 'static
    {
        let job = Box::new(f);
        self.sender.send(Message::NewJob(job)).unwrap();
    }
}

// --пропуск--

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Message>>>) -> Worker {

        let thread = thread::spawn(move ||{
            loop {
                let message = receiver.lock().unwrap().recv().unwrap();

                match message {
                    Message::NewJob(job) => {
                        println!("Работник {} получил задание; исполняется.", id);

                        job.call_box();
                    },
