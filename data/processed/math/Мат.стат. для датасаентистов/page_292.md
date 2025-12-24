---
source_image: page_292.png
page_number: 292
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.07
tokens: 11694
characters: 1306
timestamp: 2025-12-24T06:19:06.528275
finish_reason: stop
---

d = daisy(df, metric='gower')
hcl <- hclust(d)
dnd <- as.dendrogram(hcl)
plot(dnd, leaflab='none')

Результирующая дендограмма показана на рис. 7.13. Индивидуальные записи неразличимы на оси x, но мы можем обследовать записи в одном из поддеревьев (слева, используя "отсечение" 0,5) при помощи представленного далее фрагмента кода:

> df[labels(dnd_cut$lower[[1]]),]
# A table: 9 × 4
   dti payment_inc_ratio home purpose
<dbl>           <dbl> <fctr> <fctr>
1 24.57         0.83550 RENT other
2 34.95         5.02763 RENT other
3 1.51          2.97784 RENT other
4 8.73          14.42070 RENT other
5 12.05         9.96750 RENT other
6 10.15         11.43180 RENT other
7 19.61         14.04420 RENT other
8 20.92         6.90123 RENT other
9 22.49         9.36000 RENT other

Это поддерево полностью состоит из арендаторов с целью предоставления ссуды, помеченной как "другая" (other). Хотя нельзя сказать, что для всех поддеревьев есть строгое разделение, график иллюстрирует, что категориальные переменные имеют тенденцию группироваться в кластерах.

![Дендрограмма hclust применительно к выборке данных о невозвратных ссудах с типами смешанных переменных](../images/chapter7/fig7_13.png)

Рис. 7.13. Дендрограмма hclust применительно к выборке данных о невозвратных ссудах с типами смешанных переменных