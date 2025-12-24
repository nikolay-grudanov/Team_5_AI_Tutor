---
source_image: page_354.png
page_number: 354
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.20
tokens: 7476
characters: 1721
timestamp: 2025-12-24T01:00:37.888269
finish_reason: stop
---

Пример: города Калифорнии

В разделе «Пользовательские настройки легенд на графиках» данной главы было продемонстрировано использование размера и цвета точек на диаграмме рассеяния при передаче информации о расположении, размере и населении городов штата Калифорния. Здесь же мы воссоздадим этот график, но с использованием Basemap для включения данных в соответствующий картографический контекст.

Начнем, как и раньше, с загрузки данных:

In[10]: import pandas as pd
    cities = pd.read_csv('data/california_cities.csv')

    # Извлекаем интересующие нас данные
    lat = cities['latd'].values
    lon = cities['longd'].values
    population = cities['population_total'].values
    area = cities['area_total_km2'].values

Настраиваем проекцию карты, наносим данные, после чего создаем шкалу цветов и легенду (рис. 4.109):

In[11]: # 1. Рисуем фон карты
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution='h',
        lat_0=37.5, lon_0=-119,
        width=1E6, height=1.2E6)
    m.shadedrelief()
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')

    # 2. Наносим данные по городам, отражая население разными цветами,
    # а площадь — разными размерами точек
    m.scatter(lon, lat, latlon=True,
        c=np.log10(population), s=area,
        cmap='Reds', alpha=0.5)

    # 3. Создаем шкалу цветов и легенду
    plt.colorbar(label=r'$\log_{10}({\rm population})$')
    plt.clim(3, 7)

    # Делаем легенду с фиктивными точками
    for a in [100, 300, 500]:
        plt.scatter([], [], c='k', alpha=0.5, s=a,
            label=str(a) + ' km$^2$')
    plt.legend(scatterpoints=1, frameon=False,
        labelspaceing=1, loc='lower left');