---
source_image: docs_tutorials-evolution_list_topics_vm__site-on-lemp.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 155.18
tokens: 11026
characters: 6679
timestamp: 2025-12-24T06:36:16.398406
finish_reason: stop
---

### Развертывание сайта с использованием LEMP

С помощью этого руководства вы создадите простой сайт с использованием стека LEMP.

Вы будете использовать следующие сервисы:

• Виртуальная машина — сервис, в рамках которого предоставляется виртуальная машина, на которой будет развернут веб-сервер Nginx и СУБД MySQL.
• Публичный IP-адрес для доступа к сервису через интернет.
• Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
• Nginx — веб-сервер для проксирования запросов и организации защищенного HTTPS-доступа к приложению.
• Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. Разверните ресурсы в облаке.
2. Настройте Nginx.
3. Настройте базу данных MySQL.
4. Настройте сайт.
5. Настройте доменное имя.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Убедитесь, что вам назначена сервисная роль eiv.admin или роль администратора проекта. При необходимости настройте права или запросите их у администратора.

1. Разверните ресурсы в облаке

На этом шаге вы подготовите группу безопасности и виртуальную машину.

1. Создайте группу безопасности с названием sg-lemp в зоне доступности ru.AZ-1 и добавьте в нее правила:

<table>
  <tr>
    <th>Трафик</th>
    <th>Протокол</th>
    <th>Порт</th>
    <th>Тип источника/адресата</th>
    <th>Источник/Адресат</th>
  </tr>
  <tr>
    <td>Входящий</td>
    <td>TCP</td>
    <td>443</td>
    <td>IP-адрес</td>
    <td>0.0.0.0/0</td>
  </tr>
  <tr>
    <td>Исходящий</td>
    <td>Любой</td>
    <td>Оставьте пустым</td>
    <td>IP-адрес</td>
    <td>0.0.0.0/0</td>
  </tr>
</table>

2. Создайте виртуальную машину со следующими параметрами:
• Название — lemp-server .
• Зона доступности — ru.AZ-1 .
• Образ — на вкладке Маркетплейс выберите образ LEMP.
• Сетевой интерфейс — выберите тип Подсеть с публичным IP .
• Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
• Группы безопасности — добавьте sg-lemp .
• Имя пользователя — cloud-user .
• Метод аутентификации — Пароль
• Пароль — задайте пароль пользователя.

3. В строке созданной ВМ скопируйте и сохраните адрес из столбца Публичный IP: он потребуется для дальнейшей настройки.

2. Настройте Nginx

Сервер Nginx обрабатывает запросы пользователей к сайту.

1. Выберите виртуальную машину lemp-server в списке.
2. Перейдите на вкладку Серийная консоль.
3. Введите логин и пароль, указанные при создании виртуальной машины.
4. Обновите пакеты ОС. В серийной консоли выполните команды:

```
sudo apt update
sudo apt upgrade
```

5. Для обработки скриптов установите менеджер процессов PHP-FPM:

```
sudo apt install php8.1-fpm
```

6. Создайте новый конфигурационный файл:

```
sudo nano /etc/nginx/sites-available/mysite
```

7. Добавьте в файл конфигурацию виртуального сервера, заменив <public_ip> на публичный IP-адрес виртуальной машины lemp-server :

```nginx
server {
    listen 80;
    server_name <public_ip>.nip.io;
    root /var/www/html/mysite;
    index index.php index.html index.htm;
    location / {
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    }
    location ~ /\.ht {
        deny all;
    }
}
```

8. Добавьте ссылку на конфигурационный файл в каталоге sites-enabled :

```
sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/
```

9. Проверьте, что в конфигурации Nginx нет ошибок:

```
sudo nginx -t
```

10. Чтобы применить настройки, перезапустите Nginx:

```
sudo systemctl restart nginx
```

3. Настройте базу данных MySQL

В базе данных будут храниться записи, которые добавляются через форму на сайте.

1. Подключитесь к MySQL:

```
sudo mysql -u root -p
```

2. Создайте новую базу данных. Выполните построчно следующие команды:

```sql
CREATE DATABASE mydatabase;
USE mydatabase;
CREATE TABLE entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL
);
```

3. Создайте пользователя db_user :

```sql
CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'user_password';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'db_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Где <user_password> — пароль пользователя.

4. Настройте сайт

Сайт состоит из одной страницы с простой формой для добавления записей.

1. Создайте корневой каталог сайта:

```
sudo mkdir -p /var/www/html/mysite
```

2. Установите права доступа:

```
sudo chown -R www-data:www-data /var/www/html/mysite
sudo chmod -R 755 /var/www/html/mysite
```

3. Создайте стартовую страницу сайта:

```
sudo nano /var/www/html/mysite/index.php
```

4. Вставьте на страницу код, заменив <user_password> на пароль пользователя базы данных, созданного на предыдущем шаге:

```php
<?php
$conn = new mysqli("localhost", "db_user", "user_password", "mydatabase");
if ($conn->connect_error) {
    die("connection failed: ". $conn->connect_error);
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $content = $_POST["content"];
    $stmt = $conn->prepare("INSERT INTO entries (content) VALUES (?)");
    $stmt->bind_param("s", $content);
    $stmt->execute();
    $stmt->close();
}
$result = $conn->query("SELECT * FROM entries");
?>
<!DOCTYPE html>
<html>
<head>
    <title>Simple LEMP Site</title>
</head>
<body>
    <h1>Add a New Record</h1>
    <form method="post">
        <textarea name="content" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    <h2>Entries</h2>
    <ul>
        <?php while ($row = $result->fetch_assoc()) : ?>
            <li><?php echo htmlspecialchars($row['content']); ?></li>
        <?php endwhile; ?>
    </ul>
</body>
</html>
<?php
$conn->close();
?>
```

5. Настройте доменное имя

Для создания доменного имени и SSL-сертификата используется сервис nip.io. Также вы можете использовать собственный домен и SSL-сертификат.

1. Подготовьте доменное имя вида <public_ip>.nip.io , где <public_ip> — публичный IP-адрес виртуальной машины lemp-server .

2. Установите утилиту для формирования SSL-сертификата и запустите ее:

```
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d <public_ip>.nip.io --register-until=without-email
```

3. Откройте браузер и перейдите по адресу <public_ip>.nip.io .

При переходе по адресу вашего сайта откроется форма для добавления записей. Добавленные записи отображаются в списке под формой.

Результат

Вы развернули сайт с использованием стека LEMP и обеспечили безопасный доступ к нему через Nginx.