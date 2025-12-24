---
source_image: page_215.png
page_number: 215
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.63
tokens: 11576
characters: 1220
timestamp: 2025-12-24T06:15:14.487705
finish_reason: stop
---

Вычисление ROC-кривой в R выполняется достаточно прямолинейно. Следующий ниже фрагмент кода вычисляет ROC для данных о ссудах:

idx <- order(-pred)
recall <- cumsum(true_y[idx]==1)/sum(true_y==1)
specificity <- (sum(true_y==0) - cumsum(true_y[idx]==0))/sum(true_y==0)
roc_df <- data.frame(recall = recall, specificity = specificity)
ggplot(roc_df, aes(x=specificity, y=recall)) +
  geom_line(color='blue') +
  scale_x_reverse(expand=c(0, 0)) +
  scale_y_continuous(expand=c(0, 0)) +
  geom_line(data=data.frame(x=(0:100)/100), aes(x=x, y=1-x),
            linetype='dotted', color='red')

Результат показан на рис. 5.6. Пунктирная диагональная линия соответствует классификатору, который не лучше случайной возможности. Чрезвычайно эффективный классификатор (или в медицинских ситуациях чрезвычайно эффективный диагностический тест) будет иметь ROC-кривую, которая прижимается к левому верхнему углу — она правильно идентифицирует много единиц без неправильной классификации многих нулей, как единицы. Если для этой модели нам нужен классификатор со специфичностью по крайней мере 50%, то полнота составит порядка 75%.

![ROC-кривая для данных о ссудах](../images/roc_curve.png)

Рис. 5.6. ROC-кривая для данных о ссудах