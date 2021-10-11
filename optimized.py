import csv
from time import process_time

data_csv='data/dataset_20_actions.csv'

MAX_INVEST = 500


def import_data(data_csv):
    dispo_stock_list = []
    with open(data_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dispo_stock_list.append((row['name'], float(row['price']), float(row['profit'])))
        return dispo_stock_list


def filter_and_sort_data(dispo_stock_list):
    """
    filter and sort data
    """
    # filter positive price
    dispo_stock_list = list(filter(lambda stock: stock[1] > 0, dispo_stock_list))
    # filter positive profit
    dispo_stock_list = list(filter(lambda stock: stock[2] > 0, dispo_stock_list))
    # remove duplicate
    dispo_stock_list = list(set(dispo_stock_list))
    # sort by profit
    dispo_stock_list = sorted(dispo_stock_list, key=lambda stock: stock[2], reverse=True)
    return dispo_stock_list


def optimized(dispo_stock_list):
    """
    Algo optimisé de bruteforce.py
    Trouve "le meilleur chemin" qui mène best_stock_list sans essayer toutes les combinaisons possibles
    trouve best_stock_list parmis dispo_stock_list
    Notation Grand O Complexité O(n)
    """
    time_start = process_time()
    best_stock_list = []
    best_stock_list_price = 0
    best_stock_list_profit = 0
    bigO = 0
    len_dispo_stock_list = len(dispo_stock_list)

    for stock in dispo_stock_list:
        bigO += 1
        stock_price = stock[1]
        if best_stock_list_price + stock_price <= MAX_INVEST:
            stock_profit_percent = stock[2]
            stock_profit = stock_profit_percent / 100 * stock_price
            best_stock_list_price += stock_price
            best_stock_list_profit += stock_profit
            best_stock_list.append(stock)
            len_best_stock_list = len(best_stock_list)
    best_stock_list_price = round(best_stock_list_price, 2)
    best_stock_list_profit = round(best_stock_list_profit, 2)
    time_end = process_time()
    duration = time_end - time_start
    output = (len_dispo_stock_list, bigO, best_stock_list, best_stock_list_price, best_stock_list_profit,
              len_best_stock_list, duration)
    return output


dispo_stock_list = import_data(data_csv)
dispo_stock_list = filter_and_sort_data(dispo_stock_list)
len_dispo_stock_list = len(dispo_stock_list)
output = optimized(dispo_stock_list)
print("len_dispo_stock_list:", output[0], "bigO:", output[1], "best_stock_list:", output[2],
      "best_stock_list_price:", output[3], "best_stock_list_profit:", output[4],
      "len_best_stock_list:", output[5], "duration in s:", output[6])
