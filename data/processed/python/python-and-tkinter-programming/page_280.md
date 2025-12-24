---
source_image: page_280.png
page_number: 280
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.60
tokens: 8552
characters: 1859
timestamp: 2025-12-24T00:39:20.293711
finish_reason: stop
---

"enough up or down so that it turns dim, it will be "
"deleted when you release the mouse button.",
    wraplength="5i", justify=LEFT).pack(side=TOP)
self.c1=Frame(master)
self.c1.pack(side=BOTTOM, fill=X, padx=2, pady=2)
Button(self.c1, text='Quit', command=master.quit).pack()
self.canvas = Canvas(master, width=width, height=height,
    relief=FLAT, borderwidth=2)
self.canvas.pack(side=TOP, fill=X)

c = self.canvas
self.grid   = '0.25c'
self.left   = c.winfo_fpixels('1c')
self.right  = c.winfo_fpixels('13c')
self.top    = c.winfo_fpixels('1c')
self.bottom = c.winfo_fpixels('1.5c')
self.size   = c.winfo_fpixels('.2c')
self.normalStyle   = 'black'
self.activeStyle   = 'green'
self.activeStipple = ''
self.deleteStyle   = 'red'
self.deleteStipple = 'gray25'

c.create_line('1c', '0.5c', '1c', '1c', '13c', '1c',
    '13c', '0.5c', width=1)
for i in range(12):
    x = i+1
    c.create_line('%dc'%x, '1c', '%dc'%x, '0.6c', width=1)
    c.create_line('%d.25c'%x, '1c', '%d.25c'%x,
        '0.8c', width=1)
    c.create_line('%d.5c'%x, '1c', '%d.5c'%x,
        '0.7c', width=1)
    c.create_line('%d.75c'%x, '1c', '%d.75c'%x,
        '0.8c', width=1)
    c.create_text('%d.15c'%x, '.75c', text=i, anchor=SW)

wellBorder = c.create_rectangle('13.2c', '1c', '13.8c',
    '0.5c', outline='black',
    fill=self.canvas['background'])
wellTab = self.mkTab(c.winfo_pixels('13.5c'),
    c.winfo_pixels('.65c'))
c.addtag_withtag('well', wellBorder)
c.addtag_withtag('well', wellTab)

c.tag_bind('well', '<1>',
    lambda e, s=self: s.newTab(e.x, e.y))
c.tag_bind('tab', '<1>',
    lambda e, s=self: s.selectTab(e.x, e.y))
c.bind('<B1-Motion>',
    lambda e, s=self: s.moveTab(e.x, e.y))
c.bind('<Any-ButtonRelease-1>', self.releaseTab)

def mkTab(self, x, y):
    return self.canvas.create_polygon(x, y, x+self.size,
        y+self.size, x-self.size, y+self.size)