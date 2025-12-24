---
source_image: page_359.png
page_number: 359
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.34
tokens: 7702
characters: 2566
timestamp: 2025-12-24T04:42:38.272622
finish_reason: stop
---

cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
    ...
    ...
    ...
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)

rick@ubuntu:~ $ ls /sys/fs/cgroup
cgroup.clone_children
docker
init.scope
memory.kmem.tcp.limit_in_bytes
memory.kmem.tcp.max_usage_in_bytes
memory.kmem.tcp.usage_in_bytes
memory.kmem.usage_in_bytes

memory.limit_in_bytes
memory.oom_control
memory.pressure_level
system.slice
tasks
user.slice

rick@ubuntu:~ $ find /sys/fs/cgroup/docker -type d
/sys/fs/cgroup/memory/docker/
/sys/fs/cgroup/memory/docker/d54bd8ab3100ca63041fe5780bc7095e2a0f6729df5e71d7c6474ac685bf5bc7

rick@ubuntu:~ $ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
d54bd8ab3100        ubuntu:16.04        "/bin/bash"         13 hours ago        Up 13 hours         0.0.0.0:22->22/tcp   c-123

rick@ubuntu:~ $ cd /sys/fs/cgroup/memory/docker/d54bd8ab3100ca6304...d7c6474ac685bf5bc7
rick@ubuntu:/sys/fs/.../d54b...5bc7$ ls
cgroup.clone_children
cgroup.event_control
memory.kmem.limit_in_bytes
memory.kmem.slabinfo
memory.kmem.tcp.failcnt
memory.kmem.tcp.limit_in_bytes
memory.kmem.tcp.max_usage_in_bytes
memory.kmem.tcp.usage_in_bytes
memory.kmem.usage_in_bytes
memory.limit_in_bytes
memory.max_usage_in_bytes
memory.soft_limit_in_bytes
memory.swappiness
memory.usage_in_bytes
memory.use_hierarchy
notify_on_release
tasks

rick@ubuntu:/sys/fs/.../d54b...5bc7$ cat tasks
22358

rick@ubuntu:/sys/fs/.../d54b...5bc7$ cat memory.limit_in_bytes memory.soft_limit_in_bytes
9223372036854771712
9223372036854771712

rick@ubuntu:/sys/fs/.../d54b...5bc7$ cat memory.usage_in_bytes
33243136

Из листинга видно, что в системе определены 11 иерархий групп процессов, каждой из которых назначено по одному (2), реже по два (1) контроллера. Подключение иерархии производится просто путем монтирования файловой системы cgroup (1) в какое-либо место дерева каталогов (по соглашению, в подкаталоги каталога /sys/fs/cgroup).

В самих иерархиях, например в /sys/fs/cgroup/memory, созданы группы с названиями docker (1), init.scope (1), system.slice (3) и init.slice (1). Группа docker и ее подгруппы