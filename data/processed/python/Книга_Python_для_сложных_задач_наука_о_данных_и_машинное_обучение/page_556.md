---
source_image: page_556.png
page_number: 556
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.59
tokens: 7609
characters: 2102
timestamp: 2025-12-24T01:05:44.405557
finish_reason: stop
---

К сожалению, этот рисунок не дает хорошего представления о концентрации особей, поскольку точки могут перекрываться. Вряд ли вы догадаетесь по нему, что здесь показано более 1600 точек!

Воспользуемся ядерной оценкой плотности распределения, чтобы отобразить это распределение в более удобном для интерпретации виде — сглаженной индикации плотности на карте. Поскольку координатная система наложена на сферическую поверхность, а не на плоскость, воспользуемся метрикой haversine, подходящей для адекватного отображения расстояний на криволинейной поверхности.

Нам придется использовать немного шаблонного кода (один из недостатков набора инструментов Basemap), но смысл каждого блока кода должен быть вам вполне понятен (рис. 5.147):

In[15]:
# Настраиваем сетку данных для контурного графика
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()
xy = np.vstack([Y.ravel(), X.ravel()]).T xy = np.radians(xy[land_mask])

# Создаем два графика друг возле друга
fig, ax = plt.subplots(1, 2)
fig.subplots_adjust(left=0.05, right=0.95, wspace=0.05)
species_names = ['Bradypus Variegatus', 'Microryzomys Minutus']
cmaps = ['Purples', 'Reds']

for i, axi in enumerate(ax):
    axi.set_title(species_names[i])

    # Рисуем береговые линии с помощью Basemap
    m = Basemap(projection='cyl', llcrnrlat=Y.min(),
                urcrnrlat=Y.max(), llcrnrlon=X.min(),
                urcrnrlon=X.max(), resolution='c', ax=axi)
    m.drawmapboundary(fill_color='#DDEEFF')
    m.drawcoastlines()
    m.drawcountries()

    # Формируем сферическую ядерную оценку плотности распределения
    kde = KernelDensity(bandwidth=0.03, metric='haversine')
    kde.fit(np.radians(latlon[species == i]))

    # Выполняем расчеты только на поверхности Земли:
    # -9999 соответствует океану
    Z = np.full(land_mask.shape[0], -9999.0)
    Z[land_mask] = np.exp(kde.score_samples(xy))
    Z = Z.reshape(X.shape)

    # Рисуем изолинии плотности
    levels = np.linspace(0, Z.max(), 25)
    axi.contourf(X, Y, Z, levels=levels, cmap=cmaps[i])