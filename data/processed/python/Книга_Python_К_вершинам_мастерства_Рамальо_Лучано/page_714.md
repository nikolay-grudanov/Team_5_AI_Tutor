---
source_image: page_714.png
page_number: 714
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.91
tokens: 11684
characters: 1943
timestamp: 2025-12-24T02:07:43.695070
finish_reason: stop
---

```python
else: # ok, we have one and only one id field
    if isis_json_type == 1:
        id = occurrences[0]
    elif isis_json_type == 2:
        id = occurrences[0][0][1]
    elif isis_json_type == 3:
        id = occurrences[0]['_']
    if id in ids:
        msg = 'duplicate id %s in tag #%s, record %s'
        if ISIS_MFN_KEY in record:
            msg = msg + (' (mfn=%s)' % record[ISIS_MFN_KEY])
            raise TypeError(msg % (id, id_tag, i))
        record['_id'] = id
        ids.add(id)
    elif gen_uuid:
        record['_id'] = unicode(uuid4())
    elif mfn:
        record['_id'] = record[ISIS_MFN_KEY]
    if prefix:
        # обходим фиксированную последовательность тегов
        for tag in tuple(record):
            if str(tag).isdigit():
                record[prefix+tag] = record[tag]
                del record[tag] # вот поэтому мы обходим кортеж с тегами, и не сам словарь record
    if constant:
        constant_key, constant_value = constant.split(':')
        record[constant_key] = constant_value
    output.write(json.dumps(record).encode('utf-8'))
    output.write('\n')
if not mongo:
    output.write(']\n')

def main(): # создаем анализатор
    parser = argparse.ArgumentParser(
        description='Convert an ISIS .mst or .iso file to a JSON array')
    # добавляем аргументы
    parser.add_argument(
        'file_name', metavar='INPUT.(mst|iso)',
        help='.mst or .iso file to read')
    parser.add_argument(
        '-o', '--out', type=argparse.FileType('w'), default=sys.stdout,
        metavar='OUTPUT.json',
        help='the file where the JSON output should be written'
        ' (default: write to stdout)')
    parser.add_argument(
        '-c', '--couch', action='store_true',
        help='output array within a "docs" item in a JSON document'
        ' for bulk insert to CouchDB via POST to db/_bulk_docs')
    parser.add_argument(
        '-m', '--mongo', action='store_true',
```