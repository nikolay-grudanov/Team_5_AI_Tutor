---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.09
tokens: 7793
characters: 2168
timestamp: 2025-12-23T23:08:48.283903
finish_reason: stop
---

использования файла Windows calc.exe, который обычно можно найти в каталоге C:\Windows\System32:

curl --request POST --url 'https://www.virustotal.com/vtapi/v2/file/scan' --form 'apikey=replacewithapikey' --form 'file=@/c/Windows/System32/calc.exe'

Результаты после выгрузки файла будут получены не сразу. Возвращается, например, следующий объект JSON, содержащий метаданные файла, который можно использовать для последующего получения отчета с применением идентификатора сканирования или одного из значений хеш-функции:

{
"scan_id": "5543a258a819524b477dac619efa82b7f42822e3f446c9709fadc25fdff94226-1..",
"sha1": "7ffebfee4b3c05a0a8731e859bf20ebb0b98b5fa",
"resource": "5543a258a819524b477dac619efa82b7f42822e3f446c9709fadc25fdff94226",
"response_code": 1,
"sha256": "5543a258a819524b477dac619efa82b7f42822e3f446c9709fadc25fdff94226",
"permalink": "https://www.virustotal.com/file/5543a258a819524b477dac619efa82b7..",
"md5": "d82c445e3d484f31cd2638a4338e5fd9",
"verbose_msg": "Scan request successfully queued, come back later for the report"
}

Сканирование URL-адресов, доменов и IP-адресов

VirusTotal также предоставляет возможность сканирования определенного URL, домена или IP-адреса. Все вызовы API схожи в том, что они отправляют HTTP-запрос GET на соответствующий URL-адрес, указанный в табл. 11.3 с соответствующими параметрами.

Таблица 11.3. VirusTotal URL API

<table>
  <tr>
    <th>Описание</th>
    <th>Запросить URL</th>
    <th>Параметры</th>
  </tr>
  <tr>
    <td>Отчет по URL</td>
    <td>https://www.virustotal.com/vtapi/v2/url/report</td>
    <td>apikey, resource, allinfo, scan</td>
  </tr>
  <tr>
    <td>Доменный отчет</td>
    <td>https://www.virustotal.com/vtapi/v2/domain/report</td>
    <td>apikey, domain</td>
  </tr>
  <tr>
    <td>Отчет по IP</td>
    <td>https://www.virustotal.com/vtapi/v2/ip-address/report</td>
    <td>apikey, ip</td>
  </tr>
</table>

Вот пример запроса отчета сканирования по URL-адресу:

curl 'https://www.virustotal.com/vtapi/v2/url/report?apikey=replacewithapikey&resource=www.oreilly.com&allinfo=false&scan=1'

Параметр scan=1 автоматически отправит URL-адрес для анализа, если его еще нет в базе данных.