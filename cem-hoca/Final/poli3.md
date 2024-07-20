# Polimorfizm

```python
# vehicles.py

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
```

## Açıklamalar

1. **Temel Sınıf ve Abstract Methodlar**:
   - `Car` sınıfı, soyut bir sınıftır ve diğer araba sınıfları için temel oluşturur.
   - `__init__` metodu, arabanın marka ve model bilgilerini tutar.
   - `start_engine`, `drive` ve `stop_engine` metodları soyut metodlar olarak tanımlanmıştır ve bu metodlar alt sınıflar tarafından uygulanmalıdır.
   - `__str__` metodu, arabanın marka ve model bilgisini döndürür.

2. **Farklı Araba Türleri (Alt Sınıflar)**:
   - `Sedan`, `SUV`, `SportsCar` ve `ElectricCar` sınıfları `Car` sınıfından türemiştir ve her biri soyut metodları kendine özgü şekilde uygular.
   - Her bir sınıf, `start_engine`, `drive` ve `stop_engine` metodlarını kendi türüne uygun şekilde tanımlar.

3. **Araba Fabrikası**:
   - `CarFactory` sınıfı, belirli bir türde araba oluşturur ve geriye o araba nesnesini döner.
   - `create_car` metodu, `car_type` parametresine göre uygun sınıfın bir örneğini oluşturur.

4. **Garaj Sınıfı**:
   - `Garage` sınıfı, çeşitli arabaları tutar ve onların motorlarını çalıştırmak, sürmek ve motorlarını durdurmak için metodlar içerir.
   - `add_car` metodu, bir araba nesnesini garaja ekler.
   - `start_all_engines`, `drive_all_cars` ve `stop_all_engines` metodları, garajdaki tüm arabalar için ilgili işlemleri yapar.

5. **Ana Program**:
   - `CarFactory` ve `Garage` nesneleri oluşturulur.
   - Çeşitli arabalar fabrikadan üretilir ve garaja eklenir.
   - Garajdaki arabaların motorları çalıştırılır, sürülür ve motorları durdurulur.

Bu örnek, polimorfizmin çeşitli yönlerini gösterir ve farklı araba türleri için aynı metodların nasıl farklı şekillerde uygulanabileceğini gösterir.

**a.** Bu kodu test etmek için `unittest` modülünü kullanarak bir test sınıfı yazmak ister misiniz?
