"# Kullanıcıya kaç gün geçtiği sorulur\n",
    "elapsed_days = int(input(\"Enter the number of days elapsed since today: \"))\n",
    "\n",
    "# GÜn hesaplanır\n",
    "future_day = (today + elapsed_days) % 7\n",
    "\n",
    "# Sonuç gösterilir.\n",
    "print(f\"Today is {days[today]} and the future day is {days[future_day]}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BMI:  23.671253629592222\n",
      "You are normal\n"
     ]
    }
   ],
   "source": [
    "# 4.6\n",
    "\n",
    "# Kullanıcıdan boy değerleri metre ve cm, ağırlık değeri kilogram cinsinden istenir.\n",
    "height_m = float(input(\"Please enter the height in meters: \"))\n",
    "height_cm = float(input(\"Please enter remaining height in centimeters: \"))\n",
    "weight = float(input(\"Please enter weight in kg: \"))\n",
    "\n",
    "# Boyu santimetre cinsinden metre cinsine çevirip BMI hesabı yapıp ekrana yazdırılır.\n",
    "height_total = height_m + height_cm/100\n",
    "BMI = weight/(height_total**2)\n",
    "print(\"BMI: \",BMI)\n",
    "\n",
    "# Koşullar ile kullanıcının durumu karşılaştırılıp kullanıcıya verilir.\n",
    "if BMI < 18:\n",
    "    print(\"You are underweight\")\n",
    "elif BMI < 25:\n",
    "    print(\"You are normal\")\n",
    "elif BMI <30:\n",
    "    print(\"You are overweight\")\n",
    "else:\n",
    "    print(\"You are obese\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your amount 14.67 consists of:\n",
      "\t 14 dollars\n",
      "\t 2 quarters\n",
      "\t 1 dime\n",
      "\t 1 nickel\n",
      "\t 2 penies\n"
     ]
    }
   ],
   "source": [
    "# 4.7\n",
    "\n",
    "# Receive the amount\n",
    "amount = eval(input(\"Enter an amount, for example, 11.56: \"))\n",
    "# Convert the amount to cents\n",
    "remainingAmount = int(amount * 100)\n",
    "# Find the number of one dollars\n",
    "dollars = remainingAmount // 100\n",
    "remainingAmount = remainingAmount % 100\n",
    "# Find the number of quarters in the remaining amount\n",
    "quarters = remainingAmount // 25\n",
    "remainingAmount = remainingAmount % 25\n",
    "# Find the number of dimes in the remaining amount\n",
    "dimes = remainingAmount // 10\n",
    "remainingAmount = remainingAmount % 10\n",
    "# Find the number of nickels in the remaining amount\n",
    "nickels = remainingAmount // 5\n",
    "remainingAmount = remainingAmount % 5\n",
    "# Find the number of pennies in the remaining amount\n",
    "pennies = remainingAmount\n",
    "# Display the results\n",
    "print(\"Your amount\", amount, \"consists of:\")\n",
    "\n",
    "if dollars == 1:\n",
    "    print(\"\\t\", dollars, \"dollar\")\n",
    "else:\n",
    "    print(\"\\t\", dollars, \"dollars\")\n",
    "if quarters == 1:\n",
    "    print(\"\\t\", quarters, \"quarter\")\n",
    "else:\n",
    "    print(\"\\t\", quarters, \"quarters\")\n",
    "if dimes == 1:\n",
    "    print(\"\\t\", dimes, \"dime\")\n",
    "else:\n",
    "    print(\"\\t\", dimes, \"dimes\")\n",
    "if nickels == 1:\n",
    "    print(\"\\t\", nickels, \"nickel\")\n",
    "else:\n",
    "    print(\"\\t\", nickels, \"nickels\")\n",
    "if pennies == 1:\n",
    "    print(\"\\t\", pennies, \"pennie\")\n",
    "else:\n",
    "    print(\"\\t\", pennies, \"penies\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The numbers in increasing order are: 1.0 2.0 3.0\n"
     ]
    }
   ],
   "source": [
    "# 4.8\n",
    "\n",
    "num1 = float(input(\"Please enter first number:\"))\n",
    "num2 = float(input(\"Please enter second number:\"))\n",
    "num3 = float(input(\"Please enter third number:\"))\n",
    "\n",
    "sorted_nums = sorted([num1,num2,num3])\n",
    "\n",
    "print(\"The numbers in increasing order are:\",sorted_nums[0],sorted_nums[1],sorted_nums[2])\n"
   ]
=======
    "# Prompt the user to enter the number of days after today\n",
    "elapsed_days = int(input(\"Enter the number of days elapsed since today: \"))\n",
    "\n",
    "# Calculate the future day of the week\n",
    "future_day = (today + elapsed_days) % 7\n",
    "\n",
    "# Display the result\n",
    "print(f\"Today is {days[today]} and the future day is {days[future_day]}\")\n"





# 4.6

# Kullanıcıdan boy değerleri metre ve cm, ağırlık değeri kilogram cinsinden istenir.
height_m = float(input("Please enter the height in meters: "))
height_cm = float(input("Please enter remaining height in centimeters: "))
weight = float(input("Please enter weight in kg: "))

# Boyu santimetre cinsinden metre cinsine çevirip BMI hesabı yapıp ekrana yazdırılır.
height_total = height_m + height_cm/100
BMI = weight/(height_total**2)
print("BMI: ",BMI)

# Koşullar ile kullanıcının durumu karşılaştırılıp kullanıcıya verilir.
if BMI < 18:
    print("You are underweight")
elif BMI < 25:
    print("You are normal")
elif BMI <30:
    print("You are overweight")
else:
    print("You are obese")




    # 4.7

# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))
# Convert the amount to cents
remainingAmount = int(amount * 100)
# Find the number of one dollars
dollars = remainingAmount // 100
remainingAmount = remainingAmount % 100
# Find the number of quarters in the remaining amount
quarters = remainingAmount // 25
remainingAmount = remainingAmount % 25
# Find the number of dimes in the remaining amount
dimes = remainingAmount // 10
remainingAmount = remainingAmount % 10
# Find the number of nickels in the remaining amount
nickels = remainingAmount // 5
remainingAmount = remainingAmount % 5
# Find the number of pennies in the remaining amount
pennies = remainingAmount
# Display the results
print("Your amount", amount, "consists of:")

if dollars == 1:
    print("\t", dollars, "dollar")
else:
    print("\t", dollars, "dollars")
if quarters == 1:
    print("\t", quarters, "quarter")
else:
    print("\t", quarters, "quarters")
if dimes == 1:
    print("\t", dimes, "dime")
else:
    print("\t", dimes, "dimes")
if nickels == 1:
    print("\t", nickels, "nickel")
else:
    print("\t", nickels, "nickels")
if pennies == 1:
    print("\t", pennies, "pennie")
else:
    print("\t", pennies, "penies")






    # 4.8

num1 = float(input("Please enter first number:"))
num2 = float(input("Please enter second number:"))
num3 = float(input("Please enter third number:"))

sorted_nums = sorted([num1,num2,num3])

print("The numbers in increasing order are:",sorted_nums[0],sorted_nums[1],sorted_nums[2])



# 4.10

import random

# Yüzden küçük rastgele iki sayı üretilip hafızaya alınır.
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# Kullanıcıdan hesaplama sonucu istenir.
answer = eval(input("What is " + str(number1) + " * " + str(number2) + "? "))

# Kullanıcan alınan cevap kontrol edilip kullanıcıya çıktı verilir.
if number1 * number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, '*', number2, "is", number1 * number2, '.')
