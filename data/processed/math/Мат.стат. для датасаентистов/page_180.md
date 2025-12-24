---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.25
tokens: 11675
characters: 1361
timestamp: 2025-12-24T06:13:35.931815
finish_reason: stop
---

значение "синтетического исхода", комбинируя предсказание на основе одиночного предиктора с фактическим остатком от полного уравнения регрессии. Частный остаток для предиктора \( X_i \) — это обычный остаток плюс связанный с \( X_i \) член регрессии.

Частный остаток = Остаток + \( \hat{b}_i X_i \),

где \( \hat{b}_i \) — это оценочный коэффициент регрессии. Функция predict в R имеет возможность возвращать индивидуальные члены регрессии \( \hat{b}_i X_i \):

terms <- predict(lm_98105, type='terms')
partial_resid <- resid(lm_98105) + terms

График частных остатков отображает \( X_i \) на оси x и частные остатки — на оси y. Использование программного пакета ggplot2 упрощает наложение сглаженной из частных остатков.

df <- data.frame(SqFtTotLiving = house_98105[, 'SqFtTotLiving'],
    Terms = terms[, 'SqFtTotLiving'],
    PartialResid = partial_resid[, 'SqFtTotLiving'])
ggplot(df, aes(SqFtTotLiving, PartialResid)) +
    geom_point(shape=1) + scale_shape(solid = FALSE) +
    geom_smooth(linetype=2) +
    geom_line(aes(SqFtTotLiving, Terms))

Результирующий график показан на рис. 4.9. Частный остаток — это оценка вклада, который SqFtTotLiving вносит в продажную цену. Легко видно, что связь между

![График частных остатков для переменной SqFtTotLiving](../images/chapter4/fig4.9.png)

Рис. 4.9. График частных остатков для переменной SqFtTotLiving