---
source_image: page_561.png
page_number: 561
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.67
tokens: 7338
characters: 1260
timestamp: 2025-12-24T01:05:37.090391
finish_reason: stop
---

bandwidths = 10 ** np.linspace(0, 2, 100)
grid = GridSearchCV(KDEClassifier(), {'bandwidth': bandwidths})
grid.fit(digits.data, digits.target)
scores = [val.mean_validation_score for val in grid.grid_scores_]

Далее можно построить график полученной при перекрестной проверке оценки эффективности модели как функции от ширины ядра (рис. 5.148):

In[18]: plt.semilogx(bandwidths, scores)
    plt.xlabel('bandwidth')        # Ширина ядра
    plt.ylabel('accuracy')         # Точность
    plt.title('KDE Model Performance') # Эффективность модели KDE

    print(grid.best_params_)
    print('accuracy =', grid.best_score_)

{'bandwidth': 7.0548023107186433}
accuracy = 0.966611018364

Как видим, этот «не столь наивный» байесовский классификатор достигает точности перекрестной проверки в более чем 96%. И это по сравнению с примерно 80% у «наивного» байесовского классификатора:

In[19]: from sklearn.naive_bayes import GaussianNB
    from sklearn.cross_validation import cross_val_score
    cross_val_score(GaussianNB(), digits.data, digits.target).mean()

Out[19]: 0.81860038035501381

![Кривая проверки для основанного на KDE байесовского классификатора](../images/fig_5_148.png)

Рис. 5.148. Кривая проверки для основанного на KDE байесовского классификатора