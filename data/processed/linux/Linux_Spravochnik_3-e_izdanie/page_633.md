---
source_image: page_633.png
page_number: 633
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.08
tokens: 11693
characters: 1654
timestamp: 2025-12-24T03:43:53.090407
finish_reason: stop
---

<table>
  <tr>
    <th>switch</th>
    <td>switch продолжает выполнение следующего набора команд, пока выполнение не достигнет оператора breaksw или endsw. Ниже приводится общий синтаксис конструкции switch параллельно с конкретным примером, в котором обрабатывается первый аргумент командной строки:

    <pre>
    switch (string)
      case pattern1:
        commands
        breaksw
      case pattern2:
        commands
        breaksw
      case pattern3:
        commands
        breaksw
      .
      .
      default:
        commands
        breaksw
    endsw

    switch ($argv[1])
      case -[nN]:
        nroff $file | lp
        breaksw
      case -[Pp]:
        pr $file | lp
        breaksw
      case -[Mm]:
        more $file
        breaksw
      case -[Ss]:
        sort $file
        breaksw
      default
        echo "Error-no such option"
        exit 1
        breaksw
    endsw
    </pre>
    </td>
  </tr>
  <tr>
    <th>telltc</th>
    <td>telltc<br>Только для tcsh. Отобразить все характеристики терминала и их значения.</td>
  </tr>
  <tr>
    <th>time</th>
    <td>time [command]<br>Выполнить указанную команду и вычислить время выполнения. Команда без аргумента может использоваться в сценарии для замера времени его выполнения.</td>
  </tr>
  <tr>
    <th>umask</th>
    <td>umask [nnn]<br>Отобразить маску прав доступа для вновь создаваемых файлов или установить восьмеричное значение маски nnn. Маска определяет, какие компоненты прав доступа отсутствуют у создаваемых файлов.</td>
  </tr>
  <tr>
    <th>unalias</th>
    <td>unalias name<br>Удалить name из списка псевдонимов. Подробнее см. alias.</td>
  </tr>
</table>