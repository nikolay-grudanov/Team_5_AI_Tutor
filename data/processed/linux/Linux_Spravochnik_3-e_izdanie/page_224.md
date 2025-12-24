---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.24
tokens: 12025
characters: 2207
timestamp: 2025-12-24T03:25:29.278674
finish_reason: stop
---

<table>
  <tr>
    <th>—d [!] address[/mask][!][port], —destination [!] address[/mask][!][port]</th>
    <th>ipchains</th>
  </tr>
  <tr>
    <td>Отбор пакетов с определенным адресом назначения (<i>address</i>). Синтаксис параметра идентичен синтаксису параметра —s.</td>
    <td></td>
  </tr>
  <tr>
    <th>—j target, —jump target</th>
    <td></td>
  </tr>
  <tr>
    <td>Переход к специальной цели или к определенной пользователем цепи. Если этот параметр для правила не указан, соответствие пакета правилу лишь увеличивает счетчики для правила, а пакет передается для проверки на соответствие следующему правилу.</td>
    <td></td>
  </tr>
  <tr>
    <th>—i[!] name, —interface name</th>
    <td></td>
  </tr>
  <tr>
    <td>Отбор пакетов интерфейса <i>name</i>[+]. <i>name</i> — это сетевой интерфейс системы (например, eth0 или ppp0). Символ «+» может использоваться для создания маски. Так, значению ppp+ соответствуют все имена интерфейсов, начинающиеся с ppp.</td>
    <td></td>
  </tr>
  <tr>
    <th>[!] —f, [!]—fragment $PARAMETER</th>
    <td></td>
  </tr>
  <tr>
    <td>Правило отбирает все, кроме первого, фрагменты разбитого на части пакета.</td>
    <td></td>
  </tr>
  <tr>
    <th>—source-port [!] port</th>
    <td></td>
  </tr>
  <tr>
    <td>Отбор пакетов с указанным значением исходного порта. Синтаксис задания портов см. в описании параметра —s.</td>
    <td></td>
  </tr>
  <tr>
    <th>—destination-port [!] port</th>
    <td></td>
  </tr>
  <tr>
    <td>Отбор пакетов с указанным значением целевого порта. Синтаксис задания портов см. в описании параметра —s.</td>
    <td></td>
  </tr>
  <tr>
    <th>—icmp-type [!] type</th>
    <td></td>
  </tr>
  <tr>
    <td>Отбор пакетов, которые имеют указанный (по имени или номеру) тип ICMP.</td>
    <td></td>
  </tr>
  <tr>
    <th>Параметры</th>
    <td></td>
  </tr>
  <tr>
    <th>—b, —bidirectional</th>
    <td></td>
  </tr>
  <tr>
    <td>Добавить правило в цепи input и output, чтобы на соответствие этому правилу проверялись как входящие, так и исходящие пакеты.</td>
    <td></td>
  </tr>
  <tr>
    <th>—v, —verbose</th>
    <td></td>
  </tr>
  <tr>
    <td>Режим подробной диагностики.</td>
    <td></td>
  </tr>
</table>