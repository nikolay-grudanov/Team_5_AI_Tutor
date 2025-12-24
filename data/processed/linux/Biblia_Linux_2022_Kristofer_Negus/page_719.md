---
source_image: page_719.png
page_number: 719
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.07
tokens: 7468
characters: 1827
timestamp: 2025-12-24T05:05:31.670171
finish_reason: stop
---

<table>
  <tr>
    <th>Инструмент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>load_policy</td>
    <td>Загружает новые политики в ядро</td>
  </tr>
  <tr>
    <td>semodule_expand</td>
    <td>Расширяет пакет модулей политики</td>
  </tr>
  <tr>
    <td>semodule_link</td>
    <td>Связывает пакеты модулей политики вместе</td>
  </tr>
  <tr>
    <td>semodule_package</td>
    <td>Создает пакет из модуля политик</td>
  </tr>
</table>

Далее приведен пример политики, обычно используемой в качестве основы для создания локальных правил политики. Она довольно длинная, поэтому показана лишь часть:

# cat /usr/share/doc/selinux-policy/example.te

policy_module(myapp,1.0.0)

###############################################
#
# Declarations
#

type myapp_t;
type myapp_exec_t;
domain_type(myapp_t)
domain_entry_file(myapp_t, myapp_exec_t)

type myapp_log_t;
logging_log_file(myapp_log_t)
type myapp_tmp_t;
files_tmp_file(myapp_tmp_t)
...
allow myapp_t myapp_tmp_t:file manage_file_perms;
files_tmp_filetrans(myapp_t,myapp_tmp_t,file)
#

Из примера видно, что в коде политики используется специальный синтаксис. Чтобы создавать и изменять правила политики, вам нужно изучить синтаксис этого языка правил политики, научиться применять компиляторы политик SELinux и связывать файлы правил политики для формирования модулей. Для этого вам, вероятно, потребуется пройти дополнительное обучение. В этот момент может возникнуть искушение отказаться от работы с системой SELinux. Однако использовать логические типы для изменения политик гораздо проще.

Управление SELinux через логические типы

Написание правил политики SELinux и создание модулей — довольно сложная и трудоемкая работа. Создание неверных правил политики может поставить под угрозу безопасность вашей системы Linux. К счастью, SELinux работает с логическими типами.