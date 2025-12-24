---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.16
tokens: 8202
characters: 2335
timestamp: 2025-12-24T09:06:53.152127
finish_reason: stop
---

Таблица 6.4. Второй тур конкурса NIST. NIST-классификация безопасности размеров ключей алгоритмов цифровой подписи

<table>
  <tr>
    <th>Algoritм</th>
    <th>SK</th>
    <th>PK</th>
    <th>Sig</th>
    <th>SK</th>
    <th>PK</th>
    <th>Sig</th>
    <th>SK</th>
    <th>PK</th>
    <th>Sig</th>
  </tr>
  <tr>
    <td>CRYSTALS-Dilithium</td>
    <td>64</td>
    <td>1184</td>
    <td>2044</td>
    <td>64</td>
    <td>1760</td>
    <td>3366</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
  </tr>
  <tr>
    <td>FALCON</td>
    <td>1280</td>
    <td>897</td>
    <td>617</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
    <td>2304</td>
    <td>1793</td>
    <td>1233</td>
  </tr>
  <tr>
    <td>GeMSS</td>
    <td>13K</td>
    <td>352K</td>
    <td>258b</td>
    <td>34K</td>
    <td>1238K</td>
    <td>411b</td>
    <td>76K</td>
    <td>3041K</td>
    <td>576b</td>
  </tr>
  <tr>
    <td>LUOV</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
    <td>32</td>
    <td>75K</td>
    <td>494</td>
  </tr>
  <tr>
    <td>MQDSS</td>
    <td>16</td>
    <td>46</td>
    <td>20854</td>
    <td>24</td>
    <td>64</td>
    <td>43728</td>
    <td>–</td>
    <td>–</td>
    <td>–</td>
  </tr>
  <tr>
    <td>Picnic</td>
    <td>16</td>
    <td>32</td>
    <td>32 838</td>
    <td>16</td>
    <td>48</td>
    <td>74 134</td>
    <td>32</td>
    <td>64</td>
    <td>128 176</td>
  </tr>
  <tr>
    <td>qTESLA (Heuristic)</td>
    <td>126</td>
    <td>1504</td>
    <td>1376</td>
    <td>2368</td>
    <td>3104</td>
    <td>2848</td>
    <td>4672</td>
    <td>6432</td>
    <td>5920</td>
  </tr>
  <tr>
    <td>Rainbow (cyclical)</td>
    <td>93K</td>
    <td>14K</td>
    <td>512b</td>
    <td>51K</td>
    <td>711K</td>
    <td>1248b</td>
    <td>1227K</td>
    <td>170K</td>
    <td>1632b</td>
  </tr>
  <tr>
    <td>SPHINCS+ (small)</td>
    <td>64</td>
    <td>16</td>
    <td>8080</td>
    <td>64</td>
    <td>24</td>
    <td>17 064</td>
    <td>64</td>
    <td>32</td>
    <td>29 792</td>
  </tr>
</table>

Обозначения: SK – размер закрытого ключа, PK – размер открытого ключа, Sig – размер подписи.

Примечание 1: размеры в байтах, если не указано иное. К – килобайты, b – биты.

Примечание 2: цифры точки только для конкретных алгоритмов реализации в каждом криптографическом наборе.