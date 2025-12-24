---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.58
tokens: 7304
characters: 1525
timestamp: 2025-12-24T03:05:26.409788
finish_reason: stop
---

* base: reflector.westga.edu
* epel: mirror.vcu.edu
* extras: mirror.steadfastnet.com
* updates: mirror.mobap.edu
base | 3.6 kB
extras | 3.4 kB
hello-world | 2.9 kB
hello-world-noarch | 2.9 kB
updates | 3.4 kB
8 packages excluded due to repository priority protections
===============================================================================
matched: hello-world
===============================================================================
hello-world.noarch : A hello-world example package

Функция поиска работает должным образом, значит, и установка пакета должна пройти успешно:

$ yum --enablerepo=hello-world install hello-world
Loaded plugins: fastestmirror, priorities
Loading mirror speeds from cached hostfile
  * base: reflector.westga.edu
  * epel: mirror.vcu.edu
  * extras: mirror.steadfastnet.com
  * updates: mirror.mobap.edu
8 packages excluded due to repository priority protections
Resolving Dependencies
--> Running transaction check
---> Package hello-world.noarch 0:0.0.1-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved
Installing:
hello-world noarch 0.0.1-1 hello-world-noarch

Transaction Summary
Install 1 Package

Total download size: 8.1 k
Installed size: 1.3 k
Downloading packages:
hello-world-0.0.1-1.noarch.rpm | 8.1 kB
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : hello-world-0.0.1-1.noarch
  Verifying : hello-world-0.0.1-1.noarch

Installed:
  hello-world.noarch 0:0.0.1-1

Complete!