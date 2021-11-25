"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    realised_phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    def sum_amount(r_p):              # Функция вычисления суммарного количества для каждого телефона
        for i in range(0, len(r_p)): # i это индекс в корневом списке
            sum_sales = 0 
            for j in range(0, len(r_p[i]['items_sold'])): # j это индекс в списке 'items_sold' для каждого продукта
                sum_sales += r_p[i]['items_sold'][j] 
            product_name = r_p[i]['product']

            print(f'суммарное количество продаж {product_name} составляет {sum_sales} экземпляров')
    sum_amount(realised_phones)

    def mid_amount(r_p):             # Функция вычисления среднего количества продаж для каждого телефона 
        for i in range(0, len(r_p)): # i это индекс в корневом списке
            sum_sales = 0 
            for j in range(0, len(r_p[i]['items_sold'])): # j это индекс в списке 'items_sold' для каждого продукта
                sum_sales += r_p[i]['items_sold'][j] 
            mid = sum_sales / len(r_p[i]['items_sold'])
            product_name = r_p[i]['product']

            print(f'среднее количество продаж {product_name} составляет {round(mid,0)} экземпляров')
    mid_amount(realised_phones)

    def sum_by_all(r_p):            # Функция вычисления суммарногоо количества продаж всех товаров
        sum_sales = 0 
        for i in range(0, len(r_p)): # i это индекс в корневом списке
            for j in range(0, len(r_p[i]['items_sold'])): # j это индекс в списке 'items_sold' для каждого продукта
                sum_sales += r_p[i]['items_sold'][j] 

        print(f'суммарное количество продаж составляет {sum_sales} экземпляров')
    sum_by_all(realised_phones)

    def middle_sales_general(r_p):            # Функция вычисления среднего количества продаж всех товаров
        middle_sales = 0
        for i in range(0, len(r_p)): # i это индекс в корневом списке
            sum_sales = 0
            for j in range(0, len(r_p[i]['items_sold'])): # j это индекс в списке 'items_sold' для каждого продукта
                sum_sales += r_p[i]['items_sold'][j] 
                mid = sum_sales / len(r_p[i]['items_sold'])
            middle_sales +=  mid
        middle_sales_gen = middle_sales / len(r_p)
        print(f'среднее количество продаж составляет {middle_sales_gen} экземпляров')
    middle_sales_general(realised_phones)
if __name__ == "__main__":
    main()
