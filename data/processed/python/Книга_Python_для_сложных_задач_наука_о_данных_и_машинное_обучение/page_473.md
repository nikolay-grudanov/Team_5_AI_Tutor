---
source_image: page_473.png
page_number: 473
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.83
tokens: 8050
characters: 3010
timestamp: 2025-12-24T01:03:59.672841
finish_reason: stop
---

In[24]: fig, ax = plt.subplots(4, 6)
    for i, axi in enumerate(ax.flat):
        axi.imshow(Xtest[i].reshape(62, 47), cmap='bone')
        axi.set(xticks=[], yticks=[])
        axi.set_ylabel(faces.target_names[yfit[i]].split()[-1],
            color='black' if yfit[i] == ytest[i] else 'red')
    fig.suptitle('Predicted Names; Incorrect Labels in Red', size=14);

В этой небольшой выборке наш оптимальный оцениватель ошибся только для одного лица (лицо Дж. Буша в нижнем ряду было ошибочно помечено как лицо Блэра). Чтобы лучше прочувствовать эффективность работы нашего оценивателя, воспользуемся отчетом о классификации, в котором приведена статистика восстановления значений по каждой метке:

In[25]: from sklearn.metrics import classification_report
    print(classification_report(ytest, yfit,
        target_names=faces.target_names))

<table>
  <tr>
    <th></th>
    <th>precision</th>
    <th>recall</th>
    <th>f1-score</th>
    <th>support</th>
  </tr>
  <tr>
    <td>Ariel Sharon</td>
    <td>0.65</td>
    <td>0.73</td>
    <td>0.69</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Colin Powell</td>
    <td>0.81</td>
    <td>0.87</td>
    <td>0.84</td>
    <td>68</td>
  </tr>
  <tr>
    <td>Donald Rumsfeld</td>
    <td>0.75</td>
    <td>0.87</td>
    <td>0.81</td>
    <td>31</td>
  </tr>
  <tr>
    <td>George W Bush</td>
    <td>0.93</td>
    <td>0.83</td>
    <td>0.88</td>
    <td>126</td>
  </tr>
  <tr>
    <td>Gerhard Schroeder</td>
    <td>0.86</td>
    <td>0.78</td>
    <td>0.82</td>
    <td>23</td>
  </tr>
  <tr>
    <td>Hugo Chavez</td>
    <td>0.93</td>
    <td>0.70</td>
    <td>0.80</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Junichiro Koizumi</td>
    <td>0.80</td>
    <td>1.00</td>
    <td>0.89</td>
    <td>12</td>
  </tr>
  <tr>
    <td>Tony Blair</td>
    <td>0.83</td>
    <td>0.93</td>
    <td>0.88</td>
    <td>42</td>
  </tr>
  <tr>
    <td>avg / total</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>337</td>
  </tr>
</table>

Можем также вывести на экран матрицу различий между этими классами (рис. 5.66):

In[26]: from sklearn.metrics import confusion_matrix
    mat = confusion_matrix(ytest, yfit)
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
        xticklabels=faces.target_names,
        yticklabels=faces.target_names)
    plt.xlabel('true label')
    plt.ylabel('predicted label');

Эта информация позволяет нам понять, какие метки, вероятно, оцениватель определит неверно.

В реальных задачах распознавания лиц, в которых фотографии не кадрированы предварительно в аккуратные сетки, единственное отличие в схеме классификации лиц будет состоять в выборе признаков. Необходимо будет использовать более сложный алгоритм для поиска лиц и извлекать не зависящие от пикселизации признаки. Для подобных приложений удобно применять библиотеку OpenCV (http://opencv.org/), которая, помимо прочего, включает заранее обученные реализации современных инструментов выделения признаков для изображений вообще и лиц в частности.