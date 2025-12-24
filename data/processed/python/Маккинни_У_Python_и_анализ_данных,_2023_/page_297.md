---
source_image: page_297.png
page_number: 297
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.20
tokens: 7441
characters: 1239
timestamp: 2025-12-24T02:48:09.309417
finish_reason: stop
---

с сайта Yahoo! Finance) и аннотируем его некоторыми важными датами, относящимися к финансовому кризису 2008–2009 годов. Воспроизвести этот код можно, введя его в одну ячейку Jupyter-блокнота. Результат изображен на рис. 9.11.

from datetime import datetime

fig, ax = plt.subplots()

data = pd.read_csv("examples/spx.csv", index_col=0, parse_dates=True)
spx = data["SPX"]

spx.plot(ax=ax, color="black")

crisis_data = [
    (datetime(2007, 10, 11), "Peak of bull market"),
    (datetime(2008, 3, 12), "Bear Stearns Fails"),
    (datetime(2008, 9, 15), "Lehman Bankruptcy")
]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor="black", headwidth=4, width=2,
                                headlength=4),
                horizontalalignment="left", verticalalignment="top")

# Приблизить годы 2007-2010
ax.set_xlim(["1/1/2007", "1/1/2011"])
ax.set_ylim([600, 1800])

ax.set_title("Important dates in the 2008-2009 financial crisis")

![Важные даты, относящиеся к финансовому кризису 2008–2009 годов](https://i.imgur.com/3Q5z5QG.png)

Рис. 9.11. Важные даты, относящиеся к финансовому кризису 2008–2009 годов