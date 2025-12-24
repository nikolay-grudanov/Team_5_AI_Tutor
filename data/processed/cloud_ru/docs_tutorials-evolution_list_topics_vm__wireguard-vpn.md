---
source_image: docs_tutorials-evolution_list_topics_vm__wireguard-vpn.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 179.91
tokens: 13333
characters: 7744
timestamp: 2025-12-24T06:43:12.839936
finish_reason: stop
---

### Развертывание WireGuard VPN сервера с помощью Terraform в Cloud.ru Evolution

С помощью этого руководства вы научитесь автоматически развертывать защищенную VPN-инфраструктуру с использованием Terraform и WireGuard в облачной платформе Cloud.ru Evolution.

Вы развернете WireGuard на виртуальной машине и настроите конфигурацию сервера с помощью Terraform, а также настроите WireGuard на клиентском устройстве и подключитесь к VPN-серверу.

Вы будете использовать следующие сервисы:

• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
• Terraform — инструмент для управления инфраструктурой как кодом (Infrastructure as Code).
• WireGuard — современный VPN-протокол.

Шаги:

1. Установите и настройте Terraform.
2. Подготовьте файлы конфигурации.
3. Разверните инфраструктуру.
4. Установите WireGuard на клиенте.
5. Настройте сервер.
6. Настройте клиент.
7. Проверьте соединение.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте сервисный аккаунт для управления облачными ресурсами.
3. Создайте ключ доступа для аутентификации сервисного аккаунта в API Cloud.ru. Сохраните Key ID (логин) и Key Secret (пароль).
4. Скопируйте идентификатор проекта, в котором будете разворачивать ресурсы.

1. Установите и настройте Terraform

1. Установите Terraform.
   Если не удаётся скачать Terraform с сайта Hashicorp, скачайте дистрибутив Terraform из зеркала Cloud.ru.
2. Если вы загрузили дистрибутив Terraform из зеркала, добавьте в переменную PATH путь к папке с исполняемым файлом:

   export PATH=$PATH:<path>

   Где <path> — путь к исполняемому файлу Terraform.
3. Установите Terraform-провайдер.

2. Подготовьте файлы конфигурации

В конфигурационных файлах опишите облачные ресурсы, которые создает Terraform.

1. Создайте директорию для конфигурационных файлов и перейдите в нее:

   mkdir wireguard-vpn-lab && cd wireguard-vpn-lab

2. Сгенерируйте ключевую пару для подключения к серверу по SSH:

   ssh-keygen -t ed25519 -f id_ed25519 -N ""

3. Выведите на экран и скопируйте публичный ключ id_ed25519.pub :

   cat id_ed25519.pub

4. Создайте файл main.tf , содержащий определение всех создаваемых ресурсов и их конфигурацию. Вместо значений <project_id> и <ssh_public_key> укажите идентификатор проекта и содержимое публичного ключа id_ed25519.pub соответственно.

main.tf

С помощью этой конфигурации вы создадите новые ресурсы:
• виртуальную машину vpn-server с публичным IP-адресом vpn-fp ;
• группу безопасности vpn-security-group ;
• подсеть vpn-subnet .

5. Создайте файл variables.tf , содержащий все настраиваемые параметры инфраструктуры для удобства управления и повторного использования. Вместо значений <access_key> и <secret_key> укажите логин и пароль ключа доступа, который вы создали перед началом работы.

variables.tf

6. Создайте файл data.tf для получения информации о существующих ресурсах в облаке и динамической конфигурации.

data.tf

7. Создайте файл wg0.conf , содержащий конфигурацию сервера. В процессе развертывания инфраструктуры он будет автоматически скопирован на виртуальную машину vpn-server .

wg0.conf

3. Разверните инфраструктуру

1. Инициализируйте конфигурацию Terraform:

   terraform init

Если все прошло успешно, появится сообщение:

Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All Terraform commands should now work.
If you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forget, other commands will detect it and remind you to do so if necessary.

2. Проверьте корректность конфигурационных файлов с помощью команды:

   terraform validate

Если файлы корректные, появится сообщение:

