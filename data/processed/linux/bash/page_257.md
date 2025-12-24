---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.42
tokens: 7457
characters: 1739
timestamp: 2025-12-23T23:11:31.970221
finish_reason: stop
---

После того как событие записано, можно запустить wevtutil, чтобы увидеть последнюю запись в журнале APPLICATION:

$ wevtutil qe APPLICATION //c:1 //rd:true

<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'>
    <System>
        <Provider Name='Cybersecurity Ops'/>
        <EventID Qualifiers='0'>200</EventID>
        <Level>4</Level>
        <Task>0</Task>
        <Keywords>0x8000000000000000</Keywords>
        <TimeCreated SystemTime='2018-11-30T15:32:25.000000000Z'/>
        <EventRecordID>120114</EventRecordID>
        <Channel>Application</Channel>
        <Computer>localhost</Computer>
        <Security UserID='S-1-5-21-7325229459-428594289-642442149-1001'/>
    </System>
    <EventData>
        <Data>This is an event</Data>
    </EventData>
</Event>

С помощью параметра /s, позволяющего указать имя удаленного хоста или IP-адрес, вы можете записывать события в журналы удаленной системы Windows. Параметр /u применяется для указания имени пользователя в удаленной системе, а параметр /p — для указания пароля пользователя.

Создание журналов Linux

Команда logger предназначена для записи событий в системный журнал Linux. Эти события обычно хранятся в файле /var/log/messages, но указанный путь может отличаться в зависимости от дистрибутива Linux.

Чтобы записать запись в журнал, напишите следующее:

logger 'This is an event'

Вы можете использовать команду tail, чтобы увидеть запись сразу после ее фиксации:

$ tail -n 1 /var/log/messages

Nov 30 12:07:55 kali root: This is an event

Можно записать вывод прямо из команды, передав их в logger. Это может быть особенно полезно для сбора выходных данных или сообщений об ошибках, генерируемых автоматизированными задачами, такими как задания cron.