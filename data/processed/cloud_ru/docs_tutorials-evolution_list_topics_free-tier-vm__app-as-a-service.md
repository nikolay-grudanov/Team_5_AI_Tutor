---
source_image: docs_tutorials-evolution_list_topics_free-tier-vm__app-as-a-service.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 148.73
tokens: 17526
characters: 11496
timestamp: 2025-12-24T05:39:17.827273
finish_reason: stop
---

Запуск приложения на виртуальной машине в качестве службы

С помощью этого руководства вы развернете сервис для автоматического создания резервных копий выбранной директории на виртуальной машине.

Вы создадите служебный NodeJS-сервис, научитесь работать с дополнительным виртуальным диском, а также настроите запуск сервиса как systemd-службы для автоматизации процессов.

Вы будете использовать следующие сервисы:

• Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
• Systemd — системный менеджер служб в Linux.
• NodeJS и TypeScript — стек для разработки серверных приложений на языке JavaScript.

Шаги:

1. Создайте виртуальную машину.
2. Настройте группу безопасности.
3. Подключите и настройте дополнительный диск.
4. Подготовьте диск к работе.
5. Установите NodeJS и зависимости.
6. Создайте и соберите сервис резервного копирования.
7. Настройте запуск сервиса как systemd-службы.

Перед началом работы

Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, войдите под своей учетной записью.

1. Создайте виртуальную машину

На виртуальной машине будет запущена служба резервного копирования данных.

Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например backup-service.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. Назначьте публичный IP-адрес виртуальной машины — оставьте включенную опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен прямой публичный IP.
4. В поле Логин укажите логин пользователя виртуальной машины, например user1.
5. Выберите метод аутентификации — пароль.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

• отображается виртуальная машина backup-service;
• статус виртуальной машины — «Запущена»;
• виртуальной машине назначен публичный IP-адрес.

2. Настройте группу безопасности

Группы безопасности в облаке Evolution позволяют контролировать входящий и исходящий трафик для создаваемых ресурсов.

Вы настроите правила фильтрации трафика — разрешите весь исходящий трафик виртуальной машины. Создайте новую группу безопасности со следующими параметрами:

1. Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины backup-service.
2. Укажите Название группы безопасности, например allow-outbound-traffic.
3. Добавьте правило исходящего трафика:
   • Протокол — Любой.
   • Порт — оставьте пустым.
   • Тип адресата — IP-адрес.
   • Адресат — 0.0.0.0/0.
4. Назначьте созданную группу безопасности виртуальной машине backup-service.

Убедитесь, что на странице виртуальной машины в разделе Сетевые параметры для сетевого интерфейса с публичным IP отображается группа безопасности allow-outbound-traffic.

3. Подключите и настройте дополнительный диск

Резервные копии рекомендуется хранить отдельно от основного системного диска.

1. Создайте диск со следующими параметрами:
   a. В поле Зона доступности укажите ту же зону, что выбрана для виртуальной машины.
   b. Укажите название диска — backup-disk.
   c. Укажите размер диска — 10 ГБ.
2. Подключите диск к виртуальной машине:
   a. В строке созданного диска нажмите *** и выберите Подключить.
   b. Выберите виртуальную машину backup-service в списке и нажмите Подключить.

Убедитесь, что в личном кабинете на странице сервиса «Диски»:

• отображается диск backup-disk;
• статус диска — «Используется»;
• в столбце Ресурс указанна виртуальная машина backup-service.

4. Подготовьте диск к работе

После подключения отформатируйте диск, смонтируйте его и настройте права доступа.

1. Подключитесь к виртуальной машине через серийную консоль.
2. Отформатируйте диск:
   a. Получите список дисков виртуальной машины. В терминале выполните команду:

      lsblk

   Подключенный диск отображается в конце списка с именем vdb.
   b. Отформатируйте диск и создайте файловую систему:

      sudo mkfs -t xfs /dev/vdb

3. Смонтируйте диск с именем backup-disk:
   a. Создайте каталог для точки монтирования диска:

      sudo mkdir /backup-disk

   b. Выполните монтирование в созданный каталог:

      sudo mount /dev/vdb /backup-disk

4. Выдайте всем пользователям вашего проекта права на чтение и запись данных диска:

   sudo chmod a+rw /backup-disk

5. Проверьте с помощью команды lsblk , что диск backup-disk смонтирован и доступен.

5. Установите NodeJS и зависимости

На этом этапе установите NodeJS (через NVM), а также необходимые инструменты для работы сервиса резервного копирования.

1. В серийной консоли виртуальной машины последовательно выполните команды:

   sudo apt-get update -y
   sudo apt-get install -y curl
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
   source ~/.bashrc
   nvm install 18
   nvm use 18

2. Проверьте, что NodeJS и npm установлены:

   node --v
   npm --v

В результате отобразятся установленные версии.

6. Создайте и соберите сервис резервного копирования

Разверните проект резервного копирования, настройте параметры TypeScript, создайте конфигурационные и исходные файлы.

1. Создайте директорию для файлов, которые будут копироваться:

   mkdir files

2. Создайте директорию проекта:

   mkdir backup-service

3. Перейдите в директорию проекта:

   cd backup-service

4. Проинициализируйте проект NodeJS:

   npm init -y

5. Установите зависимости:

   npm install typescript ts-node @types/node --save-dev
   npm install node-cron fs-extras
   npm install @types/fs-extras --save-dev

6. Сгенерируйте файл tsconfig.json :

   npx tsc --init --module commonjs

7. Откройте файл tsconfig.json для редактирования:

   nano tsconfig.json

