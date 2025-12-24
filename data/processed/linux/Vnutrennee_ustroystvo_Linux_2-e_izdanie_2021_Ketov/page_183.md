---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.35
tokens: 7599
characters: 1578
timestamp: 2025-12-24T04:37:10.628542
finish_reason: stop
---

цы между ними, так и для последующей передачи самих данных различающихся файлов.

Листинг 4.53. Неименованные локальные (файловые) сокеты

fitz@ubuntu:~$ strace -fe socketpair,execve rsync -a /usr/share/doc /tmp/ execve("/usr/bin/rsync", ["rsync", "-a", "/usr/share/doc", "/tmp/"], ...) = 0
socketpair(AF_UNIX, SOCK_STREAM, 0, [3, 4]) = 0
socketpair(AF_UNIX, SOCK_STREAM, 0, [5, 6]) = 0
strace: Process 5268 attached
[pid 5268] socketpair(AF_UNIX, SOCK_STREAM, 0, [3, 4]) = 0
strace: Process 5269 attached
^Z
[1]+ Остановлен strace -fe socketpair,execve rsync -a /usr/share/doc /tmp/
fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
4838 pts/5 Ss 0:00 bash
5266 pts/5 T 0:00 \_ strace -fe socketpair execve rsync -a /usr/share/
5267 pts/5 t 0:00 \_ \_ rsync -a /usr/share/doc /tmp/
5268 pts/5 t 0:00 \_ \_ rsync -a /usr/share/doc /tmp/
5269 pts/5 t 0:00 \_ \_ rsync -a /usr/share/doc /tmp/
5301 pts/5 R+ 0:00 \_ ps f

fitz@ubuntu:~$ lsof -p 5269
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
rsync 5269 fitz cwd DIR 252,0 139264 26869761 /tmp
rsync 5269 fitz 0u unix 0x0000000000000000 0t0 1752340 type=STREAM
rsync 5269 fitz 4u unix 0x0000000000000000 0t0 1751443 type=STREAM

fitz@ubuntu:~$ lsof -p 5268
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
rsync 5268 fitz cwd DIR 252,0 139264 26869761 /tmp
rsync 5268 fitz 1u unix 0x0000000000000000 0t0 1752343 type=STREAM
rsync 5268 fitz 3u unix 0x0000000000000000 0t0 1751442 type=STREAM

fitz@ubuntu:~$ lsof -p 5267
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
rsync 5267 fitz cwd DIR 252,0 20480 3801093 /usr/share