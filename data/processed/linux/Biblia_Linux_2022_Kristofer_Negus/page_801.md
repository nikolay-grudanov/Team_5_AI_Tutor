---
source_image: page_801.png
page_number: 801
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.06
tokens: 7752
characters: 2288
timestamp: 2025-12-24T05:07:56.936779
finish_reason: stop
---

Расширение настроек службы cloud-init

Вы можете добавить в свои файлы meta-data и user-data гораздо больше информации для настройки облачных образов. Примеры настроек cloud-init можно найти на странице Cloud-Init (cloudinit.readthedocs.org/en/latest/topics/examples.html). В следующих разделах приведены примеры настроек, которые можно добавить в файлы user-data.

ПРИМЕЧАНИЕ
Файлы user-data и meta-data имеют формат yaml. Этот формат использует отступы и хорошо известные разделители. Элементам в списке предшествуют дефис и пробел. Ключи и значения разделяются двоеточием и пробелом. Если вы не знакомы с форматом yaml, рекомендую изучить его на сайте проекта Yaml (github.com/yaml).

Добавление ssh-ключей с помощью службы cloud-init

Вместо того чтобы использовать пароли для входа в облачные образы, вы можете задействовать аутентификацию на основе ключей вместе с командой ssh для входа в систему по сети. Такой способ обычно применяют облачные провайдеры для предоставления пользователю доступа к облачным образам.

Если вы уже сгенерировали открытый и закрытый ssh-ключи для учетной записи пользователя, с помощью которой планируете создать облачный образ, можете задействовать их для аутентификации. Если сгенерировали пару ключей RSA, то по умолчанию открытый ключ находится в файле id_rsa.pub:

# cat $HOME/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMzdq6hqDUhueWzl7rIUwjxB/rrJY4oZpoWINzeGVf6m8wX1Hmmqd9C7LtnZg2P24/ZBb3S1j7vK2WymOcwEoWekhbZHBAyYeqXKYQQjUB2E2Mr6qMkmrjQBx6ypxbz+VwADNCwegY5RCUoNjrN43GVu6nSOxhFf7hv6dtCjvos0vtt0979YS3UcEyrobpNzreGSJ8FMPMRFMWWg68Jz5hOMCIE1IldhpODvQVbTNsn/STx07ZwSYV6kfDj0szvdodDCyh8mPNC1kIDhf/qu/Zn1kxQ9xfecQ+SUi+2IWN69o1fNpexJPFr+Bwjkwcrk58C6uowG5eNSgnuu7GMUkT root@host2.example.com

Открытый ключ из этого файла обычно копируется в файл $HOME/.ssh/authorized_keys для пользователя удаленной системы, в которую нужно войти. Можно добавить ключ к этому файлу на облачном образе, применяя записи в файле user-data, который выглядит следующим образом:

users:
  - default
    name: wsmith
    gecos: William B. Smith
    primary-group: wsmith
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock-passwd: true
    ssh-authorized-keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMzdq6hqDUhueWzl7rIUwjxB/rrJY4oZpoWINzeGVf6m8wX1Hmmqd9C7LtnZg2P24/