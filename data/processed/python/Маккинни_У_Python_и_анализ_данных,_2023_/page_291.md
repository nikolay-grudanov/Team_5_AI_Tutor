---
source_image: page_291.png
page_number: 291
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.58
tokens: 7519
characters: 1652
timestamp: 2025-12-24T02:47:57.894331
finish_reason: stop
---

<table>
  <tr>
    <th>Аргумент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>sharey</td>
    <td>Все подграфики должны иметь одинаковые риски на оси Y (настройка ylim отражается на всех подграфиках)</td>
  </tr>
  <tr>
    <td>subplot_kw</td>
    <td>Словарь ключевых слов, передаваемый функции add_subplot при создании каждого подграфика</td>
  </tr>
  <tr>
    <td>**fig_kw</td>
    <td>Дополнительные ключевые слова используются при создании рисунка, например plt.subplots(2, 2, figsize=(8, 6))</td>
  </tr>
</table>

Задание свободного места вокруг подграфиков

По умолчанию matplotlib оставляет пустое место вокруг каждого подграфика и между подграфиками. Размер этого места определяется относительно высоты и ширины графика, так что если изменить размер графика программно или вручную (изменив размер окна), то график автоматически перестроится. Величину промежутка легко изменить с помощью метода subplots_adjust объекта Figure:

subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

Параметры wspace и hspace определяют, какой процент от ширины (соответственно высоты) рисунка должен составлять промежуток между подграфиками. В примере ниже я задал нулевой промежуток (рис. 9.5):

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.standard_normal(500), bins=50,
                        color="black", alpha=0.5)
fig.subplots_adjust(wspace=0, hspace=0)

![Визуализация данных, в которой подграфики не разделены промежутками](../images/9_5.png)

Рис. 9.5. Визуализация данных, в которой подграфики не разделены промежутками