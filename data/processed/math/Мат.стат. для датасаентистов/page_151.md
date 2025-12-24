---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 68.90
tokens: 11996
characters: 2092
timestamp: 2025-12-24T06:12:33.326173
finish_reason: stop
---

Пример: данные о жилом фонде округа Кинг

Примером использования регрессии является оценивание стоимости домов. Оценщики округа должны оценивать стоимость домов в целях обложения налогами. Потребители недвижимости и профессионалы в этой области консультируются на популярных веб-сайтах, таких как Zillow, чтобы удостовериться в справедливости цены. Ниже приведено несколько строк данных о жилом фонде округа Кинг (Сиэтл, шт. Вашингтон) из кадра данных data.frame house:

head(house[, c("AdjSalePrice", "SqFtTotLiving", "SqFtLot", "Bathrooms",
                "Bedrooms", "BldgGrade")])
Source: local data frame [6 x 6]
AdjSalePrice SqFtTotLiving SqFtLot Bathrooms Bedrooms BldgGrade
(dbl) (int) (int) (dbl) (int) (int)
1 300805 2400 9373 3.00 6 7
2 1076162 3764 20156 3.75 4 10
3 761805 2060 26036 1.75 4 8
4 442065 3200 8618 3.75 5 7
5 297065 1720 8620 1.75 4 7
6 411781 930 1012 1.50 2 8

Цель состоит в том, чтобы предсказать продажную цену на основе остальных переменных. Переменная lm обрабатывает случай множественной регрессии просто путем включения большего количества членов на правой стороне уравнения; аргумент na.action=na.omit заставляет модель отбрасывать записи, в которых имеются отсутствующие значения:

house_lm <- lm(AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms +
                Bedrooms + BldgGrade,
                data=house, na.action=na.omit)

Распечатка объекта house_lm произведет на выходе следующие данные:

house_lm

Call:
lm(formula = AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms +
    Bedrooms + BldgGrade, data = house, na.action = na.omit)

Coefficients:
(Intercept)   SqFtTotLiving   SqFtLot   Bathrooms
-5.219e+05    2.288e+02      -6.051e-02  -1.944e+04
Bedrooms      BldgGrade
-4.778e+04    1.061e+05

Интерпретация коэффициентов такая же, как и в простой линейной регрессии: предсказанное значение \( \hat{Y} \) изменяется коэффициентом \( b_j \) для каждого единичного изменения в \( X_j \) с учетом всех остальных переменных, \( X_k \) для \( k \neq j \) остается прежним. Например, добавление дополнительного квадратного фута общей площа-