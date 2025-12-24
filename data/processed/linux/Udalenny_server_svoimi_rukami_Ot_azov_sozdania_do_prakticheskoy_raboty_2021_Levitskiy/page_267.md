---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.74
tokens: 6264
characters: 1099
timestamp: 2025-12-24T04:01:55.745769
finish_reason: stop
---

<table>
  <tr>
    <th>DirectoryIndex</th>
    <td>Позволяет задать название документа, который будет возвращен по запросу, который не содержит имя документа. С помощью данной директивы можно задать несколько имен файлов. Значениями по умолчанию являются index.html index.php index.htm index.shtml index.cgi Default.htm default.htm index.php3. Например, если вы введете в строке адреса броузера http://localhost, то будет возвращен один из указанных в директиве DirectoryIndex документов. Если в каталоге будет несколько документов, описанных в DirectoryIndex, то будет возвращен первый из них (в данном случае – index.html)</td>
  </tr>
  <tr>
    <th>FancyIndexing</th>
    <td>При получении запроса, не содержащего имя документа, сервер передаст один из файлов, указанных в директиве DirectoryIndex. Если такой файл не существует, клиенту будет возвращено оглавление каталога. При включении директивы FancyIndexing, в оглавлении каталога будут использованы значки и описания файлов. Если директива FancyIndexing выключена, оглавление будет представлено в более простом виде.</td>
  </tr>
</table>