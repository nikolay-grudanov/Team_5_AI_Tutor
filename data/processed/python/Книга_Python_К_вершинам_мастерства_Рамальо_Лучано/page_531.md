---
source_image: page_531.png
page_number: 531
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.55
tokens: 11968
characters: 2403
timestamp: 2025-12-24T01:59:39.965032
finish_reason: stop
---

Пример: три способа загрузки из веба

последовательно: она запрашивает следующее изображение только после того, как предыдущее загружено и записано на диск. Два других скрипта производят загрузку параллельно: они запрашивают все изображения практически одновременно, а сохраняют по мере поступления. Скрипт flags_threadpool.py пользуется пакетом concurrent.futures, а flags_asyncio.py — пакетом asyncio.

В примере 17.1 показаны результаты выполнения всех трех скриптов, по три раза каждый. Я также разместил на YouTube видео продолжительностью 73 с (https://www.youtube.com/watch?v=A9e9Cy1UkME), чтобы было видно, как по мере сохранения флагов в окне OS X Finder становятся видны их изображения. Скрипты загружают изображения с сайта flupy.org, который развернут за системой доставки контента (CDN), так что при первом прогоне они работают несколько медленнее. Показанные ниже результаты получены после прогрева кэша CDN.

Пример 17.1. Результаты трех типичных прогонов скриптов flags.py, flags_threadpool.py и flags_asyncio.py

$ python3 flags.py
BD BR CD CN DE EG ET FR ID IN IR JP MX NG PH PK RU TR US VN
20 flags downloaded in 7.26s
$ python3 flags.py
BD BR CD CN DE EG ET FR ID IN IR JP MX NG PH PK RU TR US VN
20 flags downloaded in 7.20s
$ python3 flags.py
BD BR CD CN DE EG ET FR ID IN IR JP MX NG PH PK RU TR US VN
20 flags downloaded in 7.09s
$ python3 flags_threadpool.py
DE BD CN JP ID EG NG BR RU CD IR MX US PH FR PK VN IN ET TR
20 flags downloaded in 1.37s
$ python3 flags_threadpool.py
EG BR FR IN BD JP DE RU PK PH CD MX ID US NG TR CN VN ET IR
20 flags downloaded in 1.60s
$ python3 flags_threadpool.py
BD DE EG CN ID RU IN VN ET MX FR CD NG US JP TR PK BR IR PH
20 flags downloaded in 1.22s
$ python3 flags_asyncio.py
BD BR IN ID TR DE CN US IR PK PH FR RU NG VN ET MX EG JP CD
20 flags downloaded in 1.36s
$ python3 flags_asyncio.py
RU CN BR IN FR BD TR EG VN IR PH CD ET ID NG DE JP PK MX US
20 flags downloaded in 1.27s
$ python3 flags_asyncio.py
RU IN ID DE BR VN PK MX US IR ET EG NG BD FR CN JP PH CD TR
20 flags downloaded in 1.42s

1 Печать результатов каждого прогона начинается с вывода кодов стран в порядке загрузки их флагов и заканчивается сообщением о том, сколько прошло времени.
2 Скрипту flags.py требуется в среднем 7,18 с для загрузки 20 изображений.
3 Скрипту flags_threadpool.py в среднем требуется 1,40 с.
4 Скрипту flags_asyncio.py в среднем требуется 1,35 с.