---
source_image: page_351.png
page_number: 351
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.74
tokens: 8243
characters: 1619
timestamp: 2025-12-24T00:41:09.411781
finish_reason: stop
---

Вот текст кода с комментариями и номерами строк, соответствующими меткам в изображении:

```c
PyObject *rDict = NULL; /* Keep these global */
PyObject *instanceDict;
/*
**    Initializes the dictionary
**    Returns TRUE if successful, FALSE otherwise
*/
int
initDictionary(char *name)
{
    PyObject *importModule;
    int retval = 0;

    /*   *************** Initialize interpreter *************** */
    Py_Initialize();

    /* Import a borrowed reference to the dict Module  */
    if ((importModule = PyImport_ImportModule("dict")))
    {
        /* Get a borrowed reference to the dictionary instance */
        if ((instanceDict = PyObject_CallMethod(importModule, "Dictionary",
            "s", name)))
        {
            /* Store a global reference to the dictionary */
            rDict = PyObject_GetAttrString(instanceDict, "dictionary");
            if (rDict != NULL)
                retval = 1;
        }
        else
        {
            printf("Failed to initialize dictionary\n");
        }
    }
    else
    {
        printf("import of dict failed\n");
    }
    return (retval);
}
/*
**    Finalizes the dictionary
**    Returns TRUE
*/
int
exitDictionary(void)
{
    /*   *************** Finalize interpreter *************** */
    Py_Finalize();
    return (1);
}
/*
**    Returns the information in buffer (which caller supplies)
*/
void
getInfo(char *who, char *buffer)
{
```

Метки:
1. `/* Keep these global */`
2. `/* Import a borrowed reference to the dict Module  */`
3. `/* Get a borrowed reference to the dictionary instance */`
4. `/* Store a global reference to the dictionary */`