# Polimorfizm

Polimorfizmi Python dilinde ayrıntılı bir şekilde açıklayalım. Polimorfizm, nesne yönelimli programlamada oldukça önemli bir kavramdır ve birkaç temel özelliği içerir.

## Polimorfizm Nedir?

Polimorfizm, farklı sınıfların aynı isimdeki metotları kendi özel uygulamalarıyla tanımlamasını sağlar. Bu, kodun daha esnek ve yeniden kullanılabilir olmasını sağlar. Polimorfizmin iki temel türü vardır:

1. **Metot Polimorfizmi (Method Polymorphism):** Aynı isimdeki metotların farklı sınıflarda farklı işlevler görmesi.
2. **Operatör Polimorfizmi (Operator Polymorphism):** Aynı operatörün farklı veri türlerinde farklı işlemler yapabilmesi.

### Polimorfizm Örneği

Aşağıda, polimorfizmi bir örnekle açıklayalım. Bu örnekte, bir "Hayvan" sınıfı ve bu sınıftan türemiş "Kedi" ve "Köpek" sınıfları oluşturacağız. Her bir sınıf, aynı isimdeki `ses` metodunu kendi özel şekliyle uygulayacak.

```python
class Hayvan:
    def ses(self):
        raise NotImplementedError("Bu metot alt sınıflarda geçersiz kılınmalıdır.")

class Kedi(Hayvan):
    def ses(self):
        return "Miyav"

class Köpek(Hayvan):
    def ses(self):
        return "Hav"

def hayvan_sesi(hayvan):
    print(hayvan.ses())

# Örnek Kullanım
kedi = Kedi()
köpek = Köpek()

hayvan_sesi(kedi)  # Çıktı: Miyav
hayvan_sesi(köpek)  # Çıktı: Hav
```

#### Açıklamalar

1. **Temel Sınıf (Hayvan):** `Hayvan` sınıfında `ses` metodu tanımlanmış ama işlevi yok (bu metot, alt sınıflarda geçersiz kılınmalıdır).

2. **Alt Sınıflar (Kedi ve Köpek):** Her iki alt sınıf (`Kedi` ve `Köpek`), `ses` metodunu kendi spesifik işleviyle (kedi için "Miyav", köpek için "Hav") geçersiz kılar.

3. **Fonksiyon (hayvan_sesi):** `hayvan_sesi` fonksiyonu, `Hayvan` türünde bir nesne alır ve `ses` metodunu çağırır. Bu metodun hangi versiyonunun çağrılacağı, nesnenin türüne bağlı olarak değişir.

#### Daha Detaylı Açıklama

1. **Geçersiz Kılma (Overriding):** Polimorfizmde, bir sınıfın metodu alt sınıflarda yeniden tanımlanabilir. Bu, alt sınıfın kendine özgü bir uygulama sağlamasına olanak tanır.

2. **Dinamik Bağlama (Dynamic Binding):** Python, metot çağrılarını çalışma zamanında (runtime) yapar. Bu, polimorfizmin temelidir çünkü hangi metodun çağrılacağını çalışma zamanında belirleriz.

3. **Fonksiyonlarla Polimorfizm:** `hayvan_sesi` fonksiyonu, `Hayvan` türündeki herhangi bir nesne ile çalışabilir. Bu, aynı fonksiyonun farklı türdeki nesnelerle çalışmasını sağlar.

4. **Tür Güvenliği (Type Safety):** Python'da türler esnektir ve tür güvenliği genellikle çalışma zamanında sağlanır. Bu, polimorfizmin sağladığı esnekliğin bir parçasıdır.

### Operatör Polimorfizmi Örneği

Python'da operatör polimorfizmi, aynı operatörün farklı veri türlerinde farklı işlevler yapabilmesini sağlar. Örneğin, `+` operatörü hem sayıları toplamak için hem de dizileri birleştirmek için kullanılabilir:

```python
a = 10 + 20  # Sayıları toplar
b = [1, 2] + [3, 4]  # Listeleri birleştirir

print(a)  # Çıktı: 30
print(b)  # Çıktı: [1, 2, 3, 4]
```

### Başka Bir Örnek

Tabii, polimorfizmi daha geniş bir kapsamda açıklayabilmek için birkaç ek örnek sunabiliriz. Aşağıda polimorfizmi çeşitli senaryolarla detaylı bir şekilde ele alacağız:

