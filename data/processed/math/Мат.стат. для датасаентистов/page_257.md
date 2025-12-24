---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.08
tokens: 11926
characters: 2357
timestamp: 2025-12-24T06:17:49.051216
finish_reason: stop
---

Другой подход заключается в регуляризации, методе, который модифицирует функцию стоимости, чтобы оштрафовать сложность модели. Деревья решений подгоняются путем минимизации критериев стоимости, в частности, оценки разнородности Джини (см. разд. "Измерение однородности или разнородности" ранее в этой главе). В xgboost можно модифицировать функцию стоимости путем добавления члена, который измеряет сложность модели.

В xgboost имеется два параметра для регуляризации модели: alpha и lambda, которые представляют собой соответственно манхэттенское расстояние и квадратическое евклидово расстояние (см. разд. "Метрические показатели расстояния" ранее в этой главе). Увеличение этих параметров оштрафует более сложные модели и уменьшит размер подгоняемых деревьев. Например, посмотрим, что произойдет, если установить lambda в 1000:

> xgb_penalty <- xgboost(data=predictors[-test_idx,],
    label=label[-test_idx],
    params=list(eta=.1, subsample=.63, lambda=1000),
    objective = "binary:logistic", nrounds=250)
> pred_penalty <- predict(xgb_penalty, predictors[test_idx,])
> error_penalty <- abs(label[test_idx] - pred_penalty) > 0.5
> xgb_penalty$evaluation_log[250,]
iter train_error
1: 250 0.332405
> mean(error_penalty)
[1] 0.3483

Теперь ошибка тренировки только немного ниже ошибки на проверочном наборе.

Метод predict предлагает удобный аргумент ntreeelimin, который заставляет использовать в предсказании только первые i деревьев. Это позволяет нам непосредственно сопоставлять внутривыборочный коэффициент ошибок с вне выборочным по мере включения большего числа моделей:

> error_default <- rep(0, 250)
> error_penalty <- rep(0, 250)
> for(i in 1:250){
  pred_def <- predict(xgb_default, predictors[test_idx,], ntreeelimin=i)
  error_default[i] <- mean(abs(label[test_idx] - pred_def) >= 0.5)
  pred_pen <- predict(xgb_penalty, predictors[test_idx,], ntreeelimin = i)
  error_penalty[i] <- mean(abs(label[test_idx] - pred_pen) >= 0.5)
}

В данных на выходе из модели содержится ошибка для тренировочного набора в компоненте xgb_default$evaluation_log. Объединив ее с вне выборочными ошибками, мы можем отобразить на графике ошибки против числа итераций:

> errors <- rbind(xgb_default$evaluation_log,
    xgb_penalty$evaluation_log,
    data.frame(iter=1:250, train_error=error_default),
    data.frame(iter=1:250, train_error=error_penalty))