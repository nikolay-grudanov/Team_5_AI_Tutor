---
source_image: page_244.png
page_number: 244
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.97
tokens: 7329
characters: 1529
timestamp: 2025-12-24T03:07:14.131984
finish_reason: stop
---

Отличия от unittest

Python изначально включает набор утилит и вспомогательных функций для тестирования, входящих в состав модуля unittest. Так что не помешает понимать, чем отличается pytest и почему именно его рекомендуется применять.

Модуль unittest навязывает использование классов и их наследование. Это не проблема для опытного разработчика, хорошо разбирающегося в объектно-ориентированном программировании и наследовании классов, но для начинающих становится препятствием. Нельзя требовать применения классов и наследования для написания простейших тестов!

В частности, из-за необходимости наследовать от класса unittest.TestCase разработчику приходится знать (и помнить) большинство методов-операторов контроля, применяемых для верификации результатов. При использовании pytest за все это отвечает одна-единственная вспомогательная функция контроля assert.

Вот лишь часть методов-операторов контроля, которые можно задействовать при написании тестов на основе unittest. Понять суть некоторых из них несложно, но разобраться с частью прочих весьма непросто:

• self.assertEqual(a, b);
• self.assertNotEqual(a, b);
• self.assertTrue(x);
• self.assertFalse(x);
• self.assertIs(a, b);
• self.assertIsNot(a, b);
• self.assertIsNone(x);
• self.assertIsNotNone(x);
• self.assertIn(a, b);
• self.assertNotIn(a, b);
• self.assertIsInstance(a, b);
• self.assertNotIsInstance(a, b);
• self.assertRaises(exc, fun, *args, **kwds);
• self.assertRaisesRegex(exc, r, fun, *args, **kwds);
• self.assertWarns(warn, fun, *args, **kwds);