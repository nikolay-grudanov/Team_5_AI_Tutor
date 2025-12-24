---
source_image: page_255.png
page_number: 255
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.71
tokens: 11659
characters: 1577
timestamp: 2025-12-24T06:17:26.772612
finish_reason: stop
---

сжатия eta полезен для предотвращения переподгонки путем сокращения изменений в весах (меньшее изменение в весах означает, что алгоритм с меньшей вероятностью будет переподогнан к тренировочному набору). Представленный далее фрагмент кода применяет xgboost к данным о ссудах всего с двумя предикторными переменными:

library(xgboost)
predictors <- data.matrix(loan3000[, c('borrower_score',
                                        'payment_inc_ratio')])
label <- as.numeric(loan3000[, 'outcome'])-1
xgb <- xgboost(data=predictors, label=label,
               objective = "binary:logistic",
               params=list(subsample=.63, eta=0.1), nrounds=100)

Отметим, что xgboost не поддерживает формульный синтаксис, поэтому предикторы нужно конвертировать в матрицу данных data.matrix, а отклик — в двоичные переменные в формате 0/1. Аргумент objective сообщает xgboost тип решаемой задачи; опираясь на эти данные xgboost выберет для оптимизации метрический показатель.

Предсказанные значения можно получить из функции predict, и поскольку переменных всего две, их можно вывести на графике против предикторов:

pred <- predict(xgb, newdata=predictors)
xgb_df <- cbind(loan3000, pred_default=pred>.5, prob_default=pred)
ggplot(data=xgb_df, aes(x=borrower_score, y=payment_inc_ratio,
                        color=pred_default, shape=pred_default)) +
    geom_point(alpha=.6, size=2)

![Предсказанные исходы из XGBoost применительно к данным о невозвратных ссудах](../images/chapter_6_9.png)

Рис. 6.9. Предсказанные исходы из XGBoost применительно к данным о невозвратных ссудах