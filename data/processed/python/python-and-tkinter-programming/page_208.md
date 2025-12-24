---
source_image: page_208.png
page_number: 208
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.29
tokens: 8135
characters: 1142
timestamp: 2025-12-24T00:36:52.275570
finish_reason: stop
---

17 We scan the disk, finding all files with recognizable extensions and add the nodes to the tree:

    files = os.listdir(imgs)
    for file in files:
        r, ext = os.path.splitext(file)
        cont, icon = imageDir.get(ext, (None, None))
        if cont:
            cont.addChild(self.browser, icon=icon,
                name=file, action=self.showMe)

This code would probably be a little more complex in reality; I can see a couple of potential problems as I’m writing this (I could write “I leave this as an exercise for you to identify problems with this code”).

18 Once the tree has been built, we reset the inhibitDraw flag and display the tree:

    self.browser.inhibitDraw = 0
    self.browser.display()

That probably seems like a lot of code, but the resulting browser provides a highly-acceptable interface. In addition, users will understand the interface’s navigation and it is readily adaptable to a wide range of data models.

Running Example_8_10.py (with a Python built with PIL) will display a screen similar to the one in figure 8.11.

![Image browser screenshot](../images/fig8_11.png)

Figure 8.11 Image browser