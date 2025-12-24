---
source_image: page_168.png
page_number: 168
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.71
tokens: 7559
characters: 1422
timestamp: 2025-12-24T09:24:50.605696
finish_reason: stop
---

Как видите, grid-макет заполняется пустыми областями:

Обратите внимание на то, как grid-область адаптируется к элементам вокруг промежутков, которые охватывают несколько строк и столбцов. Все элементы по-прежнему остаются в grid-области, но интуитивно оборачиваются вокруг других составных элементов.

<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
    <th>8</th>
  </tr>
  <tr>
    <td>9</td>
    <td colspan="3">10 grid-column: span 3</td>
    <td>11</td>
    <td rowspan="3">12<br>grid-row: span 3</td>
    <td>13</td>
    <td>14</td>
  </tr>
  <tr>
    <td>15</td>
    <td>16</td>
    <td>17</td>
    <td>18</td>
    <td>19</td>
    <td>20</td>
    <td>21</td>
  </tr>
  <tr>
    <td>22</td>
    <td colspan="3">23<br>grid-column: span 3<br>grid-row: span 3</td>
    <td>24</td>
    <td>25</td>
    <td>26</td>
  </tr>
  <tr>
    <td>27</td>
    <td colspan="3"></td>
    <td>28</td>
    <td>29</td>
    <td>30</td>
    <td>31</td>
  </tr>
  <tr>
    <td>32</td>
    <td colspan="3"></td>
    <td>33</td>
    <td>34</td>
    <td>35</td>
    <td>36</td>
  </tr>
  <tr>
    <td>37</td>
    <td>38</td>
    <td>39</td>
    <td>40</td>
    <td>41</td>
    <td>42</td>
    <td>43</td>
    <td>44</td>
  </tr>
</table>

Попытавшись разбить макет с большим промежутком, я получил следующий вид, который демонстрирует ключевые ограничения grid-макетов: