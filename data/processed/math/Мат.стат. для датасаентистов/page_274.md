---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.95
tokens: 11489
characters: 948
timestamp: 2025-12-24T06:18:14.555914
finish_reason: stop
---

centers <- as.data.frame(t(centers))
names(centers) <- paste("Cluster", 1:5)
centers$Symbol <- row.names(centers)
centers <- gather(centers, "Cluster", "Mean", -Symbol)
centers$Color = centers$Mean > 0
ggplot(centers, aes(x=Symbol, y=Mean, fill=Color)) +
    geom_bar(stat='identity', position = "identity", width=.75) +
    facet_grid(Cluster ~ ., scales='free_y')

Результирующий график показан на рис. 7.5 и демонстрирует природу каждого кластера. Например, кластеры 1 и 2 соответствуют дням, в которые рынок падает и растет. Кластеры 3 и 5 характеризуются соответственно днями растущего рынка акций потребительского рынка и днями падающего рынка энергетических акций. Наконец, кластер 4 фиксирует дни, в которые энергетические акции росли, а акции потребительского рынка падали.

![Средние значения переменных в каждом кластере ("центроиды")](../images/chapter7/fig7_5.png)

Рис. 7.5. Средние значения переменных в каждом кластере ("центроиды")