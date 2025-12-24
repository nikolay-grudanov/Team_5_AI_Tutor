---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.09
tokens: 7649
characters: 2139
timestamp: 2025-12-23T23:08:32.706987
finish_reason: stop
---

Таблица 11.2. Элементы API VirusTotal

<table>
  <tr>
    <th>Описание</th>
    <th>Запросить URL</th>
    <th>Параметры</th>
  </tr>
  <tr>
    <td>Получение отчета о сканировании</td>
    <td>https://www.virustotal.com/vtapi/v2/file/report</td>
    <td>apikey, resource, allinfo</td>
  </tr>
  <tr>
    <td>Выгрузка и сканирование файла</td>
    <td>https://www.virustotal.com/vtapi/v2/file/scan</td>
    <td>apikey, file</td>
  </tr>
</table>

VirusTotal хранит историю всех файлов, которые ранее были загружены и проанализированы. Чтобы определить, есть ли отчет по этому файлу, можно выполнить поиск в базе данных с помощью хеша подозрительного файла. Это избавит вас от необходимости фактически выгружать файл. Недостаток этого метода в том, что, если данный файл в VirusTotal еще никто не загружал, отчета по нему не будет.

VirusTotal принимает форматы хешей MD5, SHA1 и SHA256, которые можно генерировать с помощью md5sum, sha1sum и sha256sum соответственно. После того как вы сгенерировали хеш вашего файла, с помощью curl и запроса REST его можно отправить в VirusTotal.

Запрос REST находится в виде URL-адреса, который начинается с https://www.virustotal.com/vtapi/v2/file/report и имеет три основных параметра:

- apikey — ваш ключ API, полученный от VirusTotal;
- resource — хеш файла MD5, SHA1 или SHA256;
- allinfo — если равен true, будет возвращена дополнительная информация от других инструментов.

В качестве примера возьмем образец вредоносного ПО WannaCry, который имеет MD5-хеш db349b97c37d22f5ea1d1841e3c89eb4:

curl 'https://www.virustotal.com/vtapi/v2/file/report?apikey=replacewithapikey&resource=db349b97c37d22f5ea1d1841e3c89eb4&allinfo=false > WannaCry_VirusTotal.txt

Полученный ответ JSON содержит список всех антивирусных программ, в которых был запущен файл, и определение того, был ли этот файл определен как вредоносный. Здесь мы видим ответы от первых двух движков, Bkav и MicroWorld-eScan:

{
  "scans": {
    "Bkav": {
      "detected": true,
      "version": "1.3.0.9466",
      "result": "W32.WannaCrypLTE.Trojan",
      "update": "20180712"
    },
    "MicroWorld-eScan": {
      "detected": true,