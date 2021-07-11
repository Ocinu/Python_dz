"""
Задание 1:
Создать классы для проводных наушников и блютуз наушников,
которые будут реализовывать один и тот же интерфейс взаимодействия
с пользователем и его устройствами. Создать класс пользователя,
который будет хранить в себе указатель на интерфейс наушников и
у которого должна быть возможность поменять их в любой момент
работы. При реализцаии классов должны быть оповещения о
производимых действиях с наушниками. Руководствоваться принципом L.
"""

from abc import *


class DeviceShape(ABC):
    @abstractmethod
    def set_device_type(self):
        pass

    @abstractmethod
    def set_data_transfer(self):
        pass


class HeadphonesShape(DeviceShape):
    def __init__(self):
        self.device_type = self.set_device_type()

    def set_device_type(self):
        self.device_type = 'Headphones'
        return self.device_type

    def set_data_transfer(self):
        pass

    def __str__(self):
        return self.device_type


class WiredHeadphones(HeadphonesShape):
    def __init__(self):
        HeadphonesShape.__init__(self)
        self.data_transfer = self.set_data_transfer()

    def set_data_transfer(self):
        self.data_transfer = 'wired'
        return self.data_transfer

    def __str__(self):
        return f'{self.device_type}, {self.data_transfer}'


class BluetoothHeadphones(HeadphonesShape):
    def __init__(self):
        HeadphonesShape.__init__(self)
        self.data_transfer = self.set_data_transfer()

    def set_data_transfer(self):
        self.data_transfer = 'bluetooth'
        return self.data_transfer

    def __str__(self):
        return f'{self.device_type}, {self.data_transfer}'


class User:
    def __init__(self, val):
        self.headphones = self.set_headphones(val)

    def set_headphones(self, val):
        self.headphones = val
        print(self.headphones)
        return self.headphones

    def __str__(self):
        return f'{self.headphones}'


he1 = BluetoothHeadphones()
he2 = WiredHeadphones()
user = User(he1)
print(user)
user.set_headphones(he2)
"""
Задание 2:
К заданию выше добавить классы гарнитуры и блютуз колонок. Гарнитура
включает в себя функции микрофона, а блютуз колонка - навигацию по 
аудиозаписям и настройку эквалайзера. Руководствоваться принципом I.
"""


class HeadsetShape(DeviceShape):
    def __init__(self):
        self.device_type = self.set_device_type()

    def set_device_type(self):
        self.device_type = 'Headset'
        return self.device_type

    def set_data_transfer(self):
        pass

    def set_microphone(self):
        pass


class Headset(HeadsetShape):
    def __init__(self):
        HeadsetShape.__init__(self)
        self.data_transfer = self.set_data_transfer()
        self.microphone = self.set_microphone()

    def set_data_transfer(self):
        self.data_transfer = 'bluetooth'
        return self.data_transfer

    def set_microphone(self):
        self.microphone = 'microphone'
        return self.microphone


class ColumnShape(DeviceShape):
    def __init__(self):
        self.device_type = self.set_device_type()

    def set_device_type(self):
        self.device_type = 'Column'
        return self.device_type

    def set_data_transfer(self):
        pass

    def set_navigation(self):
        pass

    def set_equalizer(self):
        pass


class Column(ColumnShape):
    def __init__(self):
        ColumnShape.__init__(self)
        self.data_transfer = self.set_data_transfer()
        self.navigation = self.set_navigation()
        self.equalizer = self.set_equalizer()

    def set_data_transfer(self):
        self.data_transfer = 'bluetooth'
        return self.data_transfer

    def set_navigation(self):
        self.navigation = 'navigation'
        return self.navigation

    def set_equalizer(self):
        self.equalizer = 'equalizer'
        return self.equalizer



