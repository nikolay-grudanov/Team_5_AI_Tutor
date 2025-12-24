---
source_image: page_079.png
page_number: 79
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 123.06
tokens: 13817
characters: 6039
timestamp: 2025-12-24T05:31:35.145765
finish_reason: stop
---

**81. \( \vdash \forall x A(x) \supset \exists x A(x) \).
**82. \( \vdash \exists x \forall y A(x, y) \supset \forall y \exists x A(x, y) \).
(Изменения кванторов.)

*82a. \( \vdash \neg \exists x A(x) \sim \forall x \neg A(x) \). *82b°. \( \vdash \neg \forall x A(x) \sim \exists x \neg A(x) \).
*83°. \( \vdash \exists x A(x) \sim \neg \forall x \neg A(x) \). *84°. \( \vdash \forall x A(x) \sim \neg \exists x \neg A(x) \).
(Отрицание и кванторы.)

*87. \( \vdash \forall x A(x) \& \forall x B(x) \sim \forall x (A(x) \& B(x)) \).
*88. \( \vdash \exists x A(x) \vee \exists x B(x) \sim \exists x (A(x) \vee B(x)) \).
*89. \( \vdash A \& \forall x B(x) \sim \forall x (A \& B(x)) \).
*90. \( \vdash A \vee \exists x B(x) \sim \exists x (A \vee B(x)) \).
*91. \( \vdash A \& \exists x B(x) \sim \exists x (A \& B(x)) \).
*92°. \( \vdash A \vee \forall x B(x) \sim \forall x (A \vee B(x)) \).
*93. \( \vdash \exists x (A(x) \& B(x)) \supset \exists x A(x) \& \exists x B(x) \).
*94. \( \vdash \forall x A(x) \vee \forall x B(x) \supset \forall x (A(x) \vee B(x)) \).
(Конъюнкция или дизъюнкция и кванторы.)

*95. \( \vdash A \supset \forall x B(x) \sim \forall x (A \supset B(x)) \)
*97°. \( \vdash A \supset \exists x B(x) \sim \exists x (A \supset B(x)) \).
*98°. \( \vdash \forall x A(x) \supset B \sim \exists x (A(x) \supset B) \).
*96. \( \vdash \exists x A(x) \supset B \sim \forall x (A(x) \supset B) \).
*99°. \( \vdash \forall x A(x) \supset \exists x B(x) \sim \exists x (A(x) \supset B(x)) \).
*99b. \( \vdash (\exists x A(x) \supset \forall x B(x)) \supset \forall x (A(x) \supset B(x)) \).
(Импликация и кванторы.)

Доказательства.
*75. 1. \( \forall x A \vdash A - \forall\text{-удал.} \) (здесь x играет роль x и r, а A играет роль A(x), так что r тривиально свободна для x в A(x)).
2. \( \vdash \forall x A \supset A - \supset\text{-введ.}, 1 \).
(A) 3. \( A \vdash A \).
4. \( A \vdash \forall x A - \forall\text{-введ.}, 3 \) (можно, так как A не содержит свободно x).
5. \( \vdash A \supset \forall x A - \supset\text{-введ.}, 4 \).
6. \( \forall x A \sim A - \sim\text{-введ.}, 2, 5 \).

(B₁) I. Допустим, что \( \forall x A \) (подготавливая \( \supset\text{-введ.} \)). По \( \forall\text{-удал.}-\text{имеем } \forall A \).
II. Допустим \( \forall A \), куда не входит свободно x. По \( \forall\text{-введ.} \) имеем \( \forall x A \).

\( \downarrow \)
1. \( \forall x A - \text{допущение.} \)
\( \downarrow \)
2. \( A - \forall\text{-удал.}, 1 \).
\( \downarrow \)
3. \( \forall x A \supset A - \supset\text{-введ.}, 2 \).
\( \downarrow \)
4. \( A - \text{допущение.} \)
\( \downarrow \)
5. \( \forall x A - \forall\text{-введ.}, 4 \).
\( \downarrow \)
6. \( A \supset \forall x A - \supset\text{-введ.}, 5 \).
7. \( \forall x A \sim A - \sim\text{-введ.}, 3, 6 \).

