'''def is_prime(n):
    """Verilen sayının asal olup olmadığını kontrol eder."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1. dosya.txt dosyasını oluştur ve içine 0'dan 100'e kadar olan sayıları yaz
with open("dosya.txt", "w") as file:
    for number in range(101):  # 0'dan 100'e kadar olan sayılar
        file.write(f"{number}\n")

# 2. dosya.txt dosyasını oku ve sayıları sınıflandır
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

# 3. asal.txt dosyasını oluştur ve asal sayıları yaz
with open("asal.txt", "w") as file:
    for prime in primes:
        file.write(f"{prime}\n")

# 4. tek.txt dosyasını oluştur ve tek sayıları yaz
with open("tek.txt", "w") as file:
    for odd in odds:
        file.write(f"{odd}\n")

# 5. cift.txt dosyasını oluştur ve çift sayıları yaz
with open("cift.txt", "w") as file:
    for even in evens:
        file.write(f"{even}\n")'''

def is_prime(n):
    """Bir sayının asal olup olmadığını kontrol eder."""
    if n <= 1:
        return False  # 0 ve 1 asal sayı değildir
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Bölünebiliyorsa asal değil
    return True

# 1. Adım: 0'dan 100'e kadar olan sayıları dosya.txt dosyasına yazma
with open("dosya.txt", "w") as file:
    for number in range(101):  # 0'dan 100'e kadar sayılar
        file.write(f"{number}\n")  # Her sayıyı dosyaya yaz

# 2. Adım: dosya.txt dosyasını oku ve sayıları sınıflandır
primes = []  # Asal sayılar için liste
odds = []    # Tek sayılar için liste
evens = []   # Çift sayılar için liste

with open("dosya.txt", "r") as file:
    for line in file:
        number = int(line.strip())  # Satırdaki sayıyı oku ve tamsayıya dönüştür
        if is_prime(number):
            primes.append(number)  # Asal sayıyı listeye ekle
        if number % 2 == 0:
            evens.append(number)   # Çift sayıyı listeye ekle
        else:
            odds.append(number)    # Tek sayıyı listeye ekle

# 3. Adım: Sınıflandırılmış sayıları ayrı dosyalara yazma

# Asal sayıları asal.txt dosyasına yaz
with open("prime.txt", "w") as file:
    for prime in primes:
        file.write(f"{prime}\n")

# Tek sayıları tek.txt dosyasına yaz
with open("odds.txt", "w") as file:
    for odd in odds:
        file.write(f"{odd}\n")

# Çift sayıları cift.txt dosyasına yaz
with open("evens.txt", "w") as file:
    for even in evens:
        file.write(f"{even}\n")