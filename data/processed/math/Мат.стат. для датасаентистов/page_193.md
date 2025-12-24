---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.55
tokens: 11839
characters: 1520
timestamp: 2025-12-24T06:14:28.481129
finish_reason: stop
---

library(klaR)
naive_model <- NaiveBayes(outcome ~ purpose_ + home_ + emp_len_,
    data = na.omit(loan_data))
naive_model$table
$purpose_
    var
grouping   credit_card debt_consolidation home_improvement major_purchase
paid off    0.1857711    0.5523427    0.07153354    0.05541148
default    0.1517548    0.5777144    0.05956086    0.03708506

    var
grouping   medical other small_business
paid off   0.01236169 0.09958506    0.02299447
default    0.01434993 0.11415111    0.04538382

$home_
    var
grouping   MORTGAGE OWN RENT
paid off   0.4966286 0.08043741 0.4229340
default    0.4327455 0.08363589 0.4836186

$emp_len_
    var
grouping   > 1 Year < 1 Year
paid off   0.9690526 0.03094744
default    0.9523686 0.04763140

На выходе из модели будут условные вероятности \( P\left(X_j \mid Y = i\right) \). Модель может использоваться для предсказания исхода новой ссуды:

new_loan
    purpose_   home_   emp_len_
1 small_business MORTGAGE   > 1 Year

В данном случае модель предсказывает невозврат ссуды:

predict(naive_model, new_loan)
$class
[1] default
Levels: paid off default

$posterior
    paid off   default
[1,] 0.3717206 0.6282794

Предсказание также возвращает апостериорную оценку posterior вероятности невозврата ссуды. Наивный байесовский классификатор известен тем, что производит смещенные оценки. Однако там, где целью является ранжирование записей согласно вероятности, что \( Y = 1 \), несмещенные оценки вероятности не нужны, и наивный байесовский классификатор приводит к хорошим результатам.