---
source_image: page_233.png
page_number: 233
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.39
tokens: 11959
characters: 2149
timestamp: 2025-12-24T03:25:52.280673
finish_reason: stop
---

<table>
  <tr>
    <th>iptables</th>
    <th>Команды</th>
  </tr>
  <tr>
    <td></td>
    <td><b>iptables</b> всегда выполняется с одной из следующих команд:</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-A chain rules, --append chain rules</b><br>Добавить новые правила к цепи.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-I chain number rules, --insert chain number rules</b><br>Вставить правила (<i>rules</i>) в цепь (<i>chain</i>) после правила с порядковым номером <i>number</i>.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-D chain rules, --delete chain rules</b><br>Удалить правила из цепи. Правила могут определяться их порядковыми номерами в цепи или их описанием.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-R chain number rule, --replace chain number rule</b><br>Заменить правило в цепи. Заменяемое правило определяется порядковым номером <i>number</i>.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-C chain rule, --check chain rule</b><br>Выяснить, как будет обрабатываться сетевой пакет, соответствующий указанному правилу. Правило должно определять источник, назначение, протокол и интерфейс создаваемого пакета.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-L [chain], --list $PARAMETER</b><br>Перечислить правила в цепи либо во всех цепях, если цепь не указана.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-F [chain], --flush chain</b><br>Удалить все правила цепи либо правила всех цепей, если цепь не указана.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-Z [chain], --zero chain</b><br>Обнулить счетчики байт и пакетов для цепи. Если цепь не указана, происходит обнуление счетчиков для всех цепей. В этом случае, если выполняется также команда <b>-L</b>, значения счетчиков перед обнулением отображаются.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-N chain, --new-chain chain</b><br>Создать новую цепь. Имя цепи должно быть уникальным. Эта команда предоставляет пользователю возможность создавать собственные цепи.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>-X [chain], --delete-chain chain</b><br>Удалить указанную цепь, созданную пользователем, либо все пользовательские цепи, если цепь не указана.</td>
  </tr>
</table>