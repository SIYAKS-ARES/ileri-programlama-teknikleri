Girilen bir sayıyı tersine çeviren bir Python fonksiyonu yazabiliriz. Bu işlemi gerçekleştirmek için sayıyı önce string olarak ele alabiliriz, ardından tersine çevirip tekrar sayıya çevirebiliriz. İşte bu işlemi yapan bir fonksiyon:

```python
def reverse_number(number):
    # Sayıyı stringe çevir ve ters çevir
    reversed_str = str(number)[::-1]
    
    # Ters çevrilen stringi tekrar sayıya çevir
    reversed_number = int(reversed_str)
    
    return reversed_number

# Kullanıcıdan sayı al
input_number = int(input("Bir sayı girin: "))

# Fonksiyonu çağır ve sonucu yazdır
reversed_number = reverse_number(input_number)
print("Ters çevrilmiş sayı:", reversed_number)
```

Bu kod şu adımları izler:
1. `reverse_number` fonksiyonu, aldığı sayıyı stringe çevirir ve tersine çevirir (`[::-1]` dilimleme yöntemiyle).
2. Tersine çevrilmiş stringi tekrar sayıya çevirir ve döndürür.
3. Kullanıcıdan bir sayı alır, bu sayıyı `reverse_number` fonksiyonuna geçirir ve sonucu yazdırır.