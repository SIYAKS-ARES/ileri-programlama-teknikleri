class Address:
    def __init__(self, street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.residents = []

    def validate(self):
        return True

    def add_person(self, person):
        self.residents.append(person)

    def get_residents(self):
        return [resident.name for resident in self.residents]

class Person:
    def __init__(self, name, age=0, phone_number=0.0, email_address="", address=None):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.emailAddress = email_address
        self.address = address
        self.has_parking_pass = False

    def validate(self):
        return True

    def set_address(self, address):
        self.address = address
        address.add_person(self)

    def hasParkingPass(self):
        return self.has_parking_pass

class Student(Person):
    def __init__(self, name, age=0, phone_number=0.0, email_address="", address=None, student_number=0.0):
        super().__init__(name, age, phone_number, email_address, address)
        self.student_number = student_number

    def isEligibleToEnroll(self, student):
        return True

    def getSeminarHistory(self):
        return []

    def takeExamination(self):
        # print("Examination taken")
        pass

class Professor(Person):
    def __init__(self, name, age=0, phone_number=0.0, email_address="", address=None, salary=0.0):
        super().__init__(name, age, phone_number, email_address, address)
        self.list_of_students = []
        self.salary = salary


    def applyExamination(self):
        # print("Examination applied")
        pass


# Adres örneği
address = Address("123 Main St", "Anytown", "Anystate", "12345", "Anycountry")

# Öğrenci örneği
student = Student(name="John Doe", age=21, phone_number=1234567890,
                email_address="john.doe@example.com", address=address, student_number=123456)

# Profesör örneği
professor = Professor(name="Dr. Smith", age=45, phone_number=9876543210,
                    email_address="dr.smith@example.com", address=address, salary=75000)

# Metotları test etme
print(student.isEligibleToEnroll(student))  # Output: True
print(student.getSeminarHistory())  # Output: []
student.takeExamination()  # Output: Examination taken

professor.applyExamination()  # Output: Examination applied

''' UML Diagrams/01.py

+-------------+
|   Address   |
+-------------+
| - street    |
| - city      |
| - state     |
| - postalCode|
| - country   |
+-------------+
| + validate(): bool |
| + add_person(person: Person): void |
| + get_residents(): list |
+-------------+
        |
        | lives at | 0..1 --> 1
        |
+-------------+
|   Person    |
+-------------+
| - name      |
| - age       |
| - phoneNumber |
| - emailAddress |
| - hasParkingPass |
+-------------+
| + validate(): bool |
+-------------+
        |
        |-----------------------------------------------|
        |                                               |
+-------------+                                  +-------------+
|   Student   |                                  |  Professor  |
+-------------+                                  +-------------+
| - studentNumber |                              | - listOfStudents |
| + isEligibleToEnroll(Student): bool |          | - Salary |
+-------------+                                  +-------------+
| + getSeminarHistory(): list |                  | + applyExamination(): void |
| + takeExamination(): void |                    +-------------+
+-------------+
'''


'''Elbette, verdiğiniz UML diyagramını kullanarak Python sınıflarını oluşturabiliriz.
UML diyagramında Person, Student, Professor ve Address sınıfları bulunuyor.
Person sınıfı, Student ve Professor sınıflarının üst sınıfı olarak tanımlanmış.
Address sınıfı ise Person sınıfıyla ilişkilendirilmiş.

### Python Kodları:

#### Address Sınıfı
```python
class Address:
    def __init__(self, street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def validate(self):
        # Burada adres doğrulama işlemi yapılabilir
        return True

    def add_person(self, person):
        self.residents.append(person)

    def get_residents(self):
        return [resident.name for resident in self.residents]

```

#### Person Sınıfı
```python
class Person:
    def __init__(self, name, age=0, phone_number=0.0, email_address="", address=None):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        self.has_parking_pass = False

    def hasParkingPass(self):
        return self.has_parking_pass

```

#### Student Sınıfı (Person'dan kalıtım alır)
```python
class Student(Person):
    def __init__(self, name, age=0, phone_number=0.0, email_address="", address=None, student_number=0.0):
        super().__init__(name, age, phone_number, email_address, address)
        self.student_number = student_number

    def isEligibleToEnroll(self, student):
        # Kayıt olma uygunluk kontrolü
        return True

    def getSeminarHistory(self):
        # Seminer geçmişini döndürme
        return []

    def takeExamination(self):
        # Sınav alımı
        print("Examination taken")

```

#### Professor Sınıfı (Person'dan kalıtım alır)
```python
class Professor(Person):
    def __init__(self, name, age=0, phone_number=0.0, email_address="", address=None, salary=0.0):
        super().__init__(name, age, phone_number, email_address, address)
        self.list_of_students = []
        self.salary = salary

    def applyExamination(self):
        # Sınav uygulaması
        print("Examination applied")

```

### Örnek Kullanım
```python
# Adres örneği
address = Address("123 Main St", "Anytown", "Anystate", "12345", "Anycountry")

# Öğrenci örneği
student = Student(name="John Doe", age=21, phone_number=1234567890,
email_address="john.doe@example.com", address=address, student_number=123456)

# Profesör örneği
professor = Professor(name="Dr. Smith", age=45, phone_number=9876543210,
email_address="dr.smith@example.com", address=address, salary=75000)

# Metotları test etme
print(student.isEligibleToEnroll(student))  # Output: True
print(student.getSeminarHistory())  # Output: []
student.takeExamination()  # Output: Examination taken

professor.applyExamination()  # Output: Examination applied
```

Bu kodlar, UML diyagramında belirtilen sınıfları ve onların ilişkilerini Python'da tanımlar ve uygular.
Her sınıfın özellikleri (attributes) ve metotları (methods) UML diyagramında belirtilen şekliyle oluşturulmuştur.
Bu sayede, UML diyagramından Python kodlarına dönüşümü gerçekleştirmiş olduk.'''