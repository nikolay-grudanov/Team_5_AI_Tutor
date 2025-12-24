---
source_image: page_424.png
page_number: 424
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.39
tokens: 7651
characters: 1674
timestamp: 2025-12-24T02:51:59.534860
finish_reason: stop
---

13.1. Набор данных Bitly с сайта 1.usa.gov

<table>
  <tr>
    <th>tz</th>
    <th>os</th>
    <th>total</th>
  </tr>
  <tr>
    <td>America/Sao_Paulo</td>
    <td>Not Windows</td>
    <td>13.0</td>
  </tr>
  <tr>
    <td>America/Sao_Paulo</td>
    <td>Windows</td>
    <td>20.0</td>
  </tr>
  <tr>
    <td>Europe/Madrid</td>
    <td>Not Windows</td>
    <td>16.0</td>
  </tr>
  <tr>
    <td>Europe/Madrid</td>
    <td>Windows</td>
    <td>19.0</td>
  </tr>
  <tr>
    <td>Pacific/Honolulu</td>
    <td>Not Windows</td>
    <td>0.0</td>
  </tr>
  <tr>
    <td>Pacific/Honolulu</td>
    <td>Windows</td>
    <td>36.0</td>
  </tr>
  <tr>
    <td>Asia/Tokyo</td>
    <td>Not Windows</td>
    <td>2.0</td>
  </tr>
  <tr>
    <td>Asia/Tokyo</td>
    <td>Windows</td>
    <td>35.0</td>
  </tr>
  <tr>
    <td>Europe/London</td>
    <td>Not Windows</td>
    <td>43.0</td>
  </tr>
  <tr>
    <td>Europe/London</td>
    <td>Windows</td>
    <td>31.0</td>
  </tr>
</table>

In [63]: sns.barplot(x='total', y='tz', hue='os', data=count_subset)

![Диаграмма первых 10 часовых поясов с выделением пользователей Windows и прочих](https://i.imgur.com/13.2.png)

Рис. 13.2. Первые 10 часовых поясов с выделением пользователей Windows и прочих

Из этой диаграммы трудно понять, какова процентная доля пользователей Windows в небольших группах, поэтому нормируем процентные доли групп, так чтобы в сумме получилась 1:

def norm_total(group):
    group["normed_total"] = group["total"] / group["total"].sum()
    return group

results = count_subset.groupby("tz").apply(norm_total)

Новая диаграмма показана на рис. 13.3:

In [66]: sns.barplot(x="normed_total", y="tz", hue="os", data=results)