---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.27
tokens: 6588
characters: 1869
timestamp: 2025-12-24T04:02:17.717539
finish_reason: stop
---

Таблица 15.4. Значения директивы AllowOverride

<table>
  <tr>
    <th>Значение</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>None</td>
    <td>Сервер Apache будет игнорировать файлы .htaccess. Рекомендую установить данную опцию, так как это повысит производительность сервера</td>
  </tr>
  <tr>
    <td>All</td>
    <td>Пользователи имеют право переопределять в файлах .htaccess глобальные параметры доступа. Из соображений безопасности лучше не использовать этот режим</td>
  </tr>
  <tr>
    <td>Options</td>
    <td>Разрешает использовать директиву Options</td>
  </tr>
  <tr>
    <td>Limit</td>
    <td>Разрешает использовать директиву Limit</td>
  </tr>
  <tr>
    <td>AuthConfig</td>
    <td>Разрешает использование директив AuthName, AuthType, AuthUserFile и AuthGroupFile</td>
  </tr>
  <tr>
    <td>FileInfo</td>
    <td>Разрешает использовать в файлах .htaccess директивы AddType и AddEncoding</td>
  </tr>
</table>

С помощью директивы Options можно определить функции сервера, которые будут доступны для использования в определяемом каталоге. Данную директиву можно использовать как в файле apache2.conf, так и в файлах .htaccess. Допустимые опции для директивы Options представлены в табл. 15.5.

Таблица 15.5. Допустимые опции директивы Options

<table>
  <tr>
    <th>Опция</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>None</td>
    <td>Не разрешается использование каких-либо функций</td>
  </tr>
  <tr>
    <td>All</td>
    <td>Разрешаются все функции</td>
  </tr>
  <tr>
    <td>FollowSymLinks</td>
    <td>Разрешается использовать символические ссылки. С точки зрения безопасности не рекомендуется использовать этот режим</td>
  </tr>
  <tr>
    <td>SymLinksIfOwnerMatch</td>
    <td>Разрешается использование символьских ссылок, если ссылка указывает на объект, который принадлежит тому же пользователю, что и ссылка</td>
  </tr>
</table>