---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.06
tokens: 8272
characters: 1710
timestamp: 2025-12-24T00:35:48.067118
finish_reason: stop
---

(NUT_FLAT,1, STATUS_ON,   MODE_US),
(NUT_FLAT,0, STATUS_ON,   MODE_UK),
(NUT_POINT, 0, STATUS_OFF, MODE_UK)]
    # Iterate for each metal type
    for metal in metals:
        mframe = Frame(self, bg="slategray2")
        mframe.pack(anchor=N, expand=YES, fill=X)
        # Iterate for each of the switches
        for top, mount, state, mode in switches:
            ToggleSwitch(mframe,
                mount=mount, outside=20,
                nutbase=metal, mode=mode,
                bg="slategray2", top=top,
                status=state).frame.pack(side=LEFT,
                    expand=YES,
                    padx=2, pady=6)
if __name__ == '__main__':
    TestSwitches().mainloop()

Code comments

① direction determines if the toggle is up or down. Since this may be changed programmatically, it provides simple animation in the GUI.

Running this code displays the window in figure 7.5.

![Toggle switches](figure_7_5.png)

Figure 7.5 Toggle switches

7.2.3 Building a MegaWidget

Now that we have mastered creating objects and subclassing to create new behavior and appearance, we can start to create some even more complex widgets, which will result ultimately in more efficient GUIs, since the code required to generate them will be quite compact. First, we need to collect all of the class definitions for LED, HexNut, Nut and ToggleSwitch in a single class library called Components.py.

Next, we are going to create a new class, SwitchIndicator, which displays a toggle switch with an LED indicator above the switch, showing the on/off state of the switch. Everything is contained in a single frame that can be placed simply on a larger GUI. Here is the code to construct the composite widget: