"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def define_age(age):
    vozrast = age
    if vozrast <= 6:
        conclusion = f'человек такого возраста должен учиться в саду'
    elif vozrast <= 17:
        conclusion = f'человек такого возраста должен ходить в школу'
    elif vozrast <= 22:
        conclusion = f'человек такого возраста должен учиться в ВУЗе'
    else:
        conclusion = f'человек такого возраста должен работать'
    return(conclusion)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('введите Ваш возраст: ', ))

     
    print(define_age(age))


if __name__ == "__main__":
    main()

