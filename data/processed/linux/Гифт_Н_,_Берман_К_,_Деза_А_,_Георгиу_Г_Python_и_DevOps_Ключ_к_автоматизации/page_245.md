---
source_image: page_245.png
page_number: 245
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.44
tokens: 7298
characters: 1435
timestamp: 2025-12-24T03:07:14.332129
finish_reason: stop
---

• self.assertWarnsRegex(warn, r, fun, *args, **kwds);
• self.assertLogs(logger, level);
• self.assertMultiLineEqual(a, b);
• self.assertSequenceEqual(a, b);
• self.assertListEqual(a, b);
• self.assertTupleEqual(a, b);
• self.assertSetEqual(a, b);
• self.assertDictEqual(a, b);
• self.assertAlmostEqual(a, b);
• self.assertNotAlmostEqual(a, b);
• self.assertGreater(a, b);
• self.assertGreaterEqual(a, b);
• self.assertLess(a, b);
• self.assertLessEqual(a, b);
• self.assertRegex(s, r);
• self.assertNotRegex(s, r);
• selfassertCountEqual(a, b).

pytest дает возможность пользоваться исключительно assert и не требует применения чего-либо из перечисленного. Более того, он позволяет писать тесты с помощью unittest и даже выполняет их. Мы настоятельно рекомендуем этого не делать и предлагаем вам задействовать простые операторы assert.

Использовать простые операторы assert не только удобнее — pytest также предоставляет обладающий большими возможностями механизм сравнения для случая непрохождения тестов (больше об этом расскажем в следующем разделе).

Возможности pytest

Помимо упрощения написания и выполнения тестов, фреймворк pytest предоставляет множество расширяемых опций, в частности точек подключения. Они позволяют взаимодействовать с внутренними механизмами фреймворка на различных этапах выполнения. Например, можно добавить точку подключения для механизма сбора тестов, чтобы внести изменения в процесс сбора. Еще один