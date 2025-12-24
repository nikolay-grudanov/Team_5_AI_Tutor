---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.30
tokens: 11848
characters: 1453
timestamp: 2025-12-24T06:07:24.759312
finish_reason: stop
---

Таблица 1.7. Корреляция между ежедневными доходностями акций телекоммуникационных компаний

<table>
  <tr>
    <th></th>
    <th>T</th>
    <th>CTL</th>
    <th>FTR</th>
    <th>VZ</th>
    <th>LVLT</th>
  </tr>
  <tr>
    <th>T</th>
    <td>1,000</td>
    <td>0,475</td>
    <td>0,328</td>
    <td>0,678</td>
    <td>0,279</td>
  </tr>
  <tr>
    <th>CTL</th>
    <td>0,475</td>
    <td>1,000</td>
    <td>0,420</td>
    <td>0,417</td>
    <td>0,287</td>
  </tr>
  <tr>
    <th>FTR</th>
    <td>0,328</td>
    <td>0,420</td>
    <td>1,000</td>
    <td>0,287</td>
    <td>0,260</td>
  </tr>
  <tr>
    <th>VZ</th>
    <td>0,678</td>
    <td>0,417</td>
    <td>0,287</td>
    <td>1,000</td>
    <td>0,242</td>
  </tr>
  <tr>
    <th>LVLT</th>
    <td>0,279</td>
    <td>0,287</td>
    <td>0,260</td>
    <td>0,242</td>
    <td>1,000</td>
  </tr>
</table>

Таблица корреляций, аналогичная табл. 1.7, широко используется с целью отобразить связь между многочисленными переменными. На рис. 1.6 показана корреляция между ежедневными доходностями крупнейших биржевых инвестиционных фондов (exchange traded funds, ETF). Она легко создается в R при помощи пакета corrplot:

etfs <- sp500_px[row.names(sp500_px)>"2012-07-01",
                 sp500_sym[sp500_sym$sector=="etf", 'symbol']]
library(corrplot)
corrplot(cor(etfs), method = "ellipse")

![Корреляция между доходностями фондов ETF](../images/1_6.png)

Рис. 1.6. Корреляция между доходностями фондов ETF