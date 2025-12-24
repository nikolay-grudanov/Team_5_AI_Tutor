---
source_image: page_452.png
page_number: 452
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.85
tokens: 7768
characters: 2373
timestamp: 2025-12-24T02:53:01.752797
finish_reason: stop
---

Получившийся объект DataFrame слишком велик, для того чтобы приводить его полностью. Ниже приведена только группа питательных элементов 'Amino Acids' (аминокислоты):

In [198]: max_foods.loc["Amino Acids"]["food"]
Out[198]:
nutrient
Alanine Gelatins, dry powder, unsweetened
Arginine Seeds, sesame flour, low-fat
Aspartic acid Soy protein isolate
Cystine Seeds, cottonseed flour, low fat (glandless)
Glutamic acid Soy protein isolate
Glycine Gelatins, dry powder, unsweetened
Histidine Whale, beluga, meat, dried (Alaska Native)
Hydroxyproline KENTUCKY FRIED CHICKEN, Fried Chicken, ORIGINAL RE
Isoleucine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Leucine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Lysine Seal, bearded (Oogruk), meat, dried (Alaska Native
Methionine Fish, cod, Atlantic, dried and salted
Phenylalanine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Proline Gelatins, dry powder, unsweetened
Serine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Threonine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Tryptophan Sea lion, Steller, meat with fat (Alaska Native)
Tyrosine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Valine Soy protein isolate, PROTEIN TECHNOLOGIES INTERNAT
Name: food, dtype: object

13.5. БАЗА ДАННЫХ ФЕДЕРАЛЬНОЙ ИЗБИРАТЕЛЬНОЙ КОМИССИИ

Федеральная избирательная комиссия США публикует данные о пожертвованиях участникам политических кампаний. Указывается имя жертвователя, род занятий, место работы и сумма пожертвования. Интерес представляет набор данных, относящийся к президентским выборам 2012 года. Версия этого набора, загруженная мной в июне 2012 года, представляет собой CSV-файл P00000001-ALL.csv размером 150 МБ, который можно скачать с помощью функции pandas.read_csv:

In [199]: fec = pd.read_csv("datasets/fec/P00000001-ALL.csv", low_memory=False)

In [200]: fec.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001731 entries, 0 to 1001730
Data columns (total 16 columns):
# Column    Non-Null Count Dtype
--- -------- -------------- -----
0 cmte_id   1001731 non-null object
1 cand_id   1001731 non-null object
2 cand_nm   1001731 non-null object
3 contbr_nm 1001731 non-null object
4 contbr_city 1001712 non-null object
5 contbr_st 1001727 non-null object
6 contbr_zip 1001620 non-null object
7 contbr_employer 988002 non-null object
8 contbr_occupation 993301 non-null object