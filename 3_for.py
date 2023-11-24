"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
@@ -16,47 +16,12 @@
* Посчитать и вывести среднее количество продаж всех товаров
"""


def summ(sold):
    cnt_day = len(sold[0]['items_sold'])

    iP_summ = sum(sold[0]['items_sold'])
    Mi_summ = sum(sold[1]['items_sold'])
    Sm_summ = sum(sold[2]['items_sold'])

    avg_sold_iP = iP_summ // cnt_day
    avg_sold_Mi = Mi_summ // cnt_day
    avg_sold_Sm = Sm_summ // cnt_day

    total_sold = iP_summ + Mi_summ + Sm_summ

    total_avg = total_sold // (cnt_day * 3)

    print(f'Суммарное количество продаж {sold[0]["product"]} = {iP_summ}')
    print(f'Суммарное количество продаж {sold[1]["product"]} = {Mi_summ}')
    print(f'Суммарное количество продаж {sold[2]["product"]} = {Sm_summ}\n')

    print(f'Среднее количество продаж {sold[0]["product"]} = {avg_sold_iP}')
    print(f'Среднее количество продаж {sold[1]["product"]} = {avg_sold_Mi}')
    print(f'Среднее количество продаж {sold[2]["product"]} = {avg_sold_Sm}\n')

    print(f'Суммарное количество продаж всех товаров = {total_sold}\n')

    print(f'Среднее количество продаж всех товаров = {total_avg}')


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    summ(sold)

    pass

if __name__ == "__main__":
    main()
