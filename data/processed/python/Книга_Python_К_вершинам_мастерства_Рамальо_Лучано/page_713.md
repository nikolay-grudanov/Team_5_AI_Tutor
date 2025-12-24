---
source_image: page_713.png
page_number: 713
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.53
tokens: 11641
characters: 2023
timestamp: 2025-12-24T02:07:31.806366
finish_reason: stop
---

Глава 14: скрипт преобразования базы данных isis2json.py

if subfield_key == '*':
    content['_'] = subfield.getContent()
else:
    subfield_occurrences = content.setdefault(subfield_key, [])
    subfield_occurrences.append(subfield.getContent())
    field_occurrences.append(content)
elif isis_json_type == 1:
    content = []
    for subfield in field.getSubfields():
        subfield_key = subfield.getId()
        if subfield_key == '*':
            content.insert(0, subfield.getContent())
        else:
            content.append(SUBFIELD_DELIMITER + subfield_key +
                           subfield.getContent())
    field_occurrences.append(''.join(content))
else:
    raise NotImplementedError('ISIS-JSON type %s conversion ' +
                             'not yet implemented for .mst input' % isis_json_type)
yield fields
mst.close()

def write_json(input_gen, file_name, output, qty, skip, id_tag,
               gen_uuid, mongo, mfn, isis_json_type, prefix,
               constant):
    start = skip
    end = start + qty
    if id_tag:
        id_tag = str(id_tag)
        ids = set()
    else:
        id_tag = ''
    for i, record in enumerate(input_gen):
        if i >= end:
            break
        if not mongo:
            if i == 0:
                output.write('[')
            elif i > start:
                output.write(',')
        if start <= i < end:
            if id_tag:
                occurrences = record.get(id_tag, None)
                if occurrences is None:
                    msg = 'id tag #%s not found in record %s'
                    if ISIS_MFN_KEY in record:
                        msg = msg + (' (mfn=%s)' % record[ISIS_MFN_KEY])
                    raise KeyError(msg % (id_tag, i))
                if len(occurrences) > 1:
                    msg = 'multiple id tags #%s found in record %s'
                    if ISIS_MFN_KEY in record:
                        msg = msg + (' (mfn=%s)' % record[ISIS_MFN_KEY])
                    raise TypeError(msg % (id_tag, i))