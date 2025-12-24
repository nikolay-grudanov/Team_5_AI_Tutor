---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.86
tokens: 7218
characters: 898
timestamp: 2025-12-24T00:58:50.082858
finish_reason: stop
---

Существует множество вариантов пользовательских настроек такого графика, которые могут нам понадобиться. Например, можно задать местоположение легенды и отключить рамку (рис. 4.42):

In[4]: ax.legend(loc='upper left', frameon=False)
    fig

![Легенда графика с пользовательскими настройками](../images/fig_4_42.png)

Рис. 4.42. Легенда графика с пользовательскими настройками

Можно также воспользоваться командой ncol, чтобы задать количество столбцов в легенде (рис. 4.43):

In[5]: ax.legend(frameon=False, loc='lower center', ncol=2)
    fig

![Легенда графика в два столбца](../images/fig_4_43.png)

Рис. 4.43. Легенда графика в два столбца

Можно использовать для легенды скругленную прямоугольную рамку (fancybox) или добавить тень, поменять прозрачность (альфа-фактор) рамки или поля около текста (рис. 4.44):

In[6]: ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
    fig