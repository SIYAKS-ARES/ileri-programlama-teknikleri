Elbette, 0'dan 100'e kadar olan sayıları içeren bir dosya oluşturup, ardından bu sayıları asal, tek ve çift olarak ayıran Python kodunu aşağıda bulabilirsin:

### 0'dan 100'e kadar olan sayıları içeren bir dosya oluşturma
```python
with open("dosya.txt", "w") as file:
    for i in range(101):
        file.write(f"{i}\n")
```

### Sayıları asal, tek ve çift olarak ayırma
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
odds = []
evens = []

with open("dosya.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if is_prime(number):
            primes.append(number)
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

with open("asal.txt", "w") as file:
    for prime in primes:
        file.write(f"{prime}\n")

with open("tek.txt", "w") as file:
    for odd in odds:
        file.write(f"{odd}\n")

with open("cift.txt", "w") as file:
    for even in evens:
        file.write(f"{even}\n")
```

Bu kod parçası, öncelikle `dosya.txt` adında bir dosya oluşturur ve içine 0'dan 100'e kadar olan sayıları yazar. Daha sonra bu dosyayı okur ve sayıları asal, tek ve çift olarak üç ayrı listeye ayırır. Son olarak, bu listeleri ayrı dosyalara (`asal.txt`, `tek.txt`, `cift.txt`) yazar.