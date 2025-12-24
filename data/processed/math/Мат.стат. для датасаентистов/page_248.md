---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.35
tokens: 11751
characters: 1633
timestamp: 2025-12-24T06:17:13.036191
finish_reason: stop
---

<table>
  <tr>
    <th></th>
    <th>1089</th>
    <th>425</th>
    <th>0.2807133</th>
  </tr>
  <tr>
    <th>default</th>
    <th>731</th>
    <th>755</th>
    <th>0.4919246</th>
  </tr>
</table>

По умолчанию натренировано 500 деревьев. Поскольку в наборе предикторов имеется всего две переменные, алгоритм в произвольном порядке отбирает переменную, по которой можно выполнить разбиение на каждом этапе (т. е. бутстропскую подвыборку размера 1).

Внепакетная оценка OOB (out-of-bag — не вошедший в пакет) ошибки — это коэффициент ошибок для натренированных моделей, применяемый к данным, отложенным в сторону из тренировочного набора для этого дерева. Используя выходные данные из модели, ошибку OOB можно отобразить на графике против числа деревьев в случайном лесе:

error_df = data.frame(error_rate = rf$err.rate[, 'OOB'],
                      num_trees = 1:rf$ntree)
ggplot(error_df, aes(x=num_trees, y=error_rate)) +
geom_line()

Результат показан на рис. 6.6. Коэффициент ошибок быстро уменьшается примерно с 0,44 до стабилизации на уровне 0,385. Предсказанные значения могут быть получены из функции predict и отображены на графике следующим образом:

pred <- predict(loan_lda)
rf_df <- cbind(loan3000, pred_default=pred[, 'default']>.5)
ggplot(data=rf_df, aes(x=borrower_score, y=payment_inc_ratio,
                       color=pred_default, shape=pred_default)) +
geom_point(alpha=.6, size=2) +
scale_shape_manual(values=c(46, 4))

![График улучшения точности случайного леса с добавлением большего числа деревьев](../images/ch6_06.png)

Рис. 6.6. Улучшение точности случайного леса с добавлением большего числа деревьев