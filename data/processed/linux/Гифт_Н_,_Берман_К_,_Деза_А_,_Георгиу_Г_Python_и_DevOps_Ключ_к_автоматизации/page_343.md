---
source_image: page_343.png
page_number: 343
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.67
tokens: 7919
characters: 2007
timestamp: 2025-12-24T03:10:07.483496
finish_reason: stop
---

$ gpg --generate-key
pub rsa2048 2019-07-12 [SC] [expires: 2021-07-11]
    E14104A0890994B9AC9C9F6782C1FF5E679EFF32
uid                  pydevops <my.email@gmail.com>
sub rsa2048 2019-07-12 [E] [expires: 2021-07-11]

Далее скачайте с веб-страницы пакет sops с его выпусками (https://github.com/mozilla/sops/releases).

Для создания нового зашифрованного файла с названием, например, environment.secrets запустите утилиту sops с флагом -pgp и передайте ей сигнатуру сгенерированного ранее ключа:

$ sops --pgp BBDE7E57E00B98B3F4FBEAF21A1EEF4263996BD0 environment.secrets

В результате будет открыт текстовый редактор по умолчанию, в который можно будет ввести секретные данные в виде открытого текста. В этом примере файл environment.secrets содержит следующее:

export DBPASS=MYPASS

Сохранив файл environment.secrets, проинспектируйте его, чтобы убедиться, что он зашифрован и его можно спокойно вносить в систему управления исходными кодами:

$ cat environment.secrets
{
  "data": "ENC[AES256_GCM,data:q1Q5zc7e8KgGmu5goC9WmE7PP8gueBoSsmM=,
    iv:xG8BHcRfdfLpH9nU1TijsYrh4TuSdvDqp5F+2Hqw4I=,
    tag:0OIVAm90/UYGljGCzZerTQ==,type:str]",
  "sops": {
    "kms": null,
    "gcp_kms": null,
    "lastmodified": "2019-07-12T05:03:45Z",
    "mac": "ENC[AES256_GCM,data:wo+zPVbPbAJt9Nl23nYuWs55f68/DZJWj3pc0
      l8T2d/SbuRF6YCuOXHSHIKs1ZBpSlsjmIrPyYTqI+M4Wf7it7fnNS8b7FnclwmxJjptBWgL
      T/A1GzIKT1Vrgw9QgJ+prq+Qcrk5dPzhsOTxOoOhGRPsyN8KjkS4sGuXM=,iv:0VvSMgjF6
      ypcK+1J54fonRoI7c5whmcu3iNV8xLH02k=,
      tag:YaI7DXvvllvpJ3Talzl8lg==,
      type:str]",
    "pgp": [
      {
        "created_at": "2019-07-12T05:02:24Z",
        "enc": "-----BEGIN PGP MESSAGE-----\n\nhQEAMA+3cyc
          g5b/Hu0OvU5ONr/F0htZM2MZQSXpxoCi0/nWGB5Czc8FTS1RSwu8/c0x0Ch1FwH+IdLwwL+jd
          oXVe55myuu/3OKUy7H1w/W2R/nPI99Biw1m5u3ir3+9tLXmRpLWkz7+nX7FThl9QnOS25
          NRUSSxS7hNaZMcYjpXW+w/nM3XeaGStgbJ90gIp4A8YGigZQVZZFl3fAG3bm2c+TNJcAb1
          zDpc40fxlR+7LroJI\njuidzyOEe49k0pq3tzqCnph5wPr3HZ1JeQmsIquf//9D509S5xH