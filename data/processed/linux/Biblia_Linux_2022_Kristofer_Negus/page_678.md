---
source_image: page_678.png
page_number: 678
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.39
tokens: 7414
characters: 1429
timestamp: 2025-12-24T05:04:13.069008
finish_reason: stop
---

1) tspi
2) passphrase
3) pkcs11-helper
4) openssl
Selection: 2
Passphrase: ***********
Select cipher:
1) aes: blocksize = 16;
min keysizes = 16; max keysize = 32 (loaded)
2) blowfish: blocksize = 16;
min keysizes = 16; max keysize = 56 (not loaded)
3) des3_ede: blocksize = 8;
min keysizes = 24; max keysize = 24 (not loaded)
4) twofish: blocksize = 16;
min keysizes = 16; max keysize = 32 (not loaded)
5) cast6: blocksize = 16;
min keysizes = 16; max keysize = 32 (not loaded)
6) cast5: blocksize = 8;
min keysizes = 5; max keysize = 16 (not loaded)
Selection [aes]: 1
Select key bytes:
1) 16
2) 32
3) 24
Selection [16]: 16
Enable plaintext passthrough (y/n) [n]: n
Enable filename encryption (y/n) [n]: n
Attempting to mount with the following options:
ecryptfs_unlink_sigs
ecryptfs_key_bytes=16
ecryptfs_cipher=aes
ecryptfs_sig=70993b8d49610e67
WARNING: Based on the contents of [/root/.ecryptfs/sig-cache.txt]
it looks like you have never mounted with this key before. This could mean that you have typed your passphrase wrong.

Would you like to proceed with the mount (yes/no)? : yes
Would you like to append sig [70993b8d49610e67] to [/root/.ecryptfs/sig-cache.txt]
in order to avoid this warning in the future (yes/no)? : yes
Successfully appended new sig to user sig cache file
Mounted eCryptfs

Утилита ecryptfs позволяет:

• выбрать тип ключа;
• задать кодовую фразу;
• выбрать шифр;
• указать размер ключа (в байтах);