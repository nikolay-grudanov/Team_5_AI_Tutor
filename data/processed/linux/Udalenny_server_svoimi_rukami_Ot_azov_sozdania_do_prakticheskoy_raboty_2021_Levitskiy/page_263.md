---
source_image: page_263.png
page_number: 263
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.77
tokens: 6366
characters: 1381
timestamp: 2025-12-24T04:01:55.575220
finish_reason: stop
---

1. Общие. К общим директивам относятся глобальные директивы, влияющие на работу всего Web-сервера. Это директивы ServerName, ServerType, Port, User и Group, ServerAdmin, ServerRoot, PidFile, DocumentRoot, UserDir.

2. Директивы протоколирования: ErrorLog, TransferLog, HostnameLookups.

3. Директивы ограничения доступа: AllowOverride, Options, Limit.

4. Директивы управления производительностью: StartServers, MaxSpareServers, MinSpareServers, а также директива CacheNegotiatedDocs.

5. Директивы обеспечения постоянного соединения с клиентом: Timeout, KeepAlive, KeepAliveTimeout.

6. Директивы настройки отображения каталога. Оформить отображение каталогов можно с помощью директив настройки отображения каталогов: DirectoryIndex, FancyIndexing и AddIconByType.

7. Директивы обработки ошибок. Директивой обработки ошибок HTTP-сервера является директива ErrorDocument. С ее помощью можно установить реакцию на любую ошибку сервера, например, на ошибку 404 (документ не найден).

8. Директивы перенаправления: Redirect, Alias и ScriptAlias.

9. Директивы для работы с многоязычными документами: AddLanguage и LanguagePriority.

10. Директивы обработки MIME-типов. Настроить свой сервер для обработки различных MIME-типов можно с помощью директив DefaultType, AddEncoding, AddType, AddHandler и Action.

11. Директивы создания виртуальных узлов: VirtualHost, Listen, BindAddress.