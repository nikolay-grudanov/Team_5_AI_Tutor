---
source_image: page_712.png
page_number: 712
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.66
tokens: 11624
characters: 2082
timestamp: 2025-12-24T02:07:28.327754
finish_reason: stop
---

ISIS_MFN_KEY = 'mfn'
ISIS_ACTIVE_KEY = 'active'
SUBFIELD_DELIMITER = '^'
INPUT_ENCODING = 'cp1252'

def iter_iso_records(iso_file_name, isis_json_type):
    from iso2709 import IsoFile
    from subfield import expand

    iso = IsoFile(iso_file_name)
    for record in iso:
        fields = {}
        for field in record.directory:
            field_key = str(int(field.tag)) # удалить начальные пробелы
            field_occurrences = fields.setdefault(field_key, [])
            content = field.value.decode(INPUT_ENCODING, 'replace')
            if isis_json_type == 1:
                field_occurrences.append(content)
            elif isis_json_type == 2:
                field_occurrences.append(expand(content))
            elif isis_json_type == 3:
                field_occurrences.append(dict(expand(content)))
        else:
            raise NotImplementedError('ISIS-JSON type %s conversion ' %
                                      'not yet implemented for .iso input' % isis_json_type)
        yield fields
    iso.close()

def iter_mst_records(master_file_name, isis_json_type):
    try:
        from bruma.master import MasterFactory, Record
    except ImportError:
        print('IMPORT ERROR: Jython 2.5 and Bruma.jar ' \
              'are required to read .mst files')
        raise SystemExit
    mst = MasterFactory.getInstance(master_file_name).open()
    for record in mst:
        fields = {}
        if SKIP_INACTIVE:
            if record.getStatus() != Record.Status.ACTIVE:
                continue
        else: # сохранить состояние, только если есть неактивные записи
            fields[ISIS_ACTIVE_KEY] = (record.getStatus() == Record.Status.ACTIVE)
            fields[ISIS_MFN_KEY] = record.getMfn()
            for field in record.getFields():
                field_key = str(field.getId())
                field_occurrences = fields.setdefault(field_key, [])
                if isis_json_type == 3:
                    content = {}
                    for subfield in field.getSubfields():
                        subfield_key = subfield.getId()