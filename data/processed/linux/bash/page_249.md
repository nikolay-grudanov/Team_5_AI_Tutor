---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.98
tokens: 7238
characters: 1287
timestamp: 2025-12-23T23:11:11.931397
finish_reason: stop
---

$ net user

User accounts for \\COMPUTER

Administrator        Guest        jsmith
The command completed successfully.

Управление группами, связанными с доменом Windows, осуществляется с помощью команды net group. Команда net localgroup предназначена для управления локальными системными группами. Чтобы добавить группу под названием accounting, введите следующее:

net localgroup accounting //add

Чтобы добавить пользователя jsmith в новую учетную группу, напишите:

net localgroup accounting jsmith //add

Для подтверждения, что jsmith был добавлен в качестве члена группы, используйте команду net localgroup:

$ net localgroup accounting

Alias name    accounting
Comment

Members

jsmith
The command completed successfully.

Кроме того, команду net user можно использовать для просмотра всех групп, в которые входит пользователь jsmith, и другой полезной информации:

$ net user jsmith

User name                jsmith
Full Name
Comment
User's comment
Country/region code      000 (System Default)
Account active           Yes
Account expires          Never

Password last set        2/26/2015 10:40:17 AM
Password expires         Never
Password changeable     2/26/2015 10:40:17 AM
Password required       Yes
User may change password Yes

Workstations allowed    All
Logon script