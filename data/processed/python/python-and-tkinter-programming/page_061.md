---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.84
tokens: 8376
characters: 2124
timestamp: 2025-12-24T00:33:02.211683
finish_reason: stop
---

4.1.4 Button

Strictly, buttons are labels that react to mouse and keyboard events. You bind a method call or callback that is invoked when the button is activated. Buttons may be disabled to prevent the user from activating a button. Button widgets can contain text (which can span multiple lines) or images. Buttons can be in the tab group, which means that you can navigate to them using the TAB key. Simple buttons are illustrated in figure 4.6.

Figure 4.6 Button widgets

Label(root, text="You shot him!").pack(pady=10)
Button(root, text="He's dead!", state=DISABLED).pack(side=LEFT)
Button(root, text="He's completely dead!",
    command=root.quit).pack(side=RIGHT)

Not all GUI programmers are aware that the relief option may be used to create buttons with different appearances. In particular, FLAT and SOLID reliefs are useful for creating toolbars where icons are used to convey functional information. However, some care must be exercised when using some relief effects. For example, if you define a button with a SUNKEN relief, the widget will not have a different appearance when it is activated, since the default behavior is to show the button with a SUNKEN relief; alternative actions must be devised such as changing the background color, font or wording within the button. Figure 4.7 illustrates the effect of combining the available relief types with increasing borderwidth. Note that increased borderwidth can be effective for some relief types (and RIDGE and GROOVE don’t work unless borderwidth is 2 or more). However, buttons tend to become ugly if the borderwidth is too great.

Figure 4.7 Combining relief and varying borderwidth

class GUI:
    def __init__(self):
        of = [None] *5
        for bdw in range(5):
            of[bdw] = Frame(self.root, borderwidth=0)
            Label(of[bdw], text='borderwidth = %d' % bdw).pack(side=LEFT)
            for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
                Button(of[bdw], text=relief,
                    borderwidth=bdw, relief=relief, width=10,
                    command=lambda s=self, r=relief, b=bdw: s.prt(r,b))\