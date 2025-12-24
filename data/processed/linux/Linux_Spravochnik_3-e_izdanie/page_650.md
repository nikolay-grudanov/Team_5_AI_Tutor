---
source_image: page_650.png
page_number: 650
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.60
tokens: 12204
characters: 2576
timestamp: 2025-12-24T03:44:41.176650
finish_reason: stop
---

Конспект команд по группам

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>transpose-sentences</td>
    <td>Перестановка пары предложений</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>transpose-paragraphs</td>
    <td>Перестановка пары абзацев</td>
  </tr>
</table>

Команды преобразования регистров

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>M-c</td>
    <td>capitalize-word</td>
    <td>Сделать прописной первую букву слова</td>
  </tr>
  <tr>
    <td>M-u</td>
    <td>upcase-word</td>
    <td>Сделать прописными все буквы слова</td>
  </tr>
  <tr>
    <td>M-l</td>
    <td>downcase-word</td>
    <td>Сделать строчными все буквы слова</td>
  </tr>
  <tr>
    <td>M- M-c</td>
    <td>negative-argument; capitalize-word</td>
    <td>Сделать прописной первую букву предыдущего слова</td>
  </tr>
  <tr>
    <td>M- M-u</td>
    <td>negative-argument; upcase-word</td>
    <td>Сделать прописными все буквы предыдущего слова</td>
  </tr>
  <tr>
    <td>M- M-l</td>
    <td>negative-argument; downcase-word</td>
    <td>Сделать строчными все буквы предыдущего слова</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>capitalize-region</td>
    <td>Сделать прописными первые буквы слов выделенной области</td>
  </tr>
  <tr>
    <td>C-x C-u</td>
    <td>upcase-region</td>
    <td>Сделать прописными все буквы в выделенной области</td>
  </tr>
  <tr>
    <td>C-x C-l</td>
    <td>downcase-region</td>
    <td>Сделать строчными все буквы в выделенной области</td>
  </tr>
</table>

Команды пошагового поиска

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-s</td>
    <td>isearch-forward</td>
    <td>Начать или повторить прямой пошаговый поиск</td>
  </tr>
  <tr>
    <td>C-r</td>
    <td>isearch-backward</td>
    <td>Начать или повторить обратный пошаговый поиск</td>
  </tr>
  <tr>
    <td>Enter</td>
    <td>(нет)</td>
    <td>Завершить успешный поиск</td>
  </tr>
  <tr>
    <td>C-g</td>
    <td>keyboard-quit</td>
    <td>Отменить пошаговый поиск; вернуться к начальному положению в тексте</td>
  </tr>
  <tr>
    <td>Del</td>
    <td>(нет)</td>
    <td>Удалить неверный символ в строке поиска</td>
  </tr>
  <tr>
    <td>M-C-r</td>
    <td>isearch-backward-regexp</td>
    <td>Обратный пошаговый поиск по регулярному выражению</td>
  </tr>
  <tr>
    <td>M-C-s</td>
    <td>isearch-forward-regexp</td>
    <td>Прямой пошаговый поиск по регулярному выражению</td>
  </tr>
</table>