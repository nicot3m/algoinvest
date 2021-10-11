import csv
from itertools import combinations
from time import process_time

data_csv = 'data/dataset_20_actions.csv'

MAX_INVEST = 500


def import_data(data_csv):
    dispo_stock_list = []
    with open(data_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dispo_stock_list.append((row['name'], float(row['price']), float(row['profit'])))
        return dispo_stock_list


def brute_force(dispo_stock_list):
    """
    Trouve best_stock_list parmis dispo_stock_list
    Teste toutes les combinaisons
    Algorithme glouton
    Notation Grand O Complexité O(2^n)
    """
    time_start = process_time()
    can_buy_stock_list = []
    bigO = 0
    len_dispo_stock_list = len(dispo_stock_list)
    for len_combi in range(0, len_dispo_stock_list+1):
        combi_stock_list = list(combinations(dispo_stock_list, len_combi))
        for combi in combi_stock_list:
            stock_combi_price = 0
            stock_combi_profit = 0
            bigO += 1
            for stock in combi:
                stock_price = stock[1]
                stock_profit_percent = stock[2]
                stock_profit = stock_profit_percent / 100 * stock_price
                stock_combi_price += stock_price
                stock_combi_profit += stock_profit
            if stock_combi_price <= MAX_INVEST:
                stock_tuple = (combi, stock_combi_price, stock_combi_profit)
                can_buy_stock_list.append(stock_tuple)

    # sort by stock_combi_profit
    can_buy_stock_list = sorted(can_buy_stock_list, key=lambda stock: stock[2], reverse=True)
    len_can_buy_stock_list = len(can_buy_stock_list)
    can_buy_stock_list_best_element = can_buy_stock_list[0]
    best_stock_list = can_buy_stock_list_best_element[0]
    best_stock_list_price = can_buy_stock_list_best_element[1]
    best_stock_list_price = round(best_stock_list_price, 2)
    best_stock_list_profit = can_buy_stock_list_best_element[2]
    best_stock_list_profit = round(best_stock_list_profit, 2)
    len_best_stock_list = len(best_stock_list)
    time_end = process_time()
    duration = time_end - time_start
    output = (len_dispo_stock_list, bigO, len_can_buy_stock_list, best_stock_list, best_stock_list_price,
              best_stock_list_profit, len_best_stock_list, duration)
    return output


dispo_stock_list = import_data(data_csv)
output = brute_force(dispo_stock_list)
print("len_dispo_stock_list:", output[0], "bigO:", output[1], "len_can_buy_stock_list:", output[2],
      "best_stock_list:", output[3], "best_stock_list_price:", output[4], "best_stock_list_profit:", output[5],
      "len_best_stock_list:", output[6], "duration in s:", output[7])
