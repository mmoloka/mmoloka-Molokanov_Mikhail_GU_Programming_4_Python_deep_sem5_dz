# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def generator_fibonacci(count: int) -> list[int]:
    n1 = 0
    n2 = 1
    fibonacci_list = [n1, n2]
    for _ in range (3, count + 1):
        temp = n2
        n2 = temp + n1
        n1 = temp
        fibonacci_list.append(n2)
    return fibonacci_list

print(*generator_fibonacci(10))    
    

