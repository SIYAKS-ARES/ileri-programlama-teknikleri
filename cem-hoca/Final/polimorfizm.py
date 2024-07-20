from abc import ABC, abstractmethod

# 1. Temel Sınıf ve Abstract Methodlar
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass  # Sürüş metodu (soyut)

    @abstractmethod
    def refuel(self):
        pass  # Yakıt doldurma metodu (soyut)

    @abstractmethod
    def get_type(self):
        pass  # Araba türünü döndüren metot (soyut)

# 2. Farklı Araba Türleri (Alt Sınıflar)
class ElectricCar(Car):
    def drive(self):
        return "Driving silently"

    def refuel(self):
        return "Charging the battery"

    def get_type(self):
        return "Electric Car"

class PetrolCar(Car):
    def drive(self):
        return "Driving with engine sound"

    def refuel(self):
        return "Refueling with petrol"

    def get_type(self):
        return "Petrol Car"

class HybridCar(Car):
    def drive(self):
        return "Driving with both engine and battery"

    def refuel(self):
        return "Refueling with petrol and charging the battery"

    def get_type(self):
        return "Hybrid Car"

# 3. Polimorfizm Kullanarak Fonksiyonlar
def test_drive(car: Car):
    return car.drive()  # Arabanın sürüş metodu çağrılır

def refuel_car(car: Car):
    return car.refuel()  # Arabanın yakıt doldurma metodu çağrılır

# 4. Polimorfizm Kullanarak Sınıf İçinde Fonksiyonlar
class CarService:
    def __init__(self, car: Car):
        self.car = car  # CarService sınıfı bir araba nesnesi alır

    def perform_service(self):
        return f"Service for {self.car.get_type()}: {self.car.refuel()}"  # Arabanın yakıt doldurma işlemini gerçekleştirir

# Araba Fabrikası sınıfı
class CarFactory:
    def create_car(self, car_type):
        if car_type == 'ElectricCar':
            return ElectricCar()
        elif car_type == 'PetrolCar':
            return PetrolCar()
        elif car_type == 'HybridCar':
            return HybridCar()
        else:
            raise ValueError("Unknown car type")

# Garaj sınıfı
class Garage:
    def __init__(self):
        self.cars = []  # Garajdaki arabaları tutacak liste

    def add_car(self, car: Car):
        self.cars.append(car)  # Arabayı garaja ekler

    def start_all_cars(self):
        for car in self.cars:
            print(f"{car.get_type()}: {car.drive()}")  # Tüm arabaların sürüş metotlarını çağırır

    def refuel_all_cars(self):
        for car in self.cars:
            print(f"{car.get_type()}: {car.refuel()}")  # Tüm arabaların yakıt doldurma metotlarını çağırır

# Polimorfizmin Kullanımı
if __name__ == "__main__":
    # Araba fabrikası ve garaj oluşturma
    factory = CarFactory()
    garage = Garage()

    # Çeşitli arabalar oluşturma ve garaja ekleme
    car_types = ['ElectricCar', 'PetrolCar', 'HybridCar']
    for car_type in car_types:
        car = factory.create_car(car_type)
        garage.add_car(car)

    # Polimorfik fonksiyonlar
    for car in garage.cars:
        print(test_drive(car))  # Her araba türü için farklı sürüş mesajı
        print(refuel_car(car))  # Her araba türü için farklı yakıt mesajı

    # Garajdaki tüm arabaların sürüş ve yakıt işlemleri
    print("\nStarting all cars:")
    garage.start_all_cars()

    print("\nRefueling all cars:")
    garage.refuel_all_cars()

    # Polimorfik sınıf kullanımı
    for car in garage.cars:
        service = CarService(car)
        print(service.perform_service())  # Her araba türü için servis mesajı


class Sekil:
    def ciz(self):
        raise NotImplementedError("Bu metot alt sınıflarda geçersiz kılınmalıdır.")

class Dikdortgen(Sekil):
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def ciz(self):
        return f"Dikdörtgen: {self.en} x {self.boy}"

