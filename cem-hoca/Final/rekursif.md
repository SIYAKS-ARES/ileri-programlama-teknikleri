Rekürsif bir fonksiyon kullanarak girilen kelimeyi tersten yazabiliriz. Rekürsif fonksiyonlar, bir problemi daha küçük alt problemlere bölerek çözmeye çalışır. Bu örnekte, kelimenin ilk karakterini sona ekleyerek geri kalan kısmını tersine çeviririz.

İşte rekürsif bir fonksiyon ile kelimeyi tersine çeviren bir Python kodu:

```python
def reverse_string_recursive(s):
    # Eğer kelime boş veya tek karakterli ise, direkt döndür
    if len(s) == 0:
        return s
    else:
        # İlk karakteri sona ekle ve geri kalan kısmı tersine çevir
        return reverse_string_recursive(s[1:]) + s[0]

# Kullanıcıdan kelime al
input_string = input("Bir kelime girin: ")

# Fonksiyonu çağır ve sonucu yazdır
reversed_string = reverse_string_recursive(input_string)
print("Ters çevrilmiş kelime:", reversed_string)
```

Bu kod şu adımları izler:
1. `reverse_string_recursive` fonksiyonu, kelimenin uzunluğu 0 ise kelimeyi doğrudan döndürür.
2. Eğer kelime boş değilse, ilk karakteri sona ekler ve geri kalan kısmı (ilk karakter hariç) tersine çevirerek fonksiyonu yeniden çağırır.
3. Kullanıcıdan bir kelime alır, bu kelimeyi `reverse_string_recursive` fonksiyonuna geçirir ve sonucu yazdırır.