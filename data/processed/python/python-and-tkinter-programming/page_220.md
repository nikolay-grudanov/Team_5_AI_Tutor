---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.66
tokens: 8386
characters: 1912
timestamp: 2025-12-24T00:37:34.082164
finish_reason: stop
---

7 Once the map ID has been entered, clicking the Add button adds the ID and the map coordinates to the list of map entries:

def addMap(self):
    self.coordinatedata.append(self.reference.get(),
        self.startx, self.starty,
        self.endx, self.endy)

8 When the Build button is pressed, we generate a Python file to test the image map:

def buildMap(self):
    filename = os.path.splitext(self.file)[0]
    ofd = open('%s.py' % filename, 'w')

9 The first section of the code is boilerplate, so it can be read in from a file:

ifd = open('image1.inp', 'r')
lines = ifd.readlines()
ifd.close()
ofd.writelines(lines)

10 Then we generate an entry for each map collected previously:

for ref, sx,sy, ex,ey in self.coordinatedata:
    ofd.write("    self.iMap.addRegion(((%5.1f,%5.1f),"
        "(%5.1f,%5.1f)), '%s')\n" % (sx,sy, ex,ey, ref))

11 Finally, we add some code to launch the image map:

ofd.write('\n%s\n' % ('#' * 70))
ofd.write('if __name__ == "__main__":\n')
ofd.write('    root = Tk()\n')
ofd.write('    root.title("%s")\n' % self.file)
ofd.write('    imageTest = ImageTest(root, width=%d, height=%d, '
    'file="%s")\n' % (self.width, self.height, self.file))
ofd.write('    imageTest.root.mainloop()\n')
ofd.close()

All you have to do is supply a GIF file and then drag the selection rectangle around each of the target regions. Give the region an identity and click the Add button. When you have identified all of the regions, click the Build button.

Note This example illustrates how Python can be used to generate code from input data. Python is so easy to use and debug that it can be a valuable tool in building complex systems. If you take a little time to understand the structure of the target code, you can write a program to generate that code. Of course, this only works if you have to produce lots of replicated code segments, but it can save you a lot of time and effort!