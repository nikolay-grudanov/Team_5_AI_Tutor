---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 78.57
tokens: 11872
characters: 2060
timestamp: 2025-12-24T03:38:24.120776
finish_reason: stop
---

<table>
  <tr>
    <th>dpkg</th>
    <td><b>dpkg [options] action</b><br>
      Инструмент для сборки, установки и управления пакетами. Является интерфейсом к dpkg-deb.<br>
      <b>Действия dpkg</b><br>
      Следующие действия выполняются непосредственно dpkg:<br>
      <b>-i pkgfile, --install pkgfile</b><br>
      Установить указанный пакет. При использовании совместно с <b>-R</b> или <b>--recursive pkgfile</b> должен быть каталогом.<br>
      <b>--unpack pkgfile</b><br>
      Распаковать пакет, но не производить настройку. При использовании совместно с <b>-R</b> или <b>--recursive pkgfile</b> должен быть каталогом.<br>
      <b>--configure [packages | -a | --pending]</b><br>
      Произвести повторную настройку одного или нескольких распакованных пакетов. При указании ключа <b>-a</b> или <b>--pending</b> вместо списка пакетов обрабатываются все распакованные, но не настроенные пакеты.<br>
      <b>-r, --remove [packages | -a | --pending]</b><br>
      <b>-P, --purge [packages | -a | --pending]</b><br>
      Удалить или уничтожить один или несколько установленных пакетов (<i>packages</i>). При удалении удаляются все файлы, кроме файлов настройки, перечисленных в <i>debian/conffiles</i>; при уничтожении удаляются также и эти файлы. При указании ключа <b>-a</b> или <b>--pending</b> команда dpkg удаляет или уничтожает все нераспакованные пакеты, назначенные (в <i>/var/lib/dpkg/status</i>) для удаления или уничтожения.<br>
      <b>--print-avail package</b><br>
      Отобразить информацию по указанному пакету из файла <i>/var/lib/dpkg/available</i>.<br>
      <b>--update-avail pkgs-file</b><br>
      <b>--merge-avail pkgs-file</b><br>
      Обновить записи о доступных файлах, содержащиеся в файле <i>/var/lib/dpkg/available</i>. Эта информация используется dpkg и dselect для создания списка доступных пакетов. Вариант update приведет к замене этой информации содержимым <i>pkgs-file</i>, распространяемых как <i>Packages</i>. Вариант merge объединяет существующую информацию и данные из <i>Packages</i>.
    </td>
  </tr>
</table>