8. Вставьте в файл конфигурацию:

   {
     "compilerOptions": {
       "target": "es2016",
       "module": "commonjs",
       "outDir": "./dist",
       "rootDir": "./src",
       "strict": true,
       "esModuleInterop": true,
       "skipLibCheck": true,
       "forceConsistentCasingInFileNames": true,
       "sourceMap": true
     },
     "include": ["src/**/*"],
     "exclude": ["node_modules", "dist"]
   }

9. Создайте директорию src и файл config.json :

   mkdir src
   touch config.json
   nano config.json

10. Вставьте в файл конфигурацию:

   {
     "inputDir": "/home/user1/files",
     "outputDir": "/backup-disk/backups",
     "backupInterval": "* * * * *",
     "logLevel": "info"
   }

11. Создайте основной скрипт резервного копирования:

   cd src
   touch backup-service.ts
   nano backup-service.ts

12. Вставьте код скрипта:

   import * as fs from 'fs-extras';
   import * as path from 'path';
   import * as cron from 'node-cron';

   interface BackupConfig {
     inputDir: string;
     outputDir: string;
     backupInterval: string;
     logLevel: string;
   }

   class BackupService {
     private config: BackupConfig;

     constructor(configPath: string) {
       this.config = this.loadConfig(configPath);
     }

     private loadConfig(configPath: string): BackupConfig {
       try {
         const configData = fs.readFileSync(configPath, 'utf8');
         return JSON.parse(configData);
       } catch (error) {
         console.error('Error loading configuration:', error);
         process.exit(1);
       }
     }

     private async performBackup(): Promise<void> {
       try {
         const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
         const backupDir = path.join(this.config.outputDir, `backup-${timestamp}`);
         console.log(`Starting backup from ${this.config.inputDir} to ${backupDir}`);

         // Ensure output directory exists
         await fs.ensureDir(this.config.outputDir);

         // Copy directory recursively
         await fs.copy(this.config.inputDir, backupDir);
         console.log(`Backup completed successfully at ${new Date().toISOString()}`);
       } catch (error) {
         console.error('Backup failed:', error);
       }
     }

     public start(): void {
       console.log(`Backup service started with interval: ${this.config.backupInterval}`);

       // Schedule backup job
       cron.schedule(this.config.backupInterval, () => {
         this.performBackup();
       });

       // Perform initial backup
       this.performBackup();
     }

     // Start the service
     const configPath = process.env.CONFIG_PATH || './config.json';
     const backupService = new BackupService(configPath);
     backupService.start();

     // Keep the process running
     process.on('SIGTERM', () => {
       console.log('Backup service shutting down...');
       process.exit(0);
     });
     process.on('SIGINT', () => {
       console.log('Backup service shutting down...');
       process.exit(0);
     });
   }

13. Откройте файл package.json для редактирования:

   cd ..
   nano package.json

14. Отредактируйте скрипты запуска в секции scripts:

   {
     "scripts": {
       "test": "ts",
       "start": "node dist/backup-service.js",
       "dev": "ts-node src/backup-service.ts"
     }
   }

15. Соберите проект:

   npm run build

16. Проверьте, что сборка успешно завершена — файл dist/backup-service.js создан:

   cat dist/backup-service.js

7. Настройте запуск сервиса как systemd-службы

На заключительном этапе настройте автоматический запуск сервиса резервного копирования через systemd.

1. Создайте конфигурацию службы:

   sudo nano /etc/systemd/system/backup-service.service

2. Вставьте следующее содержимое:

   [Unit]
   Description=Directory Backup Service
   After=network.target

   [Service]
   Type=simple
   User=user1
   Group=user1
   WorkingDirectory=/home/user1/backup-service
   ExecStart=/home/user1/nvm/versions/node/v20.19.3/bin/node /home/user1/backup-service/dist/backup-service
   Environment=NODE_ENV=production
   Environment=CONFIG_PATH=/home/user1/backup-service/config.json
   Restart=always
   RestartSec=10
   StandardOutput=syslog
   StandardError=syslog
   SyslogIdentifier=backup-service

   [Install]
   WantedBy=multi-user.target

3. Перезапустите менеджер systemd и активируйте службу:

   sudo systemctl daemon-reload
   sudo systemctl enable backup-service
   sudo systemctl start backup-service

После запуска службы копирование файлов будет автоматически запускаться каждые 10 минут.

4. Проверьте работоспособность службы:

   sudo systemctl status backup-service

Результат:

   backup-service.service - Directory Backup Service
   Loaded: loaded (/etc/systemd/system/backup-service.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2023-07-15 13:35:55 MSK; 1h 3min ago
   Main PID: 213ms
   Tasks: 11 (limit: 1016)
   Memory: 17.9M
   CPU: 213ms
   CGroup: /system.slice/backup-service.service
   └─2177 /home/user1/nvm/versions/node/v20.19.3/bin/node /home/user1/backup-service/dist/bac

У работающей службы в поле «Active» отображается значение «active (running)».

5. Создайте несколько файлов в директории files:

   cd ../files
   touch 1.txt
   touch 2.txt

6. Проверьте, что резервные копии директории files появляются в директории /backup-disk/backups .

   cd ../../backup-disk/backups

Каждая копия хранится в отдельной директории внутри /backup-disk/backups .

7. Перезагрузите виртуальную машину и убедитесь, что служба автоматически запустилась.

Результат

Вы развернули надежный сервис резервного копирования на NodeJS и systemd в облаке Cloud.ru, освоили управление дополнительным диском и автоматизацию обслуживающих процессов Linux.