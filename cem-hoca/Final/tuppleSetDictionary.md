Python'da tuple, set ve dictionary veri yapıları, farklı veri tiplerini saklamak ve yönetmek için kullanılan güçlü araçlardır. Her biri kendi özelliklerine ve kullanım durumlarına sahiptir.

### Tuple

**Tuple** (demet), değiştirilemez (immutable) ve sıralı (ordered) bir veri yapısıdır. Elemanları parantez `()` içinde tanımlanır ve birden fazla veri tipini içerebilir.

#### Özellikler:
- Değiştirilemez (immutable)
- Sıralı (ordered)
- Elemanlarına indeksleme ile erişilebilir

#### Örnek:
```python
# Tuple tanımlama
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Elemanlara erişim
print(my_tuple[0])  # Çıktı: 1
print(my_tuple[3])  # Çıktı: 'a'

# Tuple'lar değiştirilemez, bu yüzden aşağıdaki satır hata verir:
# my_tuple[1] = 5
```

### Set

**Set** (küme), benzersiz (unique) ve sırasız (unordered) elemanlar içeren bir veri yapısıdır. Küme elemanları süslü parantez `{}` içinde tanımlanır. Set'ler eleman tekrarını önler ve matematiksel küme operasyonları (birleşim, kesişim, fark vb.) yapabilir.

#### Özellikler:
- Benzersiz elemanlar (unique)
- Sırasız (unordered)
- Değiştirilebilir (mutable)

#### Örnek:
```python
# Set tanımlama
my_set = {1, 2, 3, 'a', 'b', 'c'}

# Eleman ekleme
my_set.add('d')

# Eleman silme
my_set.remove(1)

# Set'lerde indeksleme yapılamaz
# print(my_set[0])  # Bu satır hata verir

# Küme operasyonları
another_set = {'b', 'c', 'd', 'e'}
union_set = my_set.union(another_set)
print(union_set)  # Çıktı: {'a', 2, 3, 'b', 'c', 'e', 'd'}
```

### Dictionary

**Dictionary** (sözlük), anahtar-değer (key-value) çiftleri içeren bir veri yapısıdır. Sözlükler, süslü parantez `{}` içinde tanımlanır ve her anahtarın bir değeri vardır. Anahtarlar benzersizdir ve değerler herhangi bir veri tipinde olabilir.

#### Özellikler:
- Anahtar-değer çiftleri (key-value pairs)
- Sırasız (unordered) (Python 3.7+ ile sıralı davranır)
- Değiştirilebilir (mutable)

#### Örnek:
```python
# Dictionary tanımlama
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Değere erişim
print(my_dict['name'])  # Çıktı: Alice
print(my_dict['age'])   # Çıktı: 25

# Değer değiştirme
my_dict['age'] = 26

# Yeni anahtar-değer çifti ekleme
my_dict['job'] = 'Engineer'

# Anahtar veya değer silme
del my_dict['city']

# Anahtarlar üzerinde iterasyon
for key in my_dict:
    print(f"{key}: {my_dict[key]}")
# Çıktı:
# name: Alice
# age: 26
# job: Engineer
```

### Özet:

- **Tuple**: Değiştirilemez ve sıralı, elemanlarına indeksleme ile erişilebilir.
- **Set**: Benzersiz ve sırasız, matematiksel küme operasyonlarını destekler.
- **Dictionary**: Anahtar-değer çiftleri içeren, sırasız ve değiştirilebilir bir yapı.

Bu veri yapıları, farklı ihtiyaçlara ve kullanım senaryolarına göre esneklik sağlar ve Python'da veri yönetimini kolaylaştırır.