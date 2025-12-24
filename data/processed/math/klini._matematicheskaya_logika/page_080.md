---
source_image: page_080.png
page_number: 80
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 115.81
tokens: 13700
characters: 6060
timestamp: 2025-12-24T05:31:34.657091
finish_reason: stop
---

из \( \forall x \neg A(x) \), получаем по \( \forall \)-удал. \( \neg A(x) \), что противоречит \( A(x) \). По слабому \( \neg \)-удал. \( \neg \forall x \neg A(x) \). Так как ни эта формула, ни допущения \( \forall x \neg A(x) \), \( \exists xA(x) \), отличные от \( A(x) \), не содержат свободно \( x \), мы можем теперь завершить \( \exists \)-удал., а затем \( \neg \)-введ. (учтя противоречие с \( \forall x \neg A(x) \)) и получаем \( \neg \exists xA(x) \):

1. \( \neg \exists xA(x) \) — допущение.
2. \( A(x) \) — допущение.
3. \( \exists xA(x) \) — \( \exists \)-введ., 2.
4. \( \neg A(x) \) — \( \neg \)-введ., 3, 1.
5. \( \forall x \neg A(x) \) — \( \forall \)-введ., 4.
6. \( \neg \exists xA(x) \supset \forall x \neg A(x) \) — \( \supset \)-введ., 5.
7. \( \forall x \neg A(x) \) — допущение.
8. \( \exists xA(x) \) — допущение.
9. \( A(x) \) — допущение.
10. \( \neg A(x) \) — \( \forall \)-удал., 7.
11. \( \neg \forall x \neg A(x) \) — слабое \( \neg \)-удал., 9, 10.
12. \( \neg \forall x \neg A(x) \) — \( \exists \)-удал., 11.
13. \( \neg \exists xA(x) \) — \( \neg \)-введ., 7, 12.
14. \( \forall x \neg A(x) \supset \neg \exists xA(x) \) — \( \supset \)-введ., 13.
15. \( \neg \exists xA(x) \sim \forall x \neg A(x) \) — \( \sim \)-введ., 6, 14.

1. \( \neg \exists xA(x) \vdash \neg \exists xA(x) \).
2. \( A(x), \neg \exists xA(x) \vdash A(x) \).
3. \( A(x), \neg \exists xA(x) \vdash \exists xA(x) \) — \( \exists \)-введ., 2.
4. \( \neg \exists xA(x) \vdash \neg A(x) \) — \( \neg \)-введ., 3, 1.
5. \( \neg \exists xA(x) \vdash \forall x \neg A(x) \) — \( \forall \)-введ., 4.
6. \( \neg \exists xA(x) \vdash \forall x \neg A(x) \) — \( \supset \)-введ., 5.
7. \( \forall x \neg A(x) \vdash \forall x \neg A(x) \).
8. \( \exists xA(x), \forall x \neg A(x) \vdash \exists xA(x) \).
9. \( A(x), \exists xA(x), \forall x \neg A(x) \vdash A(x) \).
10. \( A(x), \exists xA(x), \forall x \neg A(x) \vdash \neg A(x) \) — \( \forall \)-удал., 7.
11. \( A(x), \exists xA(x), \forall x \neg A(x) \vdash \neg \forall x \neg A(x) \) — слабое \( \neg \)-удал., 9, 10.
12. \( \exists xA(x), \forall x \neg A(x) \vdash \neg \forall x \neg A(x) \) — \( \exists \)-удал., 11.
13. \( \forall x \neg A(x) \vdash \neg \exists xA(x) \) — \( \neg \)-введ., 7, 12.
14. \( \forall x \neg A(x) \supset \neg \exists xA(x) \) — \( \supset \)-введ., 13.
15. \( \neg \exists xA(x) \sim \forall x \neg A(x) \) — \( \sim \)-введ., 6, 14.