(B₂)
1. \( \forall x A \vdash \forall x A \).
2. \( \forall x A \vdash A - \forall\text{-удал.}, 1 \).
3. \( \vdash \forall x A \supset A - \supset\text{-введ.}, 2 \).
(B₃)
4. \( A \vdash A \).
5. \( A \vdash \forall x A - \forall\text{-введ.}, 4 \).
6. \( \vdash A \supset \forall x A - \supset\text{-введ.}, 5 \).
7. \( \vdash \forall x A \sim A - \sim\text{-введ.}, 3, 6 \).

*76. 1. \( A \vdash A \).
2. \( \exists x A \vdash A - \exists\text{-удал.}, 1 \) (заметим, что формула A, играющая роль C, не содержит свободно x).
3. \( \vdash \exists x A \supset A - \supset\text{-введ.}, 2 \).
4. \( A \supset \exists x A - \exists\text{-введ.} \) (x играет роль r).
5. \( \vdash A \supset \exists x A - \supset\text{-введ.}, 4 \).
6. \( \vdash \exists x A \sim A - \sim\text{-введ.}, 3, 5 \).

*80. 1. \( A(x, x) \vdash \exists x \exists y A(x, y) - \text{двойное } \exists\text{-введ.} \) (первый раз с у в роли x, а х в роли r, используя то, что х свободен для у в A(x, y); второй раз х играет роль и х и r) или в силу следствия 1 (b) теоремы 21.
(A) 2. \( \exists x A(x, x) \vdash \exists x \exists y A(x, y) - \exists\text{-удал.}, 1 \) (если в качестве С взять \( \exists x \exists y A(x, y) \), то в C не входит свободно x).
3. \( \vdash \exists x A(x, x) \supset \exists x \exists y A(x, y) - \supset\text{-введ.}, 2 \).

*82a. 1. \( \neg \exists x A(x), A(x) \vdash \neg \exists x A(x) \).
2. \( \neg \exists x A(x), A(x) \vdash \exists x A(x) - \exists\text{-введ.} \) (x в роли r).
3. \( \neg \exists x A(x) \vdash \neg A(x) - \neg\text{-введ.}, 2, 1 \).
4. \( \neg \exists x A(x) \vdash \forall x \neg A(x) - \forall\text{-введ.}, 3 \) (так как \( \neg \exists x A(x) \) не содержит свободно x и может рассматриваться как Г).
5. \( \vdash \neg \exists x A(x) \supset \forall x \neg A(x) - \supset\text{-введ.}, 4 \).
(A) 6. \( \forall x \neg A(x), A(x) \vdash A(x) \).
7. \( \forall x \neg A(x), A(x) \vdash \neg A(x) - \forall\text{-удал.} \).
8. \( \forall x \neg A(x), A(x) \vdash \neg \forall x \neg A(x) - \neg\text{-введ.}, 6, 7 \).
9. \( \forall x \neg A(x), \exists x A(x) \vdash \neg \forall x \neg A(x) - \exists\text{-удал.}, 8 \) (замечая, что ни \( \neg \forall x \neg A(x) \) в роли C, ни \( \forall x \neg A(x) \) в роли Г не содержат свободно x).
10. \( \forall x \neg A(x), \exists x A(x) \vdash \forall x \neg A(x) \).
11. \( \forall x \neg A(x) \vdash \neg \exists x A(x) - \neg\text{-введ.}, 10, 9 \).
12. \( \vdash \forall x \neg A(x) \supset \neg \exists x A(x) - \supset\text{-введ.}, 11 \).
13. \( \vdash \neg \exists x A(x) \sim \forall x \neg A(x) - \sim\text{-введ.}, 5, 12 \).

I. Пусть \( \neg \exists x A(x) \). Подготавливая \( \neg\text{-введ.} \), допустим \( \forall A(x) \). По \( \exists\text{-введ.} \) \( \exists x A(x) \), что противоречит \( \neg \exists x A(x) \).
Значит, \( \neg A(x) \) в силу \( \neg\text{-введ.} \) (освобождаясь от допущения A(x)). По \( \forall\text{-введ.} \) (которое возможно, ибо оставшееся допущение \( \neg \exists x A(x) \) не содержит x свободно) \( \forall x \neg A(x) \).
(B₁) II. Пусть \( \forall x \neg A(x) \). Подготавливая \( \neg\text{-введ.} \), допустим \( \exists x A(x) \). Подготавливая \( \exists\text{-удал.} \), допустим \( \forall A(x) \). Исходя