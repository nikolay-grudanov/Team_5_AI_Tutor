---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.77
tokens: 6313
characters: 1003
timestamp: 2025-12-24T04:01:41.285983
finish_reason: stop
---

Удаленный сервер своими руками

group nogroup
# Найдите директивы ca, cert и key. Закомментируйте их
#ca ca.crt
#cert client.crt
#key client.key
# Добавьте параметры cipher и auth так, как они описаны
# в server.conf
cipher AES-128-CBC
auth SHA256
# Установите key-direction в 1
key-direction 1

Теперь создадим сценарий генерации файлов конфигурации (листинг 14.1):

cd ~/clients
touch make_config
chmod +x make_config
mcedit make_config

Листинг 14.1. Файл make_config

#!/bin/bash

# First argument: Client identifier

KEY_DIR=~/openvpn-ca/keys
OUTPUT_DIR=~/clients/files
BASE_CONFIG=~/clients/base.conf

cat ${BASE_CONFIG} \
    <(echo -e '<ca>') \
    ${KEY_DIR}/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    ${KEY_DIR}/${1}.crt \
    <(echo -e '</cert>\n<key>') \
    ${KEY_DIR}/${1}.key \
    <(echo -e '</key>\n<tls-auth>') \
    ${KEY_DIR}/ta.key \
    <(echo -e '</tls-auth>') \
    > ${OUTPUT_DIR}/${1}.ovpn

Используя этот сценарий, вы сможете легко генерировать файлы конфигурации клиентов: