---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.31
tokens: 8144
characters: 2374
timestamp: 2025-12-24T04:42:07.891794
finish_reason: stop
---

hello->gtk_window_new(0, 0x7f294f2493a0, 0, 0x7f294f2493a0) = 0x55d553e24520
hello->gtk_vbox_new(1, 0, 1, 0) = 0x55d553faa180
hello->gtk_container_get_type(0x55d553f07f20, 1, 0x55d553f07f20, 0) = 0x55d553e4d8a0
hello->gtk_container_add(0x55d553e24520, 0x55d553faa180, 0x55d553e24520, 3) = 0x55d553e6b0a0
hello->gtk_label_new(0x55d55301cc84, 0x55d553faa180, 1, 0) = 0x55d5540d0210
hello->gtk_container_get_type(0x55d5540d0220, 80, 1, 0) = 0x55d553e4d8a0
hello->gtk_container_add(0x55d553faa180, 0x55d5540d0210, 0x55d553faa180, 3) = 0x55d553e6b0a0
hello->gtk_button_new_with_label(0x55d55301cc92, 0x55d5540d0210, 1, 0) = 0x55d5540d1180
hello->gtk_container_get_type(0x55d553f22bb0, 0x55d553ddd010, 0x55d553f22bb0, 0) = 0x55d553e4d8a0
hello->gtk_container_add(0x55d553faa180, 0x55d5540d1180, 0x55d553faa180, 3) = 0x55d553e6b0a0
hello->gtk_widget_show_all(0x55d553e24520, 1, 212, 0

[1406978,365] -> wl_compositor@4.create_surface(new id wl_surface@27)
[1406978,599] -> wl_surface@27.set_buffer_scale(1)
[1406979,800] -> xdg_wm_base@21.get_xdg_surface(new id xdg_surface@28, wl_surface@27)
[1406979,881] -> wl_surface@27.commit()
) = 2
hello->gtk_main(0x55d553e24530, 80, 1, 0
[1406997,924] xdg_surface@28.configure(106556)
[1406997,959] -> xdg_surface@28.ack_configure(106556)
[1407014,540] -> wl_shm@5.create_pool(new id wl_shm_pool@31, fd 13, 272800)
[1407014,580] -> wl_shm_pool@31.create_buffer(new id wl_buffer@32, 0, 275, 248, 1100, 0)
[1407018,097] -> wl_surface@27.attach(wl_buffer@32, 0, 0)
[1407018,131] -> wl_surface@27.set_buffer_scale(1)
[1407018,140] -> wl_surface@27.damage(0, 0, 275, 248)
[1407018,293] -> wl_surface@27.frame(new id wl_callback@35)
[1407018,303] -> wl_surface@27.commit()
<unfinished ...>
hello->gtk_main_quit(0x55d5540d1180, 0, 0, 0) = 0
<... gtk_main resumed> ) = 0x55d553dde280
+++ exited (status 0) +++

Wayland-взаимодействие с композитором начинается с подключения к нему и получения «дисплея» wl_display (на трассе не показано). Затем при помощи его метода get_registry() извлекается реестр глобальных интерфейсов ①, в котором зарегистрированы интерфейсы wl_compositor ①, wl_shm ②, wl_seat ③ и др. На события всех этих интерфейсов производится подписка при помощи метода bind() реестра, а затем у дисплея запрашивается ② доставка события «синхронизация», которое доставляется в момент, когда нет больше других событий в очереди доставки.