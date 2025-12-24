---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 72.97
tokens: 12744
characters: 4338
timestamp: 2025-12-24T05:42:01.188758
finish_reason: stop
---

ПРИЛОЖЕНИЯ

Г. Е. Минц

ПРИЛОЖЕНИЕ 1

Нормализация доказательств

Приведем обещанное (примечание на стр. 396) доказательство того, что любое доказательство в G4a с сечением можно путем конечного числа стандартных шагов (редукций) нормализовать, т. е. перестроить в доказательство в исходной формулировке G4a без сечения. Начиная с этого места, мы будем, не оговаривая этого особо, рассматривать лишь доказательства, обладающие свойством чистоты переменных, ограничиваясь, тем самым, секвенциями, в которые никакая переменная не входит и свободно, и связанно.

Произведением секвенций \( \Gamma \rightarrow \Delta \) и \( \Sigma \rightarrow \Lambda \) назовем, следуя Клини [1952], секвенцию \( \Gamma, \Sigma \rightarrow \Delta, \Lambda \).

Степенью формулы называется число вхождений в нее операторов \( \&,\lor,\neg,\sim;\exists,\forall \). Степенью сечения

\[
\frac{\Delta \rightarrow \Lambda, C}{\Delta, \Gamma \rightarrow \Theta, \Lambda}
\]

называется степень формулы C, которая называется формулой сечения.

Пусть k — натуральное число, F — список формул. Доказательство в G4a с сечением назовем \((k, F)\)-доказательством, если в нем все формулы сечения имеют степень \(\leq k\), а те из них, которые имеют степень k, содержатся в списке F. Вместо «имеется \((k, F)\)-доказательство секвенции S» будем писать \(|(k, F)S|\).

Лемма 1. (Обращение правил.)
1. Если \(|(k, F)\Delta \rightarrow \Lambda, A\&B|\), то \(|(k, F)\Delta \rightarrow \Lambda, A|\) и \(|(k, F)\Delta \rightarrow \Lambda, B|\).
2. Если \(|(k, F)\Delta \rightarrow \Lambda, \forall xA(x)|\), то \(|(k, F)\Delta \rightarrow \Lambda, A(t)|\), если t не содержит связанных переменных из \(A, \Lambda, \forall xA(x)\).
3. Если \(|(k, F)\Delta \rightarrow \Lambda, A \supset B|\), то \(|(k, F)A, \Delta \rightarrow \Lambda, B|\).
4. Если \(|(k, F)\Delta \rightarrow \Lambda, \neg A|\), то \(|(k, F)A, \Delta \rightarrow \Lambda|\).

5. Если \(|(k, F)\Delta \rightarrow \Lambda, A \sim B|\), то \(|(k, F)A, \Delta \rightarrow \Lambda, B|\) и \(|(k, F)B, \Delta \rightarrow \Lambda, A|\).
6. Если \(|(k, F)A \lor B, \Gamma \rightarrow \Theta|\), то \(|(k, F)A, \Gamma \rightarrow \Theta|\) и \(|(k, F)B, \Gamma \rightarrow \Theta|\).
7. Если \(|(k, F)\exists xA(x), \Gamma \rightarrow \Theta|\), то \(|(k, F)A(t), \Gamma \rightarrow \Theta|\), если t не содержит связанных переменных из \(A, \Theta, \exists xA(x)\).

Доказательство. 1. Заменяя в \((k, F)\)-доказательстве секвенции \(A \rightarrow \Lambda, A\&B\) все предки указанного явно сукцедентного вхождения \(A\&B\), имеющие вид \(A\&B\), на \(A\) и вычеркивая левые посылки соответствующих \(\rightarrow \&\) и все, что стоит над правыми посылками, получаем искомое доказательство секвенции \(A \rightarrow \Lambda, A\):

\[
\begin{array}{c}
\Delta_1 \rightarrow \Lambda_1, A \\
\Delta_1 \rightarrow \Lambda_1, A\&B \\
\Delta_1 \rightarrow \Lambda_1', A\&B \\
\Delta \rightarrow \Lambda, A\&B
\end{array}
\]
\[
\begin{array}{c}
\Delta_1 \rightarrow \Lambda_1, B \\
\Delta_1 \rightarrow \Lambda_1', A \\
\Delta \rightarrow \Lambda, A
\end{array}
\]

Здесь \(A_1'\) обозначает результат вычеркивания предков \(A\&B\) из \(A_1\).

2. Переименовывая, если нужно, в данном \((k, F)\)-доказательстве переменные b правил \(\rightarrow \forall\) и \(\exists \rightarrow\), а также связанные переменные, не входящие в нижнюю секвенцию, добиваемся, чтобы t не содержал упомянутых переменных. Теперь проходит тот же прием, что и в случае 1: все предки \(\forall xA(x)\), имеющие вид \(\forall xA(x)\), заменяются на \(A(t)\); над посылками соответствующих \(\rightarrow \forall\) делается подстановка t вместо переменной b:

\[
\begin{array}{c}
\Delta_1 \rightarrow \Lambda_1, A(b) \\
\Delta_1 \rightarrow \Lambda_1, \forall xA(x) \\
\Delta \rightarrow \Lambda, \forall xA(x)
\end{array}
\]
\[
\begin{array}{c}
\Delta_1 \rightarrow \Lambda_1, A(t) \\
\Delta \rightarrow \Lambda, A(t)
\end{array}
\]

3. Исходное доказательство показано слева, результирующее — справа:

\[
\begin{array}{c}
A, \Delta_1 \rightarrow \Lambda_1, B \\
\Delta_1 \rightarrow \Lambda_1, A \supset B \\
\Delta \rightarrow \Lambda, A \supset B
\end{array}
\]
\[
\begin{array}{c}
A, \Lambda_1 \rightarrow \Lambda_1', B \\
A, \Delta \rightarrow \Lambda, B
\end{array}
\]

4—7. Аналогично

Лемма 2. Если \(|(0, F \cup \{C\})S|\), то \(|(0, F)S|\).