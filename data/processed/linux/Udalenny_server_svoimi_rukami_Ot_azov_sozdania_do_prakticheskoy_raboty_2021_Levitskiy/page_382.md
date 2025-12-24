---
source_image: page_382.png
page_number: 382
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.50
tokens: 6318
characters: 1231
timestamp: 2025-12-24T04:04:17.272197
finish_reason: stop
---

Add Hardware Wizard

Select an Existing Disk
Which previously configured disk would you like to use?

Disk file
One disk file will be created for each 2 GB of virtual disk capacity. File names for each file beyond the first will be automatically generated using the file name provided here as a basis.

File E:\vm\vmware.vmdk Browse...

Mode
Independent disks are not affected by snapshots.
Persistent
Changes are immediately and permanently written to the disk.
Nonpersistent
Changes to the disk are discarded when you power off or restore a snapshot.

Рис. 21.13. Указываем путь к vmdk-файлу

Укажите путь к файлу, который был получен в результате конвертации (vmware.vmdk), см. рис. 21.13.

Теперь нам осталось удалить первый диск, который был создан при создании виртуальной машины. Выделите его в списке оборудования и нажмите кнопку Remove (рис. 12). Закройте окно Virtual Machine Settings, нажав кнопку OK.

Включите виртуальную машину, чтобы проверить, что все корректно. Если все хорошо, тогда выберите команду меню File, Export to OVF. В появившемся окне (рис. 21.15) выберите, куда нужно сохранить OVF-файл. Будет запущен процесс конвертации. Дождитесь его завершения, после чего вы получите OVF-файл виртуальной машины.