---
source_image: page_208.png
page_number: 208
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.98
tokens: 11689
characters: 1520
timestamp: 2025-12-24T06:15:06.132914
finish_reason: stop
---

можно использовать шаговую регрессию, выполнить подгонку членов уравнения, характеризующих взаимодействие, или включить сплайновые члены. Те же вопросы касаются применения к логистической регрессии искажающих и коррелированных переменных (см. разд. "Интерпретация уравнения регрессии" главы 4). Подгонку обобщенных аддитивных моделей можно выполнить (см. разд. "Обобщенные аддитивные модели" главы 4) с помощью пакета mgcv:

logistic_gam <- gam(outcome ~ s(payment_inc_ratio) + purpose_ +
    home_ + emp_len_ + s(borrower_score),
    data=loan_data, family='binomial')

Одна из областей, где логистическая регрессия иная, касается анализа остатков. Как и в регрессии (рис. 4.9), вычисление частных остатков выполняется прямолинейно:

terms <- predict(logistic_gam, type='terms')
partial_resid <- resid(logistic_model) + terms
df <- data.frame(payment_inc_ratio = loan_data[, 'payment_inc_ratio'],
    terms = terms[, 's(payment_inc_ratio)'],
    partial_resid = partial_resid[, 's(payment_inc_ratio)'])
ggplot(df, aes(x=payment_inc_ratio, y=partial_resid, solid = FALSE)) +
    geom_point(shape=46, alpha=.4) +
    geom_line(aes(x=payment_inc_ratio, y=terms),
        color='red', alpha=.5, size=1.5) +
    labs(y='Partial Residual')

Результирующий график отображен на рис. 5.4. Оценочная подгонка, показанная линией, проходит между двумя наборами точечных облаков. Верхнее облако соот-

![Частные остатки от логистической регрессии](../images/chapter5/fig5_4.png)

Рис. 5.4. Частные остатки от логистической регрессии