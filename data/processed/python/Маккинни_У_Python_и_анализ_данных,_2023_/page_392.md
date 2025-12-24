---
source_image: page_392.png
page_number: 392
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.35
tokens: 7193
characters: 632
timestamp: 2025-12-24T02:50:44.940264
finish_reason: stop
---

Рис. 11.5. Стандартное отклонение суточного оборота Apple

Чтобы вычислить среднее с расширяющимся окном, используйте оператор expanding вместо rolling. В этом случае начальное окно расположено в начале временного ряда и увеличивается в размере, пока не охватит весь ряд. Среднее с расширяющимся окном для временного ряда std250 вычисляется следующим образом:

In [259]: expanding_mean = std250.expanding().mean()

При вызове функции скользящего окна от имени объекта DataFrame преобразование применяется к каждому столбцу (см. рис. 11.6):

In [261]: plt.style.use('grayscale')

In [262]: close_px.rolling(60).mean().plot(logy=True)