---
source_image: page_789.png
page_number: 789
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.40
tokens: 11598
characters: 1072
timestamp: 2025-12-24T03:50:48.695633
finish_reason: stop
---

$Log$
Текст, который был создан при добавлении файла для описания его изменений. Текст предваряется именем файла RCS, номером версии, именем автора и датой. Описания изменений накапливаются, а не перезаписываются.

$RCSfile$
Имя файла RCS (без пути к нему).

$Revision$
Присвоенный номер версии.

$Source$
Имя файла RCS, включая путь.

$State$
Состояние, установленное параметром -S команды ci или rcs.

Примеры значений

Допустим, файл /projects/new/chapter3 был добавлен и извлечен пользователем с именем daniel. Вот каким будет результат подстановки ключевых слов во второй по счету версии файла:

$Author: daniel $
$Date: 2000/02/25 18:21:10 $
$Header: /projects/new/chapter3,v 1.2 2000/02/25 18:21:10 daniel \
    Exp Locker: daniel $
$Id: chapter3,v 1.2 2000/02/25 18:21:10 daniel Exp Locker: daniel $
$Locker: daniel $
$Log: chapter3,v $
#Revision 1.2 2000/02/25 18:21:10 daniel
# Added section on error-handling
#
#Revision 1.1 2000/02/25 16:49:59 daniel
# Initial revision
#
$RCSfile: chapter3,v $
$Revision: 1.2 $
$Source: /project/new/chapter3,v $
$State: Exp $