Success! The configuration is valid.

3. Для предварительного просмотра изменений инфраструктуры выполните команду:

   terraform plan

В терминале появится список ресурсов с параметрами. На этом этапе изменения не будут внесены.

4. Примените изменения инфраструктуры, описанные в конфигурации Terraform:

   terraform apply

5. Подтвердите изменения: введите yes и нажмите Enter .

После создания всех ресурсов появится сообщение:

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

6. Проверьте создание ресурсов:
   a. Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности vpn-security-group со статусом «Создана».
   b. Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина vpn-server со статусом «Запущена».
   c. Скопируйте и сохраните публичный IP-адрес виртуальной машины, он понадобится для настройки клиента.
   d. Убедитесь, что в личном кабинете на странице Сети → Подсети отображается подсеть vpn-subnet со статусом «Создана».

4. Установите WireGuard на клиенте

Для подключения к серверу установите WireGuard на своем устройстве. В руководстве в качестве клиента используется устройство с ОС Ubuntu 22.04.

1. На клиенте в терминале выполните команду:

   sudo apt install wireguard

2. Сгенерируйте ключи доступа для клиента:

   wg genkey | tee client_privatekey | wg pubkey > client_publickey

3. Выведите на экран и скопируйте публичный ключ клиента:

   cat client_publickey

Подробнее об установке WireGuard на других платформах читайте на официальном сайте.

5. Настройте сервер

В конфигурации сервера укажите данные для подключения клиента.

1. Подключитесь к VM vpn-server по SSH.
2. Откройте файл конфигурации сервера:

   sudo nano /etc/wireguard/wg0.conf

3. Добавьте в конец файла настройки клиента:

   [Peer]
   PublicKey = <client_public_key>
   AllowedIPs = 10.0.0.2/32

Где <client_public_key> — публичный ключ клиента.

4. Перезапустите WireGuard:

   sudo systemctl restart wg-quick@wg0

Результат:

interface: wg0
public key: cOxq-7582hnTetq/sXKTrPOHBCZaArot8T0********
private key: (hidden)
listening port: 51820
peer: J0SrgdengE2NTmb858pt/x+cEKsBQgcvo/********
allowed ips: 10.0.0.2/32

5. Скопируйте значение public_key в выводе.

Оно потребуется на следующем этапе для настройки клиента.

6. Настройте клиент

На клиентском устройстве создайте конфигурационный файл с настройками для подключения к серверу.

1. Выведите на экран и скопируйте приватный ключ клиента:

   cat client_privatekey

2. Создайте файл конфигурации клиента:

   sudo nano /etc/wireguard/wg0.conf

3. Вставьте конфигурацию для клиента:

   [Interface]
   Address = 10.0.0.2/32
   PrivateKey = <client_private_key>
   DNS = 8.8.8.8
   [Peer]
   PublicKey = <server_public_key>
   Endpoint = <server_public_ip>:51820
   AllowedIPs = 0.0.0.0/0
   PersistentKeepalive = 25

Где:
• <client_private_key> — приватный ключ клиента.
• <server_public_key> — публичный ключ сервера.
• <server_public_ip> — публичный IP-адрес виртуальной машины vpn-server .

4. Запустите WireGuard:

   sudo systemctl start wg-quick@wg0

Соединение с сервером будет установлено.

7. Проверьте соединение

1. Проверьте статус туннеля. На клиентском устройстве выполните команду:

   wg show

Результат:

interface: wg0
public key: J0SrgdengE2NTmb858pt/x+cEKsBQgcvo/********
private key: (hidden)
listening port: 51820
fwmode: off
peer: cOxq-7582hnTetq/sXKTrPOHBCZaArot8T0********
endpoint: 10.0.0.1:51820
allowed ips: 0.0.0.0/0
latest handshake: 46 seconds ago
transfer: 92 B received, 212 B sent
persistent keepalive: every 25 seconds

2. Проверьте доступность сервера:

   ping 10.0.0.1

Результат

Вы научились использовать Terraform для создания облачной инфраструктуры, а также настраивать серверную и клиентскую часть для WireGuard VPN.