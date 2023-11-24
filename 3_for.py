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


def summ_sold(list_sold):
    for i in list_sold:
        cnt_day = len(i['items_sold'])

        if i['product'] == 'iPhone 12':
            iP_summ = sum(i['items_sold'])
            avg_sold_iP = iP_summ // cnt_day
            print(f'Суммарное количество продаж {i["product"]} = {iP_summ}')
            print(f'Среднее количество продаж {i["product"]} = {avg_sold_iP}\n')

        elif i['product'] == 'Xiaomi Mi11':
            Mi_summ = sum(i['items_sold'])
            avg_sold_Mi = Mi_summ // cnt_day
            print(f'Суммарное количество продаж {i["product"]} = {Mi_summ}')
            print(f'Среднее количество продаж {i["product"]} = {avg_sold_Mi}\n')

        elif i['product'] == 'Samsung Galaxy 21':
            Sm_summ = sum(i['items_sold'])
            avg_sold_Sm = Sm_summ // cnt_day
            print(f'Суммарное количество продаж {i["product"]} = {Sm_summ}')
            print(f'Среднее количество продаж {i["product"]} = {avg_sold_Sm}\n')

    total_sold = iP_summ + Mi_summ + Sm_summ
    total_avg = total_sold // (cnt_day * 3)

    print(f'Суммарное количество продаж всех товаров за весь период = {total_sold}\n')

    print(f'Среднее количество продаж всех товаров в день= {total_avg}')


def main():
    list_sold = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    summ_sold(list_sold)


if __name__ == "__main__":
    main()
