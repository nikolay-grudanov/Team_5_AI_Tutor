---
source_image: page_005.png
page_number: 5
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.89
tokens: 11559
characters: 1200
timestamp: 2025-12-23T22:48:25.008341
finish_reason: stop
---

load
monitor arm semihosting enable
continue

В результате в терминале с OpenOCD мы получим наше сообщение. Вывод представлен на рис. 2.

![Скриншот терминала с выводом программы тестирования](https://i.imgur.com/3Q5z5QG.png)

Рис 2. Вывод программы тестирования.

Разработка программы
После проверки правильности работы системы сборки приступим к разработке демонстрационной программы, которая взаимодействует с периферией.
Разработаем программу управления светодиодом на отладочной плате на языке Rust. Для этого создадим новый проект. Текст программы приведен ниже.

let cp = cortex_m::Peripherals::take().unwrap();
let dp = pac::Peripherals::take().unwrap();
let pwr = dp.PWR.constrain();
let pwrcfg = pwr.smps().freeze();
let rcc = dp.RCC.constrain();
let ccdr = rcc.sys_ck(100.MHz()).freeze(pwrcfg, &dp.SYSCFG);
let mut delay = cp.SYST.delay(ccdr.clocks);
let gpioc = dp.GPIOC.split(ccdr.peripheral.GPIOC);
let mut led = gpioc.pc3.into_push_pull_output();
loop {
    led.set_high();
    delay.delay_ms(500_u16);
    led.set_low();
    delay.delay_ms(1000_u16);
}

Программы загружается на устройство STM32H735DK с помощью утилиты cargo-flash командой

cargo flash --release --chip STM32H735IGK6