---
source_image: page_449.png
page_number: 449
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.10
tokens: 7280
characters: 1230
timestamp: 2025-12-24T01:02:44.255246
finish_reason: stop
---

arg = (x - y) / width
return np.exp(-0.5 * np.sum(arg ** 2, axis))

def fit(self, X, y=None):
    # Создаем N центров, распределенных по всему диапазону данных
    self.centers_ = np.linspace(X.min(), X.max(), self.N)
    self.width_ = self.width_factor *
    (self.centers_[1] - self.centers_[0])
    return self

def transform(self, X):
    return self._gauss_basis(X[:, :, np.newaxis], self.centers_,
        self.width_, axis=1)

gauss_model = make_pipeline(GaussianFeatures(20),
    LinearRegression())

gauss_model.fit(x[:, np.newaxis], y)
yfit = gauss_model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.xlim(0, 10);

Мы привели этот пример лишь для того, чтобы подчеркнуть, что в полиномиальных базисных функциях нет никакого колдовства. Если у вас есть какие-то дополнительные сведения о процессе генерации ваших данных, исходя из которых у вас есть основания полагать, что наиболее подходящим будет тот или иной базис, — тоже можете его использовать.

![Аппроксимация Гауссовыми базисными функциями, вычисленными с помощью пользовательского преобразователя](../images/05_46.png)

Рис. 5.46. Аппроксимация Гауссовыми базисными функциями, вычисленными с помощью пользовательского преобразователя