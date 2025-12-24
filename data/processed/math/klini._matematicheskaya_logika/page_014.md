---
source_image: page_014.png
page_number: 14
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 87.45
tokens: 12856
characters: 3877
timestamp: 2025-12-24T05:26:10.446728
finish_reason: stop
---

Читатель может принять весь список и на веру, как он принимает на веру таблицу квадратных корней, тригонометрических функций или интегралов.

Надеемся, что читатель сможет применять эти результаты. Большое число из них придется знать на память, чтобы иметь возможность работать, не возвращаясь все время к теореме 2. Мы не требуем, чтобы читатель сейчас же выучил этот список наизусть, но рекомендуем почаще обращаться к нему, чтобы ознакомиться с теми из пунктов, которые чаще всего используются¹).

Теорема 2. При любом выборе формул A, B, C

1a. \( \models A \supset (B \supset A) \).
1b. \( \models (A \supset B) \supset ((A \supset (B \supset C)) \supset (A \supset C)) \).
3. \( \models A \supset (B \supset A \& B) \).
4a. \( \models A \& B \supset A \).
4b. \( \models A \& B \supset B \).
5a. \( \models A \supset A \vee B \).
5b. \( \models B \supset A \vee B \).
7. \( \models (A \supset B) \supset \neg (\neg A \supset \neg B) \supset \neg A \).
9a. \( \models (A \supset B) \supset \neg ((B \supset A) \supset (A \sim B)) \).
10a. \( \models (A \sim B) \supset (A \supset B) \).
10b. \( \models (A \sim B) \supset (B \supset A) \).
(Введение и удаление логических символов.)

*1. \( \models A \supset A \).
*2. \( \models (A \supset B) \supset ((B \supset C) \supset (A \supset C)) \).
*3. \( \models A \supset (B \supset C) \sim \sim (B \supset (A \supset C)) \).
(Принцип тождества, цепное заключение, перестановка посылок, импортация, экспортация.)
*10a. \( \models \neg A \supset (A \supset B) \).
*12a°. \( \models A \supset B \sim \neg B \supset \neg A \).
(Отрицание антецедента, контрапозиция.)

*19. \( \models A \sim A \).
*20. \( \models (A \sim B) \sim (B \sim A) \).
*21. \( \models (A \sim B) \& (B \sim C) \supset (A \sim C) \).
(Рефлексивность, симметричность и транзитивность эквивалентности.)

*31. \( \models (A \& B) \& C \sim A \& (B \& C) \).
*32. \( \models (A \vee B) \vee C \sim \sim A \vee (B \vee C) \).
*33. \( \models A \& B \sim B \& A \).
*34. \( \models A \vee B \sim B \vee A \).
*35. \( \models A \& (B \vee C) \sim \sim (A \& B) \vee (A \& C) \).
*36. \( \models A \vee (B \& C) \sim \sim (A \vee B) \& (A \vee C) \).
*37. \( \models A \& A \sim A \).
*38. \( \models A \vee B \sim A \).
*39. \( \models A \& (A \vee B) \sim A \).
*40. \( \models A \vee (A \& B) \sim A \).
(Законы ассоциативности, коммутативности, дистрибутивности, идемпотентности и элиминации.)

*49°. \( \models \neg \neg A \sim A \).
*50. \( \models \neg (A \& \neg A) \).
*51°. \( \models A \vee \neg A \).
(Закон двойного отрицания, отрицание противоречия, закон исключенного третьего.)

*55a. \( \models \neg (A \vee B) \sim \sim \neg A \& \neg B \).
*55b°. \( \models \neg (A \& B) \sim \sim \neg A \vee \neg B \).
*55c°. \( \models \neg (A \supset B) \sim A \& \neg B \).
(Законы Де Моргана [1847]¹), отрицание импликации.)

*56°. \( \models A \vee B \sim \sim \neg (\neg A \& \neg B) \).
*57°. \( \models A \& B \sim \sim \neg (\neg A \vee \neg B) \).
*58°. \( \models A \supset B \sim \neg (A \& \neg B) \).
*59°. \( \models A \supset B \sim \neg A \vee B \).
*60°. \( \models A \& B \sim \neg (A \supset \neg B) \).
*61°. \( \models A \vee B \sim \neg A \supset B \).
*63a. \( \models (A \sim B) \sim (A \supset B) \& (B \supset A) \).
(Выражение одних связок через другие.)

Упражнения. 3.1. Переделайте пример, предшествующий теореме 1 (с таблицами (a), (b), (c)), для доказательства того, что \( P \vee \neg Q \supset P \vee \neg Q \) общезначима (возьмите в качестве \( A \) не \( P \& \neg P \), а \( P \vee \neg Q \)).

3.2. Установите общезначимость формул из 1а, 4а, 6, 7, *50, *51 посредством указанного выше автоматического метода, но пользуясь, когда сможете, в вычислениях их истинностных таблиц сокращениями.

¹) В словесной форме они восходят по крайней мере к Оккаму («Summa logicae» [1323—9]). См. Лукасевич [1934], Бохенский [1956].