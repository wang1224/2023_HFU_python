import time
import abc

class Poultry(abc.ABC):  # 家禽的類別
    def __init__(self, name, sound, specy):
        self.name = name  # 外部傳入的參數會變成內部的Attribute(屬性)
        self.sound = sound
        self.specy = specy

    def make_some_noise(self, times=3):
        self.name = "Noisy " + self.name
        print(f"{self.specy}-{self.name} make noise: {self.sound * times}")
    
    def hatch(self):
        print("Baby comes out ASAP.")

    @abc.abstractmethod
    def eat(self):
        pass

class Duck(Poultry):
    def __init__(self, name, sound):
        super().__init__(name, sound, 'Duck')

    def swim(self):
        print(f"{self.specy}-{self.name} is swimimg.")

    def eat(self):
        print(f"{self.specy} eat anything.")

class Chicken(Poultry):
    def __init__(self, name, sound):
        super().__init__(name, sound, 'Chicken')

    def morning_call(self):
        current_time = time.gmtime(time.time())
        hour = current_time.tm_hour
        minute = current_time.tm_min
        print(f"{self.specy}-{self.name} said: It is {hour}:{minute} now.")
    
    def eat(self):
        print(f"{self.specy} eat bugs.")

class Goose(Poultry):
    def __init__(self, name, sound):
        super().__init__(name, sound, 'Goose')

    def chase_and_bit(self):
        print(f"{self.specy} - {self.name} is chasing you..... run !!!")
    
    def eat(self):
        print(f"{self.specy} eat vegetable.")

if __name__ == '__main__':

    duck_1 = Duck("Guck", 'Gu')
    duck_2 = Duck("Quck", 'Qu')
    duck_3 = Duck("Peter", "pu")
    chicken_1 = Chicken("Danny", "Goo")
    goose_1 = Goose("George", "Qua")


    duck_1.eat()
    chicken_1.eat()
    goose_1.eat()