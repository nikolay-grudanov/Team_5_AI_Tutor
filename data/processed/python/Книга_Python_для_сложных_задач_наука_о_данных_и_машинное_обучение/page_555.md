---
source_image: page_555.png
page_number: 555
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.12
tokens: 7352
characters: 1519
timestamp: 2025-12-24T01:05:30.835799
finish_reason: stop
---

data = fetch_species_distributions()

# Получаем матрицы/массивы идентификаторов и местоположений животных
latlon = np.vstack([data.train['dd lat'],
                    data.train['dd long']]).T
species = np.array([d.decode('ascii').startswith('micro')
                    for d in data.train['species']], dtype='int')

После загрузки данных можно воспользоваться набором инструментов Basemap (упоминавшимся ранее в разделе «Отображение географических данных с помощью Basemap» главы 4) для отображения мест, где наблюдались особи этих двух видов на карте Южной Америки (рис. 5.146):

In[14]: from mpl_toolkits.basemap import Basemap
        from sklearn.datasets.species_distributions import construct_grids

        xgrid, ygrid = construct_grids(data)

        # Рисуем береговые линии с помощью Basemap
        m = Basemap(projection='cyl', resolution='c',
                    llcrnrlat=ygrid.min(), urcrnrlat=ygrid.max(),
                    llcrnrlon=xgrid.min(), urcrnrlon=xgrid.max())
        m.drawmapboundary(fill_color='#DDEEFF')
        m.fillcontinents(color='#FFEEDD')
        m.drawcoastlines(color='gray', zorder=2)
        m.drawcountries(color='gray', zorder=2)

        # Отображаем места, где наблюдались особи
        m.scatter(latlon[:, 1], latlon[:, 0], zorder=3,
                  c=species, cmap='rainbow', latlon=True);

![Места, где наблюдались особи, в обучающей последовательности](../images/chapter_5/fig_5_146.png)

Рис. 5.146. Места, где наблюдались особи, в обучающей последовательности