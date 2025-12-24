---
source_image: page_207.png
page_number: 207
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.99
tokens: 8353
characters: 1926
timestamp: 2025-12-24T00:37:09.481504
finish_reason: stop
---

cont, icon = imageDir.get(ext, (None, None))
if cont:
    cont.addChild(self.browser, icon=icon,
        name=file, action=self.showMe)
self.browser.inhibitDraw = 0
self.browser.display()
self.panes.pack(side=TOP, expand=YES, fill=BOTH)

def createImageDisplay(self):
    self.imageDisplay = self.createcomponent('image', (), None,
        Label,
        (self.datasite,))
    self.browser.imageLabel = self.imageDisplay
    self.browser.imageData= None
    self.imageDisplay.place(relx=0.5, rely=0.5, anchor=CENTER)

def createInterface(self):
    AppShell.AppShell.createInterface(self)
    self.createButtons()
    self.createMain()
    self.createImageDisplay()

def showMe(self, dofile):
    if self.browser.imageData: del self.browser.imageData
    self.browser.imageData = ImageTk.PhotoImage(\ 
        Image.open('%s%s' % \
            (imgs, dofile)))
    self.browser.imageLabel['image'] = self.browser.imageData

if __name__ == '__main__':
    imageBrowser = ImageBrowser()
    imageBrowser.run()

Code comments (continued)
14 We define all of the icons that may be displayed for each file type:
    f   = os.path.join(path, 'folder.gif')
    of = os.path.join(path, 'openfolder.gif')
    gf = os.path.join(path, 'gif.gif')
    jf = os.path.join(path, 'jpg.gif')
    xf = os.path.join(path, 'other.gif')

15 Now the root of the tree is created and we populate the root with the supported image types:
    top=self.browser.child[0]
    top.state='expanded'
    jpeg=top.addChild(self.browser, icon=f, openicon=of,
        name='Jpeg',action=None)
    ...

16 We create a dictionary to provide translation from file extensions to an appropriate image type and icon (dictionaries are an efficient way of determining properties of an object which have varied processing requirements).
    imageDir = { '.jpg': (jpeg, jf), '.jpeg': (jpeg, jf),
        '.gif': (gif, gf), '.bmp': (other, xf),
        '.ppm': (other, xf)}