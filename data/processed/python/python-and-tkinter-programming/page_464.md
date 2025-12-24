---
source_image: page_464.png
page_number: 464
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.22
tokens: 8273
characters: 1896
timestamp: 2025-12-24T00:44:46.228101
finish_reason: stop
---

setvar(name='PY_VAR', value = '1')
Sets the specified variable, name, to the value supplied.

tk_bisque()
Provided for backward compatibility: it restores the application’s colors to the light brown (bisque) color scheme used in Tk 3.6 and earlier versions.

tk_focusFollowsMouse()
Creates an implicit focus model: it reconfigures Tk so that the focus is set to a window whenever the mouse enters it.

tk_focusNext(), tk_focusPrev()
The tk_focusNext and tk_focusPrev methods implement a focus order among the windows of a top-level; they are used in the default bindings for TAB and SHIFT TAB, among other things.

tk_menuBar(*args)
Does nothing, since the Tk function is obsolete.

tk_setPalette(*args)
Changes the color scheme for Tk by modifying the colors of existing widgets and by changing the option database so that future widgets will use the new color scheme. If tk_setPalette is invoked with a single argument, the argument is the name of a color to use as the normal background color; tk_setPalette will compute a complete color palette from this background color.
Alternatively, the arguments to tk_setPalette may consist of any number of name-value pairs, where the first argument of the pair is the name of an option in the Tk option database and the second argument is the new value to use for that option. The following database options are currently supported:

• activeBackground
• activeForeground
• background
• disabledForeground
• foreground
• highlightBackground
• highlightColor
• insertBackground
• selectColor
• selectBackground
• selectForeground
• troughColor

tk_strictMotif(boolean=None)
boolean is set to zero by default. If an application sets it to TRUE, then Tk attempts to adhere as closely as possible to Motif look-and-feel standards. For example, active elements such as buttons and scrollbar sliders will not change color when the pointer passes over them.