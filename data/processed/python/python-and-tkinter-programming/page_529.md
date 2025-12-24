---
source_image: page_529.png
page_number: 529
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.05
tokens: 8375
characters: 2532
timestamp: 2025-12-24T00:46:46.913234
finish_reason: stop
---

entrycget(index, option)
Returns the current value of a configuration option for the entry given by index. option may have any of the values accepted by the add method.

entryconfigure(index, options...)
This method is similar to the configure command, except that it applies to the options for an individual entry index, whereas configure applies to the options for the menu as a whole. options may have any of the values accepted by the add widget method. If options are specified, options are modified as indicated in the method and the method returns None. If no options are specified, it returns a list describing the current options for entry index.

index(index)
Returns the numerical index corresponding to index, or None if index was specified as None.

insert_cascade(index, options...)
Same as the add method except that it inserts the new cascade entry just before the entry given by index, instead of appending to the end of the menu. options arguments have the same interpretation as for the add method. It is not possible to insert new menu entries before the tear-off entry, if the menu has one.

insert_checkbutton(index, options...)
Same as the add method except that it inserts the new checkbutton entry just before the entry given by index, instead of appending to the end of the menu. options arguments have the same interpretation as for the add method. It is not possible to insert new menu entries before the tear-off entry, if the menu has one.

insert_command(index, options...)
Same as the add method except that it inserts the new command entry just before the entry given by index, instead of appending to the end of the menu. options arguments have the same interpretation as for the add method. It is not possible to insert new menu entries before the tear-off entry, if the menu has one.

insert_radiobutton(index, options...)
Same as the add method except that it inserts the new radiobutton entry just before the entry given by index, instead of appending to the end of the menu. options arguments have the same interpretation as for the add method. It is not possible to insert new menu entries before the tear-off entry, if the menu has one.)

insert_separator(index, options...)
Same as the add method except that it inserts the new separator entry just before the entry given by index, instead of appending to the end of the menu. options arguments have the same interpretation as for the add method. It is not possible to insert new menu entries before the tear-off entry, if the menu has one.