---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.97
tokens: 8511
characters: 1772
timestamp: 2025-12-24T02:17:58.153938
finish_reason: stop
---

<table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>loop.last</td>
    <td>True if last iteration</td>
  </tr>
  <tr>
    <td>loop.length</td>
    <td>The number of items in the sequence</td>
  </tr>
  <tr>
    <td>loop.cycle</td>
    <td>A helper function to cycle between a list of sequences</td>
  </tr>
  <tr>
    <td>loop.depth</td>
    <td>Indicates how deep in a recursive loop the rendering currently is; starts at level 1</td>
  </tr>
  <tr>
    <td>loop.depth0</td>
    <td>Indicates how deep in a recursive loop the rendering currently is; starts at level 0</td>
  </tr>
  <tr>
    <td>loop.previtem</td>
    <td>The item from the previous iteration of the loop; undefined during the first iteration</td>
  </tr>
  <tr>
    <td>loop.nextitem</td>
    <td>The item from the following iteration of the loop; undefined during the last iteration</td>
  </tr>
  <tr>
    <td>loop.changed(*val)</td>
    <td>True if previously called with a different value (or not called at all)</td>
  </tr>
</table>

Макросы

Макрос в Jinja — это функция, которая возвращает строку HTML.
Основной вариант использования макросов — избежать повторения кода и вместо этого использовать один вызов функции. Например, макрос ввода определен для сокращения непрерывного определения тегов ввода в HTML-форме:

```jinja
{% macro input(name, value='', type='text', size=20 %}
    <div class="form">
        <input type="{{ type }}" name="{{ name }}"
            value="{{ value|escape }}" size="{{ size }}">
    </div>
{% endmacro %}
```

Теперь, чтобы быстро создать ввод в вашей форме, вызывается макрос:

```jinja
{{ input('item') }}
```

Это вернет следующее:

```html
<div class="form">
    <input type="text" name="item" value="" size="20">
</div>
```