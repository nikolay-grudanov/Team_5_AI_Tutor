---
source_image: page_290.png
page_number: 290
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.53
tokens: 6380
characters: 1118
timestamp: 2025-12-24T04:02:35.495737
finish_reason: stop
---

Таблица 16.1. Команды конвертирования

<table>
  <tr>
    <th>Направление</th>
    <th>Команда</th>
  </tr>
  <tr>
    <td>PEM -> DER</td>
    <td>openssl x509 -outform der -in certificate.pem -out certificate.der</td>
  </tr>
  <tr>
    <td>PEM -> P7B</td>
    <td>openssl crl2pkcs7 -nocrl -certfile certificate.cer -out certificate.p7b -certfile CACert.cer</td>
  </tr>
  <tr>
    <td>PEM -> PFX</td>
    <td>openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt</td>
  </tr>
  <tr>
    <td>DER -> PEM</td>
    <td>openssl x509 -inform der -in certificate.cer -out certificate.pem</td>
  </tr>
  <tr>
    <td>P7B -> PEM</td>
    <td>openssl pkcs7 -print_certs -in certificate.p7b -out certificate.cer</td>
  </tr>
  <tr>
    <td>P7B -> PFX</td>
    <td>openssl pkcs7 -print_certs -in certificate.p7b -out certificate.ceropenssl pkcs12 -export -in certificate.cer -inkey privateKey.key -out certificate.pfx -certfile CACert.cer</td>
  </tr>
  <tr>
    <td>PFX -> PEM</td>
    <td>openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes</td>
  </tr>
</table>