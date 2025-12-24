---
source_image: page_604.png
page_number: 604
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.10
tokens: 8305
characters: 1979
timestamp: 2025-12-24T00:49:04.571283
finish_reason: stop
---

Components

hull
This acts as the body for the megawidget. The contents of the megawidget are created as canvas items and positioned in the hull using the canvas coordinate system. By default, this component is a Tkinter.Canvas.

Methods

add(pagename, ** kw)
Adds a page at the end of the notebook. See the insert() method for full details.

delete(*pageNames)
Deletes the pages given by pageNames from the notebook. Each of the pageNames may have any of the forms accepted by the index() method. If the currently selected page is deleted, then the next page, in index order, is selected. If the end page is deleted, then the previous page is selected.

getcurselection()
Returns the name of the currently selected page.

index(index, forInsert = 0)
Returns the numerical index of the page corresponding to index. This may be specified in any of the following forms:
• name    Specifies the page labelled name.
• number  Specifies the page numerically, where 0 corresponds to the first page.
• END     Specifies the last page.
• SELECT  Specifies the currently selected page.

insert(pageName, before = 0, **kw)
Adds a page to the notebook as a component named pageName. The page is added just before the page specified by before, which may have any of the forms accepted by the index() method. If tabpos is not None, also create a tab as a component named pageName-tab. Keyword arguments prefixed with page_ or tab_ are passed to the respective constructors when creating the page or tab. If the tab_text keyword argument is not given, the text option of the tab defaults to pageName. If a page is inserted into an empty notebook, the page is selected. To add a page to the end of the notebook, use add(). The method returns the pageName component widget.

page(pageIndex)
Returns the frame component widget of the page pageIndex, where pageIndex may have any of the forms accepted by the index() method.

pagenames()
Returns a list of the names of the pages, in display order.