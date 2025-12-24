---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.05
tokens: 8365
characters: 1716
timestamp: 2025-12-24T00:34:09.371603
finish_reason: stop
---

else:
    print 'You clicked on', result, sels[0]
    dialog.deactivate(result)

dialog = Pmw.SelectionDialog(root, title='String',
    buttons=('OK', 'Cancel'), defaultbutton='OK',
    scrolledlist_labelpos=N, label_text='Who sells string?',
    scrolledlist_items=('Mousebat', 'Follicle', 'Goosecreature',
        'Mr. Simpson', 'Ampersand', 'Spong', 'Wapcaplet',
        'Looseliver', 'Vendetta', 'Prang'),
    command=execute)
dialog.activate()

Documentation for the SelectionDialog widget starts on page 603.

4.3.28 TextDialog

The TextDialog widget provides a convenience dialog used to display multi-line text to the user. It may also be used as a simple text editor. It is shown in figure 4.50.

![Screenshot of a TextDialog window showing a multi-line text box with a list of doctor-patient interactions](./images/fig_4_50.png)

Figure 4.50 Pmw TextDialog widget

sketch = """Doctor: Mr. Bertenshaw?
Mr. B: Me, Doctor.
Doctor: No, me doctor, you Mr. Bertenshaw.
Mr. B: My wife, doctor...
Doctor: No, your wife patient.
Sister: Come with me, please.
Mr. B: Me, Sister?
Doctor: No, she Sister, me doctor, you Mr. Bertenshaw.
Nurse: Dr. Walters?
Doctor: Me, nurse...You Mr. Bertenshaw, she Sister, you doctor.
Sister: No, doctor.
Doctor: No doctor: call ambulance, keep warm.
Nurse: Drink, doctor?
Doctor: Drink doctor, eat Sister, cook Mr. Bertenshaw, nurse me!
Nurse: You, doctor?
Doctor: ME doctor!! You Mr. Bertenshaw. She Sister!
Mr. B: But my wife, nurse...
Doctor: Your wife not nurse. She nurse, your wife patient. Be patient,
    she nurse your wife. Me doctor, you tent, you tree, you Tarzan, me
    Jane, you Trent, you Trillo...me doctor!

dialog = Pmw.TextDialog(root, scrolledtext_labelpos='n',