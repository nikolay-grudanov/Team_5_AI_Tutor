---
source_image: page_559.png
page_number: 559
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.81
tokens: 7464
characters: 1872
timestamp: 2025-12-24T11:00:28.811003
finish_reason: stop
---

fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>> ) -> Worker {
    let thread = thread::spawn(move || {
        loop {
            let job = receiver.lock().unwrap().recv().unwrap();
            println!("Работник {} получил задание; исполняется.", id);
            ⑥ job.call_box();
        }
    });
    Worker {
        id,
        thread,
    }
}

Сначала мы создаем новый типаж под названием FnBox ①. У него есть один метод call_box ②, похожий на методы call для других типажей Fn*, за исключением того, что он берет self: Box<Self>, чтобы взять self во владение и переместить значение из Box<T>.

Далее мы реализуем типаж FnBox для любого типа F, который реализует типаж FnOnce() ③. Это практически означает, что метод call_box может использоваться любым замыканием FnOnce(). Реализация метода call_box использует (*self)() для перемещения замыкания из Box<T> и вызова замыкания ④.

Теперь нужно, чтобы псевдоним типа Job был типом Box, содержащим все, что реализует новый типаж FnBox ⑤. Это позволит использовать метод call_box в Worker, когда мы получим значение Job, не вызывая замыкание непосредственно ⑥. Реализация типажа FnBox для любого замыкания FnOnce() означает, что не нужно ничего менять в фактических значениях, которые мы посылаем по каналу. Теперь компилятору понятно, что наши действия правильные.

Этот трюк очень хитрый и сложный. Не волнуйтесь, если он выглядит совершенно нелогично, когда-нибудь он станет совершенно ненужным.

При реализации этого трюка пул потоков исполнения находится в рабочем состоянии! Запустите команду cargo run и сделайте несколько запросов:

$ cargo run
    Compiling hello v0.1.0 (file:///projects/hello)
warning: field is never used: `workers`
 --> src/lib.rs:7:5
  |
7 |     workers: Vec<Worker>,
  |     ^^^^^^^^^^^^^^^^^^^^
  = note: #[warn(dead_code)] on by default

warning: field is never used: `id`