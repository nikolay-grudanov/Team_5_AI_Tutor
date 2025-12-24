---
source_image: page_440.png
page_number: 440
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.00
tokens: 7486
characters: 2152
timestamp: 2025-12-24T01:02:36.480835
finish_reason: stop
---

Для простоты выберем лишь несколько из этих категорий, после чего скачаем обучающую и контрольную последовательности:

In[8]:
categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

Вот типичный образец записи из этого набора данных:

In[9]: print(train.data[5])

From: dmcgee@uluhe.soest.hawaii.edu (Don McGee)
Subject: Federal Hearing
Originator: dmcgee@uluhe
Organization: School of Ocean and Earth Science and Technology
Distribution: usa
Lines: 10

Fact or rumor....? Madalyn Murray O'Hare an atheist who eliminated the use of the bible reading and prayer in public schools 15 years ago is now going to appear before the FCC with a petition to stop the reading of the Gospel on the airways of America. And she is also campaigning to remove Christmas programs, songs, etc from the public schools. If it is true then mail to Federal Communications Commission 1919 H Street Washington DC 20054 expressing your opposition to her request. Reference Petition number 2493.

Чтобы использовать эти данные для машинного обучения, необходимо преобразовать содержимое каждой строки в числовой вектор. Для этого воспользуемся векторизатором TF–IDF (который обсуждали в разделе «Проектирование признаков» текущей главы) и создадим конвейер, присоединяющий его последовательно к полиномиальному наивному байесовскому классификатору:

In[10]: from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import make_pipeline

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

С помощью этого конвейера мы можем применить модель к обучающей последовательности и предсказать метки для контрольных данных:

In[11]: model.fit(train.data, train.target)
    labels = model.predict(test.data)

Теперь, предсказав метки для контрольных данных, мы изучим их, чтобы выяснить эффективность работы оценивателя. Например, вот матрица различий между настоящими и предсказанными метками для контрольных данных (рис. 5.41):