---
source_image: page_339.png
page_number: 339
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.29
tokens: 7919
characters: 2568
timestamp: 2025-12-24T04:42:10.918435
finish_reason: stop
---

Графическая система Wayland

[2890482.729] wl_drm@10.device("/dev/dri/card0")
ioctl(5, DRM_IOCTL_GET_MAGIC, 0x7ffe85f71eb4) = 0
[2890483.635] -> wl_drm@10.authenticate(16)
    ...        ...        ...        ...
ioctl(5, DRM_IOCTL_VERSION, 0x55acc6ed9a20) = 0
ioctl(5, DRM_IOCTL_VERSION, 0x55acc6ed9a20) = 0
strace: Process 13734 attached
[pid 13733] ioctl(5, DRM_IOCTL_I915_GEM_CREATE, 0x7ffe85f71a40) = 0
    ...        ...        ...        ...
[pid 13733] ioctl(5, DRM_IOCTL_I915_GEM_MMAP, 0x7ffe85f71a80) = 0
    ...        ...        ...        ...
[2890542.462] -> wl_compositor@4.create_surface(new id wl_surface@9)
    ...        ...        ...        ...
[2890572.504] -> zwp_linux_dmabuf_v1@11.create_params(new id zwp_linux_buffer_params_v1@18)
[pid 13733] ioctl(5, DRM_IOCTL_PRIME_HANDLE_TO_FD, 0x7ffe85f7223c) = 0
[2890572.853] -> zwp_linux_buffer_params_v1@18.add(fd 8, 0, 0, 1024, 16777216, 2)
[2890573.500] -> zwp_linux_buffer_params_v1@18.create_inmem(new id wl_buffer@19, 250, 250, ..., 0)
[2890573.928] -> zwp_linux_buffer_params_v1@18.destroy()
[2890574.009] -> wl_surface@9.attach(wl_buffer@19, 0, 0)
[2890574.299] -> wl_surface@9.damage(0, 0, 2147483647, 2147483647)
[pid 13733] ioctl(5, DRM_IOCTL_I915_GEM_EXECBUFFER2, 0x7ffe85f722a0) = 0
[pid 13733] ioctl(5, DRM_IOCTL_I915_GEM_WAIT or DRM_IOCTL_RADEON_GEM_OP, 0x7ffe85f72230) = 0
[pid 13733] ioctl(5, DRM_IOCTL_I915_GEM_BUSY, 0x7ffe85f720f0) = 0
[2890575.166] -> wl_surface@9.commit()

После обычного разбора реестра глобальных интерфейсов ① и подписки на нужные интерфейсы ① и ②, при получении события ③ доступности файла «устройства» DRM производится подключение ② к нему. Затем при помощи уже известного (по листингу 7.40) ioctl-интерфейса к DRM ③ создаются буферы в памяти видеоускорителя и отображаются в память процесса Wayland-клиента. После чего создается «поверхность» ④ для отображения, DRM-буфер с результатом будущего рендеринга ⑤ превращается в файловый дескриптор fd = 8, на основе которого создается wl_buffer ⑥ и уже известным способом присоединяется к «поверхности» ⑦. На последнем этапе при помощи DRM задействуется ⑧ GPU видеоускорителя, а затем полученный результат отрисовки поступает композитору на отображение ⑨.

8.3. Запуск графической среды на основе Wayland

За долгое время развития оконной системы X сложилась устоявшаяся инфраструктура запуска ее компонент и обеспечения графического входа пользователей в систему на основе так называемого менеджера дисплеев (см. разд. 7.3.3). Вместе с тем, как было показано выше, Wayland-композитор является всего лишь совре-