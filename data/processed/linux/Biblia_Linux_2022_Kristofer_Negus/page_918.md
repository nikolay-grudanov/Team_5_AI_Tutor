---
source_image: page_918.png
page_number: 918
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.92
tokens: 7581
characters: 2067
timestamp: 2025-12-24T05:10:49.091783
finish_reason: stop
---

918 Приложения

б) загрузите установочный образ и установите его на жесткий диск;
в) для рабочего стола Fedora Workstation после завершения установки и перезагрузки установите следующий пакет (для других дистрибутивов Linux может потребоваться установить пакет, который предоставляет службу libvirtd):
    # yum install virt-manager libvirt-daemon-config-network

3. Чтобы убедиться, что службы sshd и libvirtd запущены в системе, введите следующее:
    # systemctl start sshd.service
    # systemctl enable sshd.service
    # systemctl start libvirtd.service
    # systemctl enable libvirtd.service

4. Загрузите установочный ISO-образ Linux, совместимый с вашим гипервизором, и скопируйте его в каталог по умолчанию, используемый программой Virtual Machine Manager. Например, если DVD с Fedora Workstation находится в текущем каталоге, можете ввести следующее:
    # cp Fedora-Workstation-Live-x86_64-30-1.2.iso /var/lib/libvirt/images/

5. Чтобы проверить настройки сетевого моста по умолчанию (virbr0), введите следующее:
    # ip addr show virbr0
    4: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state UP group default
        link/ether de:21:23:0e:2b:c1 brd ff:ff:ff:ff:ff:ff
        inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
            valid_lft forever preferred_lft forever6.

6. Чтобы установить виртуальную машину с помощью ISO-образа, скопированного ранее, выполните следующие действия:
   а) введите команду:
       # virt-manager &
   б) перейдите в меню File (Файл) и выберите New Virtual Machine (Новая виртуальная машина);
   в) выберите Local Install Media (Жесткий диск) и нажмите Forward (Далее);
   г) выберите Browse (Загрузить), выберите «живой» или установочный образ, нажмите Choose Volume (Выбрать том) и нажмите кнопку Forward (Далее);
   д) выберите подходящие память и процессоры и нажмите кнопку Forward (Далее);
   е) выберите нужный размер диска и нажмите кнопку Forward (Далее);
   ж) выберите Virtual network default: NAT (Виртуальная сеть по умолчанию: NAT), возможно, она уже выбрана;