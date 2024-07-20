# Polimorfizm

## `vehicles.py`

```python
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
```

### Kod Açıklaması

1. **Temel Sınıf ve Abstract Methodlar**:
    - `Car` sınıfı soyut bir sınıftır ve üç soyut metot içerir: `drive`, `refuel`, `get_type`.

2. **Farklı Araba Türleri (Alt Sınıflar)**:
    - `ElectricCar`, `PetrolCar`, `HybridCar` sınıfları, `Car` sınıfından türemiş ve soyut metodları kendilerine özgü şekilde uygulamıştır.

3. **Polimorfizm Kullanarak Fonksiyonlar**:
    - `test_drive` ve `refuel_car` fonksiyonları, bir `Car` nesnesi alır ve bu nesnenin `drive` ve `refuel` metodlarını çağırır.

4. **Polimorfizm Kullanarak Sınıf İçinde Fonksiyonlar**:
    - `CarService` sınıfı, bir `Car` nesnesi alır ve `perform_service` metodu, arabanın `refuel` metodunu çağırarak bir servis mesajı döner.

5. **Araba Fabrikası Sınıfı**:
    - `CarFactory` sınıfı, belirli bir türde araba oluşturmak için kullanılır.

6. **Garaj Sınıfı**:
    - `Garage` sınıfı, çeşitli arabaları depolar ve onların sürüş ve yakıt doldurma işlemlerini yönetir.

7. **Polimorfizmin Kullanımı**:
    - Çeşitli araba nesneleri oluşturur ve garaja ekler, ardından polimorfizmin kullanımlarını gösterir.
    - `test_drive` ve `refuel_car` fonksiyonları ile arabaların sürüş ve yakıt işlemleri gerçekleştirilir.
    - `Garage` sınıfı ile tüm arabaların sürüş ve yakıt işlemleri toplu olarak gerçekleştirilir.
    - `CarService` sınıfı ile her araba türü için servis işlemi gerçekleştirilir.
