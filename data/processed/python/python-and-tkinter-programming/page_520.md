---
source_image: page_520.png
page_number: 520
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.82
tokens: 8313
characters: 2115
timestamp: 2025-12-24T00:46:26.824983
finish_reason: stop
---

forgotten, so that if the slave is managed once more by the grid geometry manager, the initial default settings are used.

grid_info()
Returns a list whose elements are the current configuration state of the slave. The first two elements of the tuple are in master where master is the slave’s master

grid_location(x, y)
Given x and y values in screen units relative to the master window, the column and row number at that x and y location is returned. For locations that are above or to the left of the grid, -1 is returned.

grid_propagate(flag=_noarg_)
If flag has a true boolean value such as 1 or ON then propagation is enabled for self. If flag has a false boolean value then propagation is disabled for self. If flag is omitted then the command returns FALSE or TRUE to indicate whether propagation is currently enabled for self. Propagation is enabled by default.

grid_rowconfigure(index, options...)
Queries or sets the row properties of the index row of the geometry master, master. The valid options are minsize, weight and pad.

grid_remove()
Removes slave from grid for its master and unmaps the window. The slave will no longer be managed by the grid geometry manager. However, the configuration options for that window are remembered, so if the slave is managed once more by the grid geometry manager, the previous values are retained.

grid_size()
Returns the size of the grid (in columns then rows) for master. The size is determined either by the slave occupying the largest row or column, or the largest column or row with a minsize, weight, or pad that is non-zero.

grid_slaves(row=None, column=None)
If no options are supplied, a list of all of the slaves in master are returned, with the most recently managed first. Option can be either row or column which causes only the slaves in the row (or column) specified by value to be returned.

Label

Description
The Label class defines a new window and creates an instance of a label widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the label such as its colors,