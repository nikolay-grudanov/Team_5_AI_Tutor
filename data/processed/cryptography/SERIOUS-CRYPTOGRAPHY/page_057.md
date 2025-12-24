---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.61
tokens: 7374
characters: 1394
timestamp: 2025-12-24T09:11:14.474559
finish_reason: stop
---

Более безопасный способ работы с /dev/urandom

В листинге 2.2, скопированном из библиотеки LibreSSL, показано более безопасное использование /dev/urandom.

Листинг 2.2. Безопасное использование /dev/urandom

int random_bytes_safer(void *buf, size_t len)
{
    struct stat st;
    size_t i;
    int fd, cnt, flags;
    int save_errno = errno;

    start:
        flags = O_RDONLY;
#ifdef O_NOFOLLOW
        flags |= O_NOFOLLOW;
#endif
#ifdef O_CLOEXEC
        flags |= O_CLOEXEC;
#endif
        fd = open("/dev/urandom", flags, 0);
        if (fd == -1) {
            if (errno == EINTR)
                goto start;
            goto nodevrandom;
        }
#ifdef O_CLOEXEC
        fcntl(fd, F_SETFD, fcntl(fd, F_GETFD) | FD_CLOEXEC);
#endif

        /* Простая проверка разумного поведения устройства */
        if (fstat(fd, &st) == -1 || !S_ISCHR(st.st_mode)) {
            close(fd);
            goto nodevrandom;
        }
        if (ioctl(fd, RNDGETENTCNT, &cnt) == -1) {
            close(fd);
            goto nodevrandom;
        }
        for (i = 0; i < len; ) {
            size_t wanted = len - i;
            ssize_t ret = read(fd, (char *)buf + i, wanted);

            if (ret == -1) {
                if (errno == EAGAIN || errno == EINTR)
                    continue;
                close(fd);
                goto nodevrandom;
            }
            i += ret;
        }
}