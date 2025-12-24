---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.50
tokens: 8351
characters: 1753
timestamp: 2025-12-24T00:37:03.563208
finish_reason: stop
---

```python
appname = 'Image Browser'
def createButtons(self):
    self.buttonAdd('Ok',
        helpMessage='Exit',
        statusMessage='Exit',
        command=self.quit)

def createMain(self):
    self.panes = self.createcomponent('panes', (), None,
        Pmw.PanedWidget,
        (self.interior(),),
        orient='horizontal')
    self.panes.add('browserpane', min=150, size=160)
    self.panes.add('displaypane', min=.1)

    f = os.path.join(path, 'folder.gif')
    of = os.path.join(path, 'openfolder.gif')
    self.browser = self.createcomponent('browse', (), None,
        Tree,
        (self.panes.pane('browserpane'),),
        icon=f,
        openicon=of,
        treename='Multimedia',
        action=None)
    self.browser.pack(side=TOP, expand=YES, fill=Y)

    self.datasite = self.createcomponent('datasite', (), None,
        Frame,
        (self.panes.pane('displaypane'),))

    self.datasite.pack(side=TOP, expand=YES, fill=BOTH)

    f = os.path.join(path, 'folder.gif')
    of = os.path.join(path, 'openfolder.gif')
    gf = os.path.join(path, 'gif.gif')
    jf = os.path.join(path, 'jpg.gif')
    xf = os.path.join(path, 'other.gif')

    self.browser.inhibitDraw = 1

    top=self.browser.child[0]
    top.state='expanded'
    jpeg=top.addChild(self.browser, icon=f, openicon=of,
        name='Jpeg',action=None)
    gif=top.addChild(self.browser, icon=f, openicon=of,
        name='GIF', action=None)
    other=top.addChild(self.browser, icon=f, openicon=of,
        name='Other', action=None)

    imageDir = {'.jpg': (jpeg, jf), '.jpeg': (jpeg, jf),
        '.gif': (gif, gf), '.bmp': (other, xf),
        '.ppm': (other, xf)}

    files = os.listdir(imgs)
    for file in files:
        r, ext = os.path.splitext(file)
```