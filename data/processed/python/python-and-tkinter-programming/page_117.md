---
source_image: page_117.png
page_number: 117
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.82
tokens: 8272
characters: 1865
timestamp: 2025-12-24T00:34:32.878646
finish_reason: stop
---

root.title('Scrapbook')
scrapbook = Scrapbook(root)
root.mainloop()

Code comments

1 We create the Label which will contain the image, placing it approximately in the center of the window and anchoring it at the center. Note that the relative placings are expressed as percentages of the width or height of the container.

self.lbl.place(relx=0.5, rely=0.48, anchor=CENTER)

2 We get a list of files from the images directory

3 place really lends itself to be used for calculated positioning. In the loop we create a Button, binding the index of the button to the activate callback and placing the button at the next available position.

4 We put one button at the bottom right of the screen to allow us to quit the scrapbook. Note that we anchor it at the SE corner. Also note that we pack the outer frame. It is quite common to pack a group of widgets placed within a container. The Packer does all the work of negotiating the space with the outer containers and the window manager.

5 getImg is the PIL code to load the image, create a thumbnail, and load it into the Label.

In addition to providing precise window placement, place also provides rubber sheet placement, which allows the programmer to specify the size and location of the slave window in terms of the dimensions of the master window. It is even possible to use a master window which is not the parent of the slave. This can be very useful if you want to track the dimensions of an arbitrary window. Unlike pack and grid, place allows you to position a window outside the master (or sibling) window. Figure 5.22 illustrates the use of a window to display some of an image’s properties in a window above each of the images. As the size of the image changes, the information window scales to fit the width of the image.

Figure 5.21 Adding a sibling window which tracks changes in attached window