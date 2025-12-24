---
source_image: page_407.png
page_number: 407
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.09
tokens: 7465
characters: 1906
timestamp: 2025-12-24T03:11:44.130336
finish_reason: stop
---

задействовать интерактивную командную оболочку с автодополнением, описаниями команд и примерами. Учтите, что для повторения этого примера вам нужно будет использовать отличное от нашего уникальное название functionapp. Возможно, также вам придется указать другой регион Azure, например eastus, поддерживающий бесплатные пробные учетные записи:

$ az interactive
az>> login
az>> az group create --name myResourceGroup --location westus2
az>> az storage account create --name griggheorghiustorage --location westus2 \
--resource-group myResourceGroup --sku Standard_LRS
az>> az functionapp create --resource-group myResourceGroup --os-type Linux \
--consumption-plan-location westus2 --runtime python \
--name pyazure-devops4all7 \
--storage-account griggheorghiustorage
az>> exit

Развертываем проект functionapp в Azure с помощью утилиты func:

$ func azure functionapp publish pyazure-devops4all --build remote
Getting site publishing info...
Creating archive for current directory...
Perform remote build for functions project (--build remote).
Uploading 2.12 KB

ВЫВОД ОПУЩЕН

Running post deployment command(s)...
Deployment successful.
App container will begin restart within 10 seconds.
Remote build succeeded!
Syncing triggers...
Functions in pyazure-devops4all:
    currentTime - [httpTrigger]
        Invoke url:
        https://pyazure-devops4all.azurewebsites.net/api/
        currenttime?code=b0rN93004cGPcGFKyX7n9HgITTPnHZiGCmjJN/SRsPX7taM7axJbbw==

Проверяем работу развернутой функции в Azure посредством запроса к ее конечной точке с помощью curl:

$ curl "https://pyazure-devops4all.azurewebsites.net/api/currenttime\
?code\=b0rN93004cGPcGFKyX7n9HgITTPnHZiGCmjJN/SRsPX7taM7axJbbw\=\=&name\=joe"
Hello joe, the current time is 01:20:32.036097!%

Никогда не помешает очистить ненужные больше облачные ресурсы. В данном случае можно выполнить команду

$ az group delete --name myResourceGroup