class Cember(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def ciz(self):
        return f"Çember: Yarıçap {self.yaricap}"

def sekil_ciz(s):
    print(s.ciz())

# Örnek Kullanım
dikdortgen = Dikdortgen(4, 5)
cember = Cember(3)

sekil_ciz(dikdortgen)  # Çıktı: Dikdörtgen: 4 x 5
sekil_ciz(cember)     # Çıktı: Çember: Yarıçap 3

'''# vehicles.py

from abc import ABC, abstractmethod

# Temel Araba sınıfı (Abstract Base Class)
class Car(ABC):
    def __init__(self, make, model):
        self.make = make  # Arabanın markası
        self.model = model  # Arabanın modeli

    @abstractmethod
    def start_engine(self):
        pass  # Motoru çalıştırma metodu (soyut)

    @abstractmethod
    def drive(self):
        pass  # Sürüş metodu (soyut)

    @abstractmethod
    def stop_engine(self):
        pass  # Motoru durdurma metodu (soyut)

    def __str__(self):
        return f"{self.make} {self.model}"  # Arabanın markası ve modeli bilgisini döndürür

# Sedan türü araba sınıfı
class Sedan(Car):
    def start_engine(self):
        return "Sedan engine started"

    def drive(self):
        return "Sedan is driving smoothly"

    def stop_engine(self):
        return "Sedan engine stopped"

# SUV türü araba sınıfı
class SUV(Car):
    def start_engine(self):
        return "SUV engine started"

    def drive(self):
        return "SUV is driving through tough terrain"

    def stop_engine(self):
        return "SUV engine stopped"

# Spor araba sınıfı
class SportsCar(Car):
    def start_engine(self):
        return "Sports car engine roared to life"

    def drive(self):
        return "Sports car is driving at high speed"

    def stop_engine(self):
        return "Sports car engine stopped"

# Elektrikli araba sınıfı
class ElectricCar(Car):
    def start_engine(self):
        return "Electric car engine started silently"

    def drive(self):
        return "Electric car is driving efficiently"

    def stop_engine(self):
        return "Electric car engine stopped"

# Araba Fabrikası sınıfı
class CarFactory:
    def create_car(self, car_type, make, model):
        if car_type == 'Sedan':
            return Sedan(make, model)
        elif car_type == 'SUV':
            return SUV(make, model)
        elif car_type == 'SportsCar':
            return SportsCar(make, model)
        elif car_type == 'ElectricCar':
            return ElectricCar(make, model)
        else:
            raise ValueError("Unknown car type")

# Garaj sınıfı
class Garage:
    def __init__(self):
        self.cars = []  # Garajdaki arabaları tutacak liste

    def add_car(self, car: Car):
        self.cars.append(car)  # Arabayı garaja ekler

    def start_all_engines(self):
        for car in self.cars:
            print(f"{car}: {car.start_engine()}")  # Tüm arabaların motorlarını çalıştırır

    def drive_all_cars(self):
        for car in self.cars:
            print(f"{car}: {car.drive()}")  # Tüm arabaları sürer

    def stop_all_engines(self):
        for car in self.cars:
            print(f"{car}: {car.stop_engine()}")  # Tüm arabaların motorlarını durdurur

# Ana program
if __name__ == "__main__":
    # Araba fabrikası ve garaj oluşturma
    factory = CarFactory()
    garage = Garage()

    # Çeşitli arabalar oluşturma ve garaja ekleme
    car1 = factory.create_car('Sedan', 'Toyota', 'Camry')
    car2 = factory.create_car('SUV', 'Jeep', 'Cherokee')
    car3 = factory.create_car('SportsCar', 'Ferrari', 'F8')
    car4 = factory.create_car('ElectricCar', 'Tesla', 'Model S')

    garage.add_car(car1)
    garage.add_car(car2)
    garage.add_car(car3)
    garage.add_car(car4)

    # Arabaların motorlarını çalıştırma
    print("Starting all engines:")
    garage.start_all_engines()

    # Arabaları sürme
    print("\nDriving all cars:")
    garage.drive_all_cars()

    # Arabaların motorlarını durdurma
    print("\nStopping all engines:")
    garage.stop_all_engines()
'''
