---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.83
tokens: 7370
characters: 1037
timestamp: 2025-12-24T09:21:41.905154
finish_reason: stop
---

3.22. :not()

not(.excluded)

<table>
  <tr>
    <th>tr#first td</th>
    <th>td.excluded</th>
  </tr>
  <tr>
    <td>td.excluded</td>
    <td><b>td.default</b></td>
  </tr>
  <tr>
    <td>td.excluded</td>
    <td>td.excluded</td>
  </tr>
  <tr>
    <td>td.default</td>
    <td>td.excluded</td>
  </tr>
</table>

3.23. :empty

p::first-line { text-transform: uppercase; }

<table>
  <tr>
    <th colspan="2">&lt;p&gt; ЭТО ДЛИННЫЙ АБЗАЦ ТЕКСТА, ДЕМОНСТРИРУЮЩИЙ, КАК ПСЕВДОЭЛЕМЕНТ ::FIRST-LINE влияет только на первую строку текста, даже если она — часть того же элемента абзаца.&lt;/p&gt;</th>
  </tr>
</table>

3.24. Вложенные псевдоселекторы

p::first-letter { font-size: 200%; }

<p>Псевдоселекторы могут быть связаны.</p>

3.25. :dir(rtl) и :dir(ltr)

dir(rtl) или :dir(ltr)

<table>
  <tr>
    <td>&lt;div dir = "rtl"&gt;Справа налево&lt;/div&gt;</td>
  </tr>
  <tr>
    <td>&lt;div dir = "ltr"&gt;Слева направо&lt;/div&gt;</td>
  </tr>
  <tr>
    <td>&lt;div dir = "auto"&gt;&lt;בָּרְאֵל עִצּוֹ&gt;&lt;/div&gt;</td>
  </tr>
</table>