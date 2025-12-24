---
source_image: page_334.png
page_number: 334
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.20
tokens: 8281
characters: 1859
timestamp: 2025-12-24T00:40:46.685512
finish_reason: stop
---

If a window has been iconified or withdrawn, you may restore the window with the deiconify method. It is not an error to deiconify a window that is currently displayed. Make sure that the window is placed on top of the window stack by calling lift as well.

self.deiconify()
self.lift()

13.4 Icon methods

The icon methods are really only useful with X Window window managers. You have limited control over icons with most window managers.
    To set a two-color icon, use iconbitmap:

    self.top.iconbitmap(myBitmap)

    To give the icon a name other than the window’s title, use iconname:

    self.top.iconname('Example')

    You can give the window manager a hint about where you want to position the icon (however, the window manager may place the icon in an iconbox if one is defined or wherever else it wishes):

    self.root.iconposition(10,200)

    If you want a color bitmap, you must create a Label with an image and then use iconwindow:

    self.label = Label(self, image=self.img)
    self.root.iconwindow(self.label)

13.5 Protocol methods

Window managers that conform to the ICCCM* conventions support a number of protocols:

• WM_DELETE_WINDOW    The window is about to be deleted.
• WM_SAVE_YOURSELF    Saves client data.
• WM_TAKE_FOCUS    The window has just gained focus.

You normally will use the first protocol to clean up your application when the user has chosen the exit window menu option and destroyed the window without using the application’s Quit button:

self.root.protocol(WM_DELETE_WINDOW, self.cleanup)

In Python 1.6, the WM_DELETE_WINDOW protocol will be bound to the window’s destroy method by default.

* ICCCM stands for Inter-Client Communication Conventions Manual, which is a manual for client communication in the X environment. This pertains to UNIX systems, but Tk emulates the behavior on all platforms.