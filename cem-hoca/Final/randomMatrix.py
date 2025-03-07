print("\nSimple as possible:")

import random

# 1. Rastgele veri oluşturma
num_employees = 8
num_days = 7

# Boş bir matris oluşturuyoruz
work_hours_matrix = []

# Her çalışanın haftalık çalışma saatlerini oluşturuyoruz
for _ in range(num_employees):
    # 7 gün için rastgele çalışma saatleri oluşturuyoruz
    hours = []
    for _ in range(num_days):
        hour = random.randint(1, 8)  # 1 ile 8 saat arasında rastgele bir saat
        hours.append(hour)  # Bu saati günler listesine ekliyoruz
    work_hours_matrix.append(hours)  # Bu günler listesini matrisimize ekliyoruz

# Rastgele oluşturulan matrisin yazdırılması
print("Rastgele Çalışma Saatleri Matrisi:")
for hours in work_hours_matrix:
    print(hours)

# 2. Toplam çalışma saatlerini hesaplama
totals = []

# Her çalışanın toplam çalışma saatlerini hesaplıyoruz
for hours in work_hours_matrix:
    total_hours = 0
    for hour in hours:
        total_hours += hour  # Her günün saatlerini topluyoruz
    totals.append(total_hours)  # Toplam saatleri listeye ekliyoruz

# 3. Çalışanları toplam saatlere göre sıralama
sorted_indices = []

# Çalışanların indekslerini toplam saatlere göre sıralıyoruz
for i in range(num_employees):
    sorted_indices.append((i, totals[i]))  # Her çalışan ve toplam saatini tuple olarak ekliyoruz

# Listeyi toplam saatlere göre sıralıyoruz (büyükten küçüğe)
sorted_indices.sort(key=lambda x: x[1], reverse=True)

# Sıralı matris oluşturma
sorted_matrix = []

# Sıralı indeksleri kullanarak matrisimizi sıralıyoruz
for index, _ in sorted_indices:
    sorted_matrix.append(work_hours_matrix[index])  # Sıralı matris oluşturuyoruz

# Sıralı matrisi yazdırıyoruz
print("\nToplam Çalışma Saatlerine Göre Sıralanmış Matris:")
for hours in sorted_matrix:
    print(hours)

# Sıralı toplam saatleri yazdırıyoruz
print("\nÇalışanların Toplam Çalışma Saatleri (Sıralı):")
for index, total in sorted_indices:
    print(f"Çalışan {index + 1}: {total} saat")

import numpy as np

print("With Numpy:")

# 1. Rastgele veri oluşturma
np.random.seed(0)  # Sonuçların tekrarlanabilir olması için
num_employees = 8
num_days = 7
work_hours_matrix = np.random.randint(1, 9, size=(num_employees, num_days))

print("Rastgele Çalışma Saatleri Matrisi:\n", work_hours_matrix)

# 2. Toplam çalışma saatlerini hesaplama
total_hours_per_employee = np.sum(work_hours_matrix, axis=1)

# 3. Çalışanları toplam saatlere göre sıralama
# Çalışanların indekslerini ve toplam saatlerini içeren bir liste oluşturuyoruz
employee_total_hours = list(enumerate(total_hours_per_employee))

# Toplam saatlere göre sıralama
sorted_employee_total_hours = sorted(employee_total_hours, key=lambda x: x[1], reverse=True)

# Sıralı matris
sorted_indices = [x[0] for x in sorted_employee_total_hours]
sorted_work_hours_matrix = work_hours_matrix[sorted_indices]

print("\nToplam Çalışma Saatlerine Göre Sıralanmış Matris:\n", sorted_work_hours_matrix)
print("\nÇalışanların Toplam Çalışma Saatleri (Sıralı):", [x[1] for x in sorted_employee_total_hours])

'''
import random

print("\nWithout Numpy:")

# 1. Rastgele veri oluşturma
num_employees = 8
num_days = 7

# Rastgele saatleri içeren matris
work_hours_matrix = [[random.randint(1, 8) for _ in range(num_days)] for _ in range(num_employees)]

print("Rastgele Çalışma Saatleri Matrisi:")
for row in work_hours_matrix:
    print(row)

# 2. Toplam çalışma saatlerini hesaplama
total_hours_per_employee = [sum(row) for row in work_hours_matrix]

# Çalışanların toplam saatlerini ve indekslerini içeren liste oluşturma
employee_total_hours = list(enumerate(total_hours_per_employee))

# 3. Çalışanları toplam saatlere göre sıralama
# Toplam saatlere göre sıralama (büyükten küçüğe)
sorted_employee_total_hours = sorted(employee_total_hours, key=lambda x: x[1], reverse=True)

# Sıralı matris
sorted_indices = [x[0] for x in sorted_employee_total_hours]
sorted_work_hours_matrix = [work_hours_matrix[i] for i in sorted_indices]

print("\nToplam Çalışma Saatlerine Göre Sıralanmış Matris:")
for row in sorted_work_hours_matrix:
    print(row)

print("\nÇalışanların Toplam Çalışma Saatleri (Sıralı):", [x[1] for x in sorted_employee_total_hours])

import random

print("\nLike a COS student:")

# 1. Rastgele veri oluşturma
num_employees = 8
num_days = 7

# Çalışma saatlerini içeren matris
work_hours_matrix = []
for _ in range(num_employees):
    day_hours = [random.randint(1, 8) for _ in range(num_days)]
    work_hours_matrix.append(day_hours)

print("Rastgele Çalışma Saatleri Matrisi:")
for row in work_hours_matrix:
    print(row)

# 2. Toplam çalışma saatlerini hesaplama
total_hours_per_employee = []
for hours in work_hours_matrix:
    total_hours_per_employee.append(sum(hours))

# Çalışanların toplam saatlerini ve indekslerini içeren liste oluşturma
employee_total_hours = list(enumerate(total_hours_per_employee))

# 3. Çalışanları toplam saatlere göre sıralama
# Toplam saatlere göre sıralama (büyükten küçüğe)
sorted_employee_total_hours = sorted(employee_total_hours, key=lambda x: x[1], reverse=True)

# Sıralı matris
sorted_indices = [x[0] for x in sorted_employee_total_hours]
sorted_work_hours_matrix = [work_hours_matrix[i] for i in sorted_indices]

print("\nToplam Çalışma Saatlerine Göre Sıralanmış Matris:")
for row in sorted_work_hours_matrix:
    print(row)

print("\nÇalışanların Toplam Çalışma Saatleri (Sıralı):", [x[1] for x in sorted_employee_total_hours])'''
