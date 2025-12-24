---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.38
tokens: 6570
characters: 1488
timestamp: 2025-12-24T02:13:08.712576
finish_reason: stop
---

профессиональных программистов на языке Python, так что вы не одиноки в компании тех, у кого такой подход вызывает недоумение.

Чтобы прояснить все, о чем мы говорили, рассмотрим конкретный пример. В приведенном ниже коде вы видите обновленный класс Dog, определенный с новыми функциями, и новый объект lassie, создаваемый с параметрами, один из которых задает его имя как "Lassie", а другой устанавливает его температуру равной 37.

In [1]: # определение класса объектов Dog
class Dog:

    # метод для инициализации объекта внутренними данными
    def __init__(self, petname, temp):
        self.name = petname;
        self.temperature = temp;

    # получить состояние
    def status(self):
        print("имя собаки: ", self.name)
        print("температура собаки: ", self.temperature)
        pass

    # задать температуру
    def setTemperature(self, temp):
        self.temperature = temp;
        pass

    # собаки могут лаять
    def bark(self):
        print("Гав!")
        pass
pass

In [2]: # создать новый объект собаки на основе класса Dog
lassie = Dog("Lassie", 37)

In [3]: lassie.status()
имя собаки: Lassie
температура собаки: 37

Как видите, вызов функции status() для объекта lassie класса Dog обеспечивает вывод его имени и текущего значения температуры. С момента создания объекта эта температура не изменялась.

Попытаемся изменить температуру объекта и проверим, действительно ли она изменилась, введя следующий код.

lassie.SetTemperature(40)
lassie.status()