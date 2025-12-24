---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.34
tokens: 8493
characters: 2417
timestamp: 2025-12-24T00:37:03.400888
finish_reason: stop
---

3 Rather than use the default megawidget interior, we create our own form component:

def createForm(self):
    self.form = self.createcomponent('form', (), None,
        Frame, (self.interior(),),)
    self.form.pack(side=TOP, expand=YES, fill=BOTH)
    self.formwidth = self.root.winfo_width()

4 We extract the data from the selected data dictionary element and initialize data structures:

def createFields(self):
    self.table, self.top, self.anchor, self.incr, self.fields, \
        self.title, self.keylist = dataDict[self.dictionary]
    self.records= []
    self.dirty= FALSE

5 This example does not interface with any database, but we still need to create a single empty record even for this case. We create one empty entry for each field:

    self.ypos = self.top
    self.recrows = len(self.records)
    if self.recrows < 1: # Create one!
        self.recrows = 1
        trec = []
        for i in range(len(self.fields)):
            trec.append(None)
        self.records.append((trec))

6 Although we are not going to be able to save any information input to the form, we still define markers at the left- and right-bottom of the screen to indicate when a record has been modified or added:

    Label(self.form, text=self.title, width=self.formwidth-4,
        bd=0).place(relx=0.5, rely=0.025, anchor=CENTER)
    self.lmarker = Label(self.form, text="", bd=0, width=10)
    self.lmarker.place(relx=0.02, rely=0.99, anchor=SW)
    self.rmarker = Label(self.form, text="", bd=0, width=10)
    self.rmarker.place(relx=0.99, rely=0.99, anchor=SE)

7 This is where we create the label/field pairs which make up our interface. We give the user a visual clue that a field is the key by increasing the highlight thickness:

    for label, field, width, proc, valid, nonblank in self.fields:
        pstr = 'Label(self.form,text="%s").place(relx=%f,rely=%f,\n' % (label, (self.anchor-0.02), self.ypos)
        if idx == self.keylist[0]:
            pstr = '%ssself.%s=Entry(self.form,text="",\n' % (pstr,field,width)
            'insertbackground="yellow", width=%d+1,\n' % (pstr,field,width)
        else:
            ...

Note In this application we have chosen to use highlightthickness to provide a visual clue to the user that the field contains the key to the data. You might choose one of several other methods to get this effect, such as changing the background color or changing the borderwidth.