---
source_image: page_403.png
page_number: 403
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.10
tokens: 8178
characters: 1346
timestamp: 2025-12-24T00:42:41.266584
finish_reason: stop
---

Now, we need to create a batch file which sets environment variables and invokes our application’s short Python script:

start.bat

set PYTHONPATH=C:\PYTHON\LIB;C:\PYTHON;c:\MyApplication\Common
set TCL_LIBRARY=C:\PYTHON\TCL8.0
set TK_LIBRARY=C:\PYTHON\TK8.0
c:\Python\pythonw startApp.py

The Python script can’t get much simpler:

startApp.py

import myApplication
myApplication.main()

Now, we need to change the properties of the batch program, start.bat. We right mouse-button click on start.bat and select Properties:

Then we set the working directory to the directory containing MyApplication.py, choose Minimized from the Run combobox and check Close on exit. These options are shown in figure 19.4. If you want to change the icon to something specific for your application, click the Change Icon... button and select an icon. Be careful to choose an icon that you ship with your application, and make sure that it is installed in the right place.

Now, when you double-click on the Start.bat file you’ll get just your application with no MS-DOS window. You will get an icon in the Start bar at the bottom of the screen for your open window.

![Screenshot of the start.bat Properties dialog showing options for setting working directory, run minimized, and close on exit](./images/fig_19_4.png)

Figure 19.4 Setting batch file properties