На каждом шаге рассуждений (\( B_2 \)) можно использовать те результаты, которые не расположены напротив других стрелок. Так, для строки 4 можно в целях \( \neg \)-введ. использовать строку 1, которую мы рассматриваем как один из двух «данных выводов», ибо соотношение \( \neg \exists xA(x) \vdash \neg \exists xA(x) \) дает нам (в силу общих свойств \( \vdash \)) \( A(x), \neg \exists xA(x) \vdash \neg \exists xA(x) \). Хотя мы можем в строках 9—11 устранить допущение \( \exists xA(x) \), мы предпочитаем его сохранить в силе со строки 8 до строки 12 с тем, чтобы \( \exists \)-удал., примененное к строке 11, непосредственно дало бы \( \exists xA(x), \exists xA(x), \forall x \neg A(x) \vdash \neg \forall x \neg A(x) \). (Ср. 12—17 из (\( B_3 \)) примера 9 § 13.)

*82b. Используем метод цепей, которым мы уже располагаем в силу § 24. \( \vdash \exists x \neg A(x) \sim \neg \neg \exists x \neg A(x) [*49] \sim \neg \forall x \neg \neg A(x) [*82a] \sim \neg \forall xA(x) [*49] \).

*87—*94. Эти результаты можно устанавливать попарно, как будет показано для *91 и *92 (*88, *90, *94 можно установить также прямыми методами, аналогично *91):

*91. I. Допустим \( _1A & \exists xB(x) \), подготавливая \( \supset \)-введ. Отсюда по \( & \)-удал. \( _2A \) и \( _3\exists xB(x) \). Подготавливая \( \exists \)-удал., допустим \( _4B(x) \). По \( & \)-введ. \( _5A & B(x) \), по \( \exists \)-введ. \( _6\exists x(A & B(x)) \).

\( (B_1) \) Теперь завершаем \( \exists \)-удал., а затем \( \supset \)-введ.
II. Пусть \( _9\exists x(A & B(x)) \). Подготавливая \( \exists \)-удал., допустим \( _{10}A & B(x) \). По \( & \)-удал. \( _{11}A \) и \( _{12}B(x) \). По \( \exists \)-введ. \( _{13}\exists xB(x) \). По \( & \)-введ. \( _{14}A & \exists xB(x) \). Завершаем \( \exists \)-удал. и \( \supset \)-введ.

*92. \( \vdash A \forall \forall xB(x) \sim \neg (\neg A & \neg \forall xB(x)) [*56] \sim \neg (\neg A & \exists x \neg B(x)) [*82b] \sim \neg \exists x (\neg A & \neg B(x)) [*91] \sim \neg \forall x (\neg A & \neg B(x)) [*82a] \sim \forall x (A \vee B(x)) [*56].

*95—*99b. Все эти результаты можно получить методом цепей из *90, *92, *94, пользуясь *59 (\( \vdash A \supset B \sim \neg A \vee B \)), *82a, *82b (и *34). При некоторой практике эти преобразования можно делать в уме, поэтому ими можно пользоваться, когда нужно вспомнить 95—99b, если помнить *88—*94. (Некоторые из этих формул можно также получить прямыми методами.)

Нужно заметить, что *87 и *88 являются теоремами, тогда как аналогичные формулы с \( \forall \) и \( \vee \) или с \( \exists \) и \( & \) теоремами не являются (ими будут только *94 и *93) Это происходит потому, что квантор \( \forall \) родствен связке \( & \) (можно мыслить \( \forall \) как конъюнкцию, распространенную на область \( D \); например, если \( D = \{1, 2, 3\} \), то \( \forall x P(x) \) означает то же, что \( P(1) & P(2) & P(3) \), в том расширении исчисления предикатов, которое получается присоединением символов «1», «2», «3» в качестве имен элементов из \( D \)). Аналогичное родство есть между \( \exists \) и \( \vee \).

Теорема 6° и ее следствие° обобщаются на исчисление предикатов с \( \vdash \) (вместо \( \models \)), причем в операцию \( \vdash \) теперь включаем также взаимную замену \( \forall \) и \( \exists \)¹). Доказательство проводится, как и раньше, только дополнительно используются *82a и *82b.

¹) Единственное, чего недостает для обобщения теоремы 7 (принципа двойственности) на исчисление предикатов с \( \vdash \) (операция \( \vdash \) включает теперь и взаимную замену кванторов), — это простого частного случая правила подста-