---
source_image: page_437.png
page_number: 437
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.26
tokens: 7366
characters: 1612
timestamp: 2025-12-24T08:57:00.939680
finish_reason: stop
---

```python
print('Calculating d that is mod inverse of e...')
d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
publicKey = (n, e)
privateKey = (n, d)
print('Public key:', publicKey)
print('Private key:', privateKey)
return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
    # Создает два файла, 'x_pubkey.txt' и 'x_privkey.txt' (где x - значение параметра name), записывая в них целые числа keySize, n и e, разделенные запятыми.
    # Проверка, предотвращающая перезапись старых файлов ключей
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and rerun this program.' % (name, name))
    publicKey, privateKey = generateKey(keySize)
    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    print()
    print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()

# Если файл makePublicPrivateKeys.py выполняется как программа (а не импортируется как модуль), вызвать функцию main()
if __name__ == '__main__':
    main()
```