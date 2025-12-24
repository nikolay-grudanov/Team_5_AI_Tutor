---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.79
tokens: 8105
characters: 2889
timestamp: 2025-12-24T04:22:05.178925
finish_reason: stop
---

Если неверно указать версию, то дискета не будет создана, потому что программа ищет необходимые для загрузочной дискеты файлы в каталоге /lib/modules/ver, где ver — это номер версии. В моем случае это каталог /lib/modules/2.6.31.

3.8.2. Обновление ядра из пакета

Обновление из графической оболочки скорей всего будет настроено автоматически, и графическая оболочка Linux предупредит вас, когда станут доступны новые обновления, и установит их.

Самый простой способ установить новое ядро — использование пакета. Процесс установки такой же, как и любой другой программы. Для обновления в Red Hat версиях Linux можно выполнить команду:

rpm -Uvh ИмяПакета

Если вы хотите установить новое ядро, то ключ U необходимо заменить на ключ i. ОС Linux удобна тем, что можно одновременно установить несколько ядер. Правда, загрузить можно будет только одно из них.

Из пакета rpm устанавливаются только файлы, модули и загрузчик, но чтобы можно было загрузиться с новым ядром, необходимо еще прописать ядро в загрузчик GRUB.

[sudo] password for mflenov:
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages have been kept back:
    linux-generic linux-headers-generic linux-image-generic
The following packages will be upgraded:
    apache2 apache2-bin apache2-data apache2-mpm-prefork apparmor apport
    avahi-daemon cups cups-bsd cups-client cups-common cups-daemon cups-ppdc
    cups-server-common curl gcc-4.8-base gnupg gpgv grub-common grub-pc
    grub-pc-bin grub2-common initramfs-tools initramfs-tools-bin
    libapache2-mod-php5 libapparmor-perl libapparmor1 libavahi-client3
    libavahi-common-data libavahi-common3 libavahi-core7 libavahi-glib1 libcups2
    libcupscgi1 libcupsimage2 libcupsmime1 libcupsppdc1 libcurl3 libcurl3-gnutls
    libdrm2 libgcc1 libglib2.0-0 libglib2.0-data libgudev-1.0-0 libmysqclient18
    libpam-smbpass libpam-systemd libpixman-1-0 libpq5 libprocps0 libstdc++6
    libsystemd-daemon0 libsystemd-login0 libudev1 libwbclient0 mysql-client-5.5
    mysql-client-core-5.5 mysql-common mysql-server mysql-server-5.5
    mysql-server-core-5.5 openssh-client openssh-server php5-cli php5-common
    php5-mysql php5-readline postgresql-9.1 postgresql-client-9.1
    postgresql-contrib-9.1 postgresql-doc-9.1 procps python3-apport
    python3-distupgrade python3-problem-report python3-software-properties
    python3-update-manager samba samba-common samba-common-bin samba-doc
    smbclient software-properties-common systemd-services systemd-shim
    ubuntu-release-upgrader-core udev update-manager-core update-notifier-common
    winbind wpa_supplicant
91 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
Need to get 72.6 MB of archives.
After this operation, 202 kB of additional disk space will be used.
Do you want to continue [Y/n]? _

Рис. 3.6. Предложение обновить список пакетов