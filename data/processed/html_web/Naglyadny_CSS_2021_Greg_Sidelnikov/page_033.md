---
source_image: page_033.png
page_number: 33
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.54
tokens: 7243
characters: 985
timestamp: 2025-12-24T09:21:20.603682
finish_reason: stop
---

2.4. ::first-line

p::first-line { text-transform: uppercase; }

<table>
  <tr>
    <th>&lt;p&gt;</th>
    <td>Это длинный абзац текста, демонстрирующий, как псевдоэлемент ::first-line влияет только на первую строку текста, даже если она является частью того же элемента абзаца.</td>
  </tr>
</table>

2.5. ::selection

::selection { background: black; color: white; caret-color: blue; }

Псевдоэлемент ::selection применяется для выделения текста.

2.6. ::slotted(*)

Псевдоселектор slotted работает только в контексте HTML-элемента template для выбора элементов slot.

::slotted(*) или ::slotted(имя-элемента)

<table>
  <tr>
    <td>
      &lt;template&gt;
      &lt;div&gt;
        &lt;slot name = "animal"&gt;&lt;/slot&gt;
        &lt;ul&gt;
          &lt;li&gt;&lt;slot name = "kind"&gt;Кот&lt;/slot&gt;&lt;/li&gt;
          &lt;li&gt;&lt;slot name = "name"&gt;Феликс&lt;/slot&gt;&lt;/li&gt;
        &lt;/ul&gt;
      &lt;/div&gt;
    &lt;/template&gt;
    </td>
  </tr>
</table>