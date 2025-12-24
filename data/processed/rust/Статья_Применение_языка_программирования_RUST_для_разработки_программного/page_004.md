---
source_image: page_004.png
page_number: 4
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.94
tokens: 11700
characters: 1682
timestamp: 2025-12-23T22:48:17.016916
finish_reason: stop
---

6. Для настройки компилятора Rustc для архитектуры ARM Cortex-M требуется:
7. Загрузить с сайта [1] и установить утилиту rustup [8], которая позволяет управлять наборами инструментов Rust.
8. Загрузить и установить кросс-компилятор ARM thumbv7em-none-eabihf для сборки программ для отладочной платы.
9. Загрузить и установить утилиту cargo-flash с помощью системы cargo. Данная утилита позволяет загрузить программу в Flash-память устройства после завершения отладки.

![Схема работы системы](https://i.imgur.com/3Q5z5QG.png)

Рис 1. Схема работы системы.

Тестирование
Проверим выводится ли сообщения отладки на компьютер хоста.
Для этого будет использоваться HAL [9]. HAL (Hardware Abstraction Layer) — это слой абстрагирования, реализованный в программном обеспечении, находящийся между физическим уровнем аппаратного обеспечения и программным обеспечением, запускаемом на этом компьютере.
Эта программа инициализирует контроллер. Ниже приведен фрагмент массива функции main.

let cp = cortex_m::Peripherals::take().unwrap();
let dp = pac::Peripherals::take().unwrap();
let pwr = dp.PWR.constrain();
let pwrcfg = pwr.smps().freeze();
let rcc = dp.RCC.constrain();
let ccdr = rcc.sys_ck(100.MHz()).freeze(pwrcfg, &dp.SYSCFG);
let mut _delay = cp.SYST.delay(ccdr.clocks);
hprintln!("HELLO WORLD!").unwrap();

loop {}

Программа компилируется командой:

cargo build --target thumbv7em-none-eabihf

В параметрах команды указывается целевая платформа компиляции.
Отладчик OpenOCD следует запустить в одном окне терминала а отладчик gdb-multiarch с названием исполняемого файла в другом окне. В окне терминала отладчика GDB требуется выполнить следующие команды:

# target remote :3333