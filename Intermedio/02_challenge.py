## Challenges ##

## FIZZ BUZZ

'''
Si los números son multiplos de 3, aparece Fizz
Si los números son múltiplos de 5, aparece Buzz
Si los numeros son multiplos de 3 y 5, aparece FizzBuzz
'''

def fizzBuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)



fizzBuzz()