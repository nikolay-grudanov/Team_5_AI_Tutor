---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.15
tokens: 7532
characters: 1799
timestamp: 2025-12-24T04:53:06.734414
finish_reason: stop
---

тит, что изменений не требуется. Вместо этого примените подкоманду reinstall. Предположим, вы установили пакет zsh, а затем случайно удалили файл /bin/zsh. Недостающие компоненты можно восстановить, набрав следующее:

# yum reinstall zsh

Можно удалить пакет вместе с его зависимостями, которые не требуются другим пакетам, с помощью подкоманды remove. Например, чтобы удалить пакет emacs и его зависимости, введите:

# yum remove emacs
Removing:
emacs        x86_64   1:26.2-1.fc30   updates   38 M
Removing unused dependencies:
ImageMagick-libs    x86_64   1:6.9.10.28-1.fc30   fedora   8.9 M
emacs-common        x86_64   1:26.2-1.fc30   updates   89 M
fftw-libs-double    x86_64   3.3.8-4.fc30   fedora   4.2 M
...
Transaction Summary
Remove  7 Packages
Freed space: 142 M
Is this ok [y/N]: y

Обратите внимание на то, что используемая память, указанная для каждого пакета, является фактической (именно столько места пакет занимает в файловой системе), а не размером, указанным при загрузке (он значительно меньше).

Еще один способ удалить набор установленных пакетов — подкоманда history. С ее помощью можно увидеть все действия команд yum и отменить все транзакции. Другими словами, все установленные пакеты можно удалить, применив параметр undo подкоманды history, как показано в следующем примере:

# yum history
ID | Command line | Date and time | Action(s) | Altered
-----------------------------|----------------|----------------|------------|-------------
12 | install emacs | 2019-06-22 11:14 | Install | 7
...
# yum history info 12
Transaction ID : 12
...
Command Line    : install emacs
...
# yum history undo 12
Undoing transaction 12, from Sat 22 Jun 2019 11:14:42 AM EDT

Install emacs-1:26.2-1.fc30.x86_64      @updates
    Install emacs-common-1:26.2-1.fc30.x86_64   @updates
...