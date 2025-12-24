---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 92.95
tokens: 12069
characters: 2930
timestamp: 2025-12-24T06:41:18.595423
finish_reason: stop
---

Рис. 22.1 (часть (б) я даже б-м нарисовал)

<table>
  <tr>
    <th>обработанное ребро</th>
    <th colspan="9">непересекающиеся множества</th>
  </tr>
  <tr>
    <th>вначале</th>
    <td>{a}</td>
    <td>{b}</td>
    <td>{c}</td>
    <td>{d}</td>
    <td>{e}</td>
    <td>{f}</td>
    <td>{g}</td>
    <td>{h}</td>
    <td>{i}</td>
    <td>{j}</td>
  </tr>
  <tr>
    <th>(b, d)</th>
    <td>{a}</td>
    <td>{b, d}</td>
    <td>{c}</td>
    <td>{e}</td>
    <td>{f}</td>
    <td>{g}</td>
    <td>{h}</td>
    <td>{i}</td>
    <td>{j}</td>
  </tr>
  <tr>
    <th>(e, g)</th>
    <td>{a}</td>
    <td>{b, d}</td>
    <td>{c}</td>
    <td>{e, g}</td>
    <td>{f}</td>
    <td>{h}</td>
    <td>{i}</td>
    <td>{j}</td>
  </tr>
  <tr>
    <th>(a, c)</th>
    <td>{a, c}</td>
    <td>{b, d}</td>
    <td>{e, g}</td>
    <td>{f}</td>
    <td>{h}</td>
    <td>{i}</td>
    <td>{j}</td>
  </tr>
  <tr>
    <th>(h, i)</th>
    <td>{a, c}</td>
    <td>{b, d}</td>
    <td>{e, g}</td>
    <td>{f}</td>
    <td>{h, i}</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>(a, b)</th>
    <td>{a, b, c, d}</td>
    <td></td>
    <td>{e, g}</td>
    <td>{f}</td>
    <td>{h, i}</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>(e, f)</th>
    <td>{a, b, c, d}</td>
    <td></td>
    <td>{e, f, g}</td>
    <td></td>
    <td>{h, i}</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>(b, c)</th>
    <td>{a, b, c, d}</td>
    <td></td>
    <td>{e, f, g}</td>
    <td></td>
    <td>{h, i}</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Рисунок 22.1 22.1 а) Граф, состоящий из четырех связных компонент: {a, b, c, d}, {e, f, g}, {h, i} и {j}. б) Последовательные состояния системы непересекающихся множеств в процессе работы алгоритма CONNECTED-COMPONENTS.

Same-Component(u, v)
1 if Find-Set(u)=Find-Set(v)
2 then return true
3 else return false

Алгоритм CONNECTED-COMPONENTS работает так. Сначала каждая вершина рассматривается как одноэлементное подмножество. Далее для каждого ребра графа мы объединяем подмножества, в которые попали концы этого ребра (рис. 22.1б). Когда все рёбра обработаны, множество вершин разбивается на связные компоненты (упр. 22.1-2). Теперь процедура SAME-COMPONENT определяет, лежат ли две данные вершины в одной связной компоненте, дважды вызвав процедуру FIND-SET.

Упражнения
22.1-1
Следуя образцу рис. 22.1, опишите выполнение алгоритма CONNECTED-COMPONENTS для графа G, у которого V[G] = {a, b, c, d, e, f, g, h, i, j, k} и E[G] = {(d, i), (f, k), (g, i), (b, g), (a, h), (i, j), (d, k), (b, j), (d, f), Рёбра обрабатываются в том порядке, в котором они выписаны.
22.1-2
Покажите, что алгоритм CONNECTED-COMPONENTS действительно находит связные компоненты графа.
22.1-3
Алгоритм CONNECTED-COMPONENTS применили к графу с v вершинами и e ребрами, состоящему из k связных компонент. Сколько при этом было вызовов процедур FIND-SET и UNION?