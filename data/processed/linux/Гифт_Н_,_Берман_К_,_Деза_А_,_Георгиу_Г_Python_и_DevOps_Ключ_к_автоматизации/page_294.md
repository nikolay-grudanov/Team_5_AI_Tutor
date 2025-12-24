---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.38
tokens: 7591
characters: 1765
timestamp: 2025-12-24T03:08:42.715547
finish_reason: stop
---

как на макро-, так и на микроуровне. В следующем примере1 метод make_blobs создает набор данных, включающий 100 тыс. записей и десять признаков. При этом измеряется время выполнения каждого алгоритма k-средних, а также общее время:

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import time

def do_kmeans():
    """Кластеризация сгенерированных данных методом k-средних"""

    X,_ = make_blobs(n_samples=100000, centers=3, n_features=10,
                     random_state=0)
    kmeans = KMeans(n_clusters=3)
    t0 = time.time()
    kmeans.fit(X)
    print(f"KMeans cluster fit in {time.time()-t0}")

def main():
    """Выполняем все расчеты"""

    count = 10
    t0 = time.time()
    for _ in range(count):
        do_kmeans()
    print(f"Performed {count} KMeans in total time: {time.time()-t0}")
if __name__ == "__main__":
    main()

Время выполнения алгоритма метода k-средних демонстрирует, что это ресурсоемкая операция, — десять итераций делятся 3,5 секунды:

(.python-devops) ➔ python kmeans_sequential.py
KMeans cluster fit in 0.29854321479797363
KMeans cluster fit in 0.2869119644165039
KMeans cluster fit in 0.2811620235443115
KMeans cluster fit in 0.28687286376953125
KMeans cluster fit in 0.2845759391784668
KMeans cluster fit in 0.2866239547729492
KMeans cluster fit in 0.2843656539916992
KMeans cluster fit in 0.2885470390319824
KMeans cluster fit in 0.2878849506378174
KMeans cluster fit in 0.28443288803100586
Performed 10 KMeans in total time: 3.510640859603882

1 В последних версиях библиотеки sklearn нет модуля sklearn.datasets.samples_generator, его заменил sklearn.datasets, так что первая строка с импортом должна выглядеть вот так: from sklearn.datasets import make_blobs. — Примеч. пер.