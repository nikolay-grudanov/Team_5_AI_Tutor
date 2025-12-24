---
source_image: page_565.png
page_number: 565
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.90
tokens: 7453
characters: 1946
timestamp: 2025-12-24T01:05:46.650102
finish_reason: stop
---

positive_patches.shape

Out[3]: (13233, 62, 47)

Мы получили пригодную для обучения выборку из 13 000 изображений лиц.

2. Получаем набор отрицательных обучающих выборок.

Далее нам необходимо найти набор миниатюр такого же размера, на которых не изображены лица. Чтобы сделать это, можно, например, взять любой корпус исходных изображений и извлечь из них миниатюры в различных масштабах. Воспользуемся некоторыми из поставляемых вместе с пакетом Scikit-Image изображений, а также классом PatchExtractor библиотеки Scikit-Learn:

In[4]: from skimage import data, transform

    imgs_to_use = ['camera', 'text', 'coins', 'moon',
                    'page', 'clock', 'immunohistochemistry',
                    'chelsea', 'coffee', 'hubble_deep_field']
    images = [color.rgb2gray(getattr(data, name)())
              for name in imgs_to_use]

In[5]:
from sklearn.feature_extraction.image import PatchExtractor

def extract_patches(img, N, scale=1.0,
                   patch_size=positive_patches[0].shape):
    extracted_patch_size = \
        tuple((scale * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(patch_size=extracted_patch_size,
                              max_patches=N, random_state=0)
    patches = extractor.transform(img[np.newaxis])
    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size)
                            for patch in patches])
    return patches

negative_patches = np.vstack([extract_patches(im, 1000, scale)
                             for im in images for scale in [0.5, 1.0, 2.0]])
negative_patches.shape

Out[5]: (30000, 62, 47)

У нас теперь есть 30 000 подходящих фрагментов изображений, не содержащих лиц. Рассмотрим некоторые из них, чтобы лучше представить, как они выглядят (рис. 5.150):

In[6]: fig, ax = plt.subplots(6, 10)
       for i, axi in enumerate(ax.flat):
           axi.imshow(negative_patches[500 * i], cmap='gray')
           axi.axis('off')