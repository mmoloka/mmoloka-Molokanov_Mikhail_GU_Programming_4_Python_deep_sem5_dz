# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».

def generator_prime_numbers(n: int) -> list[int]:
    #my_list = []
    count = 0
    number = 2
    while count < n:
        for i in range(2, number + 1):
            if number % i == 0 and i != number:
                number += 1
                break
            elif i == number:
                #my_list.append(number)
                yield number
                number += 1
                count += 1
    #return my_list

#print(*generator_prime_numbers(25)) 
for i in generator_prime_numbers(25):
    print(i, end=' ')           

     