# Polimorfizm

Polimorfizm, nesne yönelimli programlamanın (OOP) önemli bir kavramıdır ve nesnelerin aynı arayüz veya sınıftan türetilmiş farklı türevlerde farklı şekillerde davranabilme yeteneğini ifade eder. Bu, aynı işlemin farklı nesnelerde farklı şekillerde uygulanabilmesi anlamına gelir.

Python'da polimorfizm örneği olarak, bir `Animal` sınıfı ve bu sınıftan türetilen `Dog` ve `Cat` sınıflarını kullanabiliriz.

## Örnek Kod

```python
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Polimorfik fonksiyon
def make_sound(animal):
    print(animal.sound())

# Nesneler
dog = Dog()
cat = Cat()

# Polimorfizm burada devreye giriyor
make_sound(dog)  # Çıktı: Woof!
make_sound(cat)  # Çıktı: Meow!
```

Bu örnekte:

1. `Animal` sınıfı, `sound` adında soyut bir metod tanımlar.
2. `Dog` ve `Cat` sınıfları, `Animal` sınıfından türetilir ve `sound` metodunu kendi ihtiyaçlarına göre uygularlar.
3. `make_sound` fonksiyonu, parametre olarak bir `Animal` nesnesi alır ve bu nesnenin `sound` metodunu çağırır.

Polimorfizm, `make_sound` fonksiyonunun hem `Dog` hem de `Cat` nesneleri ile çalışabilmesini sağlar ve her bir nesneye özgü doğru metodun çağrılmasını garantiler.
