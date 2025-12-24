---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.28
tokens: 7272
characters: 2379
timestamp: 2025-12-24T04:34:41.565216
finish_reason: stop
---

Absolutely naturally, it is reasonable to assume that the programs firefox(1) and skype(1) do not have any such intentions of access to user SSH keys. It can even be trusted program firefox(1), which was installed from a trusted source (distribution), where it was compiled from open source code, subject to verification. However, there are no grounds to trust the closed skype, delivered in binary form.

More than that, providing access to programs firefox(1) and skype(1) to SSH keys of the user is not necessary, first of all, simply because this goes beyond the minimum requirements for their normal functioning. Secondly, practically in any program there are errors, using which an attacker can perform unintended actions in its own interest. Such actions are especially vulnerable to programs, using network communication with an untrusted external environment — clients and servers of network services of the operating system. At the same time, discretionary approach and mechanisms serve for the distinction of access of different users to files, but are not designed for the distinction of access of programs of one and the same user to different files.

For the distinction of access of subjects — programs to objects — files of the file system catalogs use so-called mandatory (from the English mandatory — mandatory or compulsory) approach (MAC, mandatory access control), which assumes following mandatory rules of access to files, assigned by administrators of the system. Access rules are based on knowledge of the internal structure of programs and represent themselves as a description of the minimum requirements for their normal functioning.

Thus, in mandatory rules, restricting access to SSH keys of the user, only the program ssh(1) should be allowed access for direct execution of its own functions, while programs firefox(1) and skype(1) in access to SSH keys should be denied.

3.6.1. Модуль принудительного разграничения доступа AppArmor

In Linux mandatory mechanisms of access distinction are additional and are activated at the request of the user or distributor. For example, in Ubuntu Linux by default is installed and enabled module of mandatory access distinction apparmor(7). Module W:[AppArmor] has some number of profiles ready for use (called profiles) for limiting (confine) access of subjects — programs to objects of the operating system