### 1. Metot Polimorfizmi

#### Örnek: Şekil Çizimi

Bir `Şekil` sınıfımız ve bu sınıftan türemiş `Dikdörtgen` ve `Çember` sınıflarımız olacak. Her şekil kendi özel `çiz` metodunu sağlar.

```python
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
```

### 2. Operatör Polimorfizmi

#### Örnek: Vektörler

Vektörleri temsil eden bir sınıf oluşturup, `+` ve `*` operatörlerini nasıl polimorfik bir şekilde kullanabileceğimizi görelim.

```python
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)
    
    def __mul__(self, skalar):
        return Vektor(self.x * skalar, self.y * skalar)
    
    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"

# Örnek Kullanım
v1 = Vektor(2, 3)
v2 = Vektor(4, 1)

toplam = v1 + v2
print(toplam)  # Çıktı: Vektor(6, 4)

carpim = v1 * 3
print(carpim)  # Çıktı: Vektor(6, 9)
```

### 3. Polimorfizm ile Fonksiyon Kullanımı

#### Örnek: Çalışanlar

Bir `Calisan` sınıfımız ve bu sınıftan türemiş `Yazilimci` ve `Tasarimci` sınıflarımız olacak. Her çalışan kendi özel `calis` metodunu sağlar.

```python
class Calisan:
    def calis(self):
        raise NotImplementedError("Bu metot alt sınıflarda geçersiz kılınmalıdır.")

class Yazilimci(Calisan):
    def calis(self):
        return "Yazılım geliştiriyor."

class Tasarimci(Calisan):
    def calis(self):
        return "Tasarım yapıyor."

def calisan_calistir(calisan):
    print(calisan.calis())

# Örnek Kullanım
yazilimci = Yazilimci()
tasarimci = Tasarimci()

calisan_calistir(yazilimci)  # Çıktı: Yazılım geliştiriyor.
calisan_calistir(tasarimci)  # Çıktı: Tasarım yapıyor.
```

### 4. Polimorfizm ve İstisnalar

#### Örnek: Formlar

`Form` sınıfı ve `DikdortgenForm` ile `CemberForm` sınıfları. `Form` sınıfı `alan` metoduna sahiptir, bu metod alt sınıflarda geçersiz kılınır.

```python
class Form:
    def alan(self):
        raise NotImplementedError("Bu metot alt sınıflarda geçersiz kılınmalıdır.")

class DikdortgenForm(Form):
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def alan(self):
        return self.en * self.boy

class CemberForm(Form):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan(self):
        from math import pi
        return pi * (self.yaricap ** 2)

def form_alan(form):
    print(form.alan())

# Örnek Kullanım
dikdortgen_form = DikdortgenForm(4, 5)
cember_form = CemberForm(3)

form_alan(dikdortgen_form)  # Çıktı: 20
form_alan(cember_form)     # Çıktı: 28.274333882308138
```

### Polimorfizm ile İlgili Diğer Konular

1. **Soyut Sınıflar:** Polimorfizm genellikle soyut sınıflar (abstract classes) ile birlikte kullanılır. Soyut sınıflar, bazı metodların alt sınıflarda tanımlanmasını zorunlu kılar.

2. **İnterfeysler:** Python'da doğrudan bir arayüz (interface) yapısı yoktur, ancak soyut sınıflar ve metotlar ile benzer bir davranış elde edilebilir.

3. **Dinamik Tür Belirleme:** Python'un dinamik tür sistemi, polimorfizmi daha etkili bir şekilde kullanmanıza olanak tanır çünkü nesnelerin türlerini çalışma zamanında belirleriz.

Bu örnekler ve açıklamalar, polimorfizmi Python'da daha iyi anlamanıza yardımcı olacaktır. Polimorfizm, kodunuzu daha esnek, genişletilebilir ve yeniden kullanılabilir hale getirir.

### Sonuç

Polimorfizm, nesne yönelimli programlamada kodun daha esnek ve yeniden kullanılabilir olmasını sağlar. Python'da polimorfizmi uygularken, metot geçersiz kılma ve dinamik bağlama özellikleri ile farklı sınıfların aynı isimdeki metodlarını özelleştirebiliriz. Bu, kodun daha genel ve esnek bir şekilde yazılmasına olanak tanır.
