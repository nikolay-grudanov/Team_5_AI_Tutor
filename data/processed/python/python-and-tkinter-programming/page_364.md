---
source_image: page_364.png
page_number: 364
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.86
tokens: 8446
characters: 2778
timestamp: 2025-12-24T00:41:49.401131
finish_reason: stop
---

16.1 The elements of good interface design

User interfaces are really rather simple: display a screen, have the user input data and click on a button or two and show the user the result of their actions. This appears to be easy, but unless you pay attention to detail, the end user’s satisfaction with the application can be easily destroyed by a badly designed GUI. Of course, appreciation of GUI’s is highly subjective and it is almost impossible to satisfy everyone. We are going to develop a number of example interfaces in this chapter and examine their relative merits. The source code for the examples will not be presented in the text, but it is available online if you want to reproduce the examples or use them as templates for your own interfaces. You can see many more examples of Tkinter code throughout the book! If you do use the supplied source code, please make sure that only the good examples are used.

Take a look at the first GUI (figure 16.1). You may not believe me, but I have seen GUIs similar to this one in commercial applications. This screen does all that it is intended to do—and nothing more—but without any concern for the end user or for human factors. You may wish to examine this example again after we have discussed how to construct a better GUI.

Even though I said that this is an inferior GUI, this type of screen can be acceptable in certain contexts; if all that is needed is a simple screen to input debug information for an application, the amount of code necessary to support this screen is quite small. However, don’t inflict this type of screen on an end user; especially if they are expected to pay money for it!

So let’s take a quick look at the screen’s faults before we determine how the screen could be improved.

1 Jagged label/entry boundary is visually taxing, causing the user to scan randomly in the GUI.
2 Poor choice of font: Courier is a fixed pitch serif font. In this case it does not have sufficient weight or size to allow easy visual scanning.
3 Although the contrast between the black letters and the white background in the entry fields is good, the contrast between the frame and the label backgrounds is too great and makes for a stark interface.
4 Crowded fields make it difficult for the user to locate labels and fields.
5 Fields have arbitrary length. This provides no clues to the user to determine the length of data that should be input.
6 Poor grouping of data: the Position, Employee # type of data have more to do with the name of the individual than the address of the individual and should be grouped accordingly.

Let’s attempt to correct some of the problems with figure 16.1 and see if we can improve the interface. Figure 16.2 shows the result of changing some of the attributes of the GUI.