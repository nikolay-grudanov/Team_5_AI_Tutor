---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.03
tokens: 7475
characters: 1892
timestamp: 2025-12-24T00:58:30.310593
finish_reason: stop
---

Команда savefig() определяет формат файла, исходя из расширения заданного имени файла. В зависимости от установленной в вашей системе прикладной части может поддерживаться множество различных форматов файлов. Вывести список поддерживаемых форматов файлов для вашей системы вы можете с помощью следующего метода объекта canvas рисунка:

In[8]: fig.canvas.get_supported_filetypes()

Out[8]: {'eps': 'Encapsulated Postscript',
    'jpeg': 'Joint Photographic Experts Group',
    'jpg': 'Joint Photographic Experts Group',
    'pdf': 'Portable Document Format',
    'pgf': 'PGF code for LaTeX',
    'png': 'Portable Network Graphics',
    'ps': 'Postscript',
    'raw': 'Raw RGBA bitmap',
    'rgba': 'Raw RGBA bitmap',
    'svg': 'Scalable Vector Graphics',
    'svgz': 'Scalable Vector Graphics',
    'tif': 'Tagged Image File Format',
    'tiff': 'Tagged Image File Format'}

Обратите внимание, что при сохранении рисунка не обязательно использовать команду plt.show() или другие команды, обсуждавшиеся ранее.

Два интерфейса по цене одного

Два интерфейса библиотеки Matplotlib (удобный MATLAB-подобный интерфейс, основанный на сохранении состояния, и обладающий большими возможностями объектно-ориентированный интерфейс) — свойство, которое потенциально может привести к путанице. Рассмотрим вкратце различия между ними.

Интерфейс в стиле MATLAB

Библиотека Matplotlib изначально была написана как альтернативный вариант (на языке Python) для пользователей пакета MATLAB, и значительная часть ее синтаксиса отражает этот факт. MATLAB-подобные инструменты содержатся в интерфейсе pyplot (plt). Например, следующий код, вероятно, выглядит довольно знакомо пользователям MATLAB (рис. 4.3):

In[9]: plt.figure()  # Создаем рисунок для графика

    # Создаем первую из двух областей графика и задаем текущую ось
    plt.subplot(2, 1, 1) # (rows, columns, panel number)
    plt.plot(x, np.sin(x))