---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.21
tokens: 7490
characters: 1811
timestamp: 2025-12-24T01:00:42.282749
finish_reason: stop
---

Данные находятся в формате NetCDF, который в языке Python можно прочитать с помощью библиотеки netCDF4. Установить эту библиотеку можно следующим образом:

$ conda install netcdf4

Прочитаем данные с помощью команд:

In[13]: from netCDF4 import Dataset
    data = Dataset('gistemp250.nc')

Файл содержит множество глобальных показаний температуры на различные даты, нам нужно выбрать индекс, соответствующий интересующей нас дате — 15 января 2014 года:

In[14]: from netCDF4 import date2index
    from datetime import datetime
    timeindex = date2index(datetime(2014, 1, 15),
        data.variables['time'])

Теперь можно загрузить данные по широте и долготе, а также температурным аномалиям для этого значения индекса:

In[15]: lat = data.variables['lat'][:]
    lon = data.variables['lon'][:]
    lon, lat = np.meshgrid(lon, lat)
    temp_anomaly = data.variables['tempanomaly'][timeindex]

Воспользуемся методом pcolormesh() для отрисовки цветовой сетки наших данных. Нас интересует Северная Америка, и в качестве фона мы будем использовать карту с оттененным рельефом. Обратите внимание, что для этих данных мы специально выбрали дивергентную карту цветов, с нейтральным цветом для 0 и двумя контрастными цветами для отрицательных и положительных значений (рис. 4.110).

В справочных целях мы также нарисуем светлым цветом поверх цветов береговые линии:

In[16]: fig = plt.figure(figsize=(10, 8))
    m = Basemap(projection='lcc', resolution='c',
        width=8E6, height=8E6,
        lat_0=45, lon_0=-100,)
    m.shadedrelief(scale=0.5)
    m.pcolormesh(lon, lat, temp_anomaly,
        latlon=True, cmap='RdBu_r')
    plt.clim(-8, 8)
    m.drawcoastlines(color='lightgray')
    plt.title('January 2014 Temperature Anomaly')
    plt.colorbar(label='temperature anomaly (°C)');
    # Температурные аномалии