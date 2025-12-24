---
source_image: page_207.png
page_number: 207
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 80.40
tokens: 12190
characters: 2302
timestamp: 2025-12-24T06:15:32.168474
finish_reason: stop
---

рые позволяют выполнить диагностику модели и ее улучшить. Вместе с оценочными коэффициентами R сообщает о стандартной ошибке коэффициентов (SE), z-оценке и p-значении:

summary(logistic_model)

Call:
glm(formula = outcome ~ payment_inc_ratio + purpose_ + home_ +
    emp_len_ + borrower_score, family = "binomial", data = loan_data)

Deviance Residuals:

    Min        1Q    Median        3Q        Max
-2.71430   -1.06806   -0.04482    1.07446    2.11672

Coefficients:
                Estimate  Std. Error  z value Pr(>|z|)
(Intercept)      1.269822     0.051929   24.453 < 2e-16 ***
payment_inc_ratio 0.082443     0.002485   33.177 < 2e-16 ***
purpose_debt_consolidation 0.252164     0.027409    9.200 < 2e-16 ***
purpose_home_improvement 0.343674     0.045951    7.479 7.48e-14 ***
purpose_major_purchase 0.243728     0.053314    4.572 4.84e-06 ***
purpose_medical      0.675362     0.089803    7.520 5.46e-14 ***
purpose_other         0.592678     0.039109   15.154 < 2e-16 ***
purpose_small_business 1.212264     0.062457   19.410 < 2e-16 ***
home_OWN             0.031320     0.037479    0.836 0.403
home_RENT            0.168670     0.021041    8.016 1.09e-15 ***
emp_len_ < 1 Year    0.444892     0.053342    8.340 < 2e-16 ***
borrower_score      -4.638902     0.082433  -56.275 < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
(Dispersion parameter for binomial family taken to be 1)
    Null deviance: 64147 on 46271 degrees of freedom
Residual deviance: 58531 on 46260 degrees of freedom
AIC: 58555

Number of Fisher Scoring iterations: 4

Интерпретация p-значения сопровождается теми же оговорками, что и в регрессии, и должна рассматриваться больше как относительный индикатор важности переменной (см. разд. "Диагностика модели" главы 4), чем как формальная мера статистической значимости. С моделью логистической регрессии, которая имеет бинарный отклик, не связан показатель RMSE либо \( R^2 \). Вместо этого модель логистической регрессии обычно оценивается при помощи более общих метрических показателей, предназначенных для классификации (см. разд. "Оценивание модели классификации" далее в этой главе).

Многие другие понятия, относящиеся к линейной регрессии, переносятся на параметрическую настройку логистической регрессии (и других ОЛМ). Например,