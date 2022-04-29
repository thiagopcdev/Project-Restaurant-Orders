import csv


def get_most_requested_dish(path_to_file, client_name):
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",")
        client_requests = {}
        for row in reader:
            if row[0] == client_name:
                if row[1] in client_requests:
                    client_requests[row[1]] += 1
                else:
                    client_requests[row[1]] = 1
    dishes = list(client_requests.keys())
    dishes_qnt = list(client_requests.values())
    most_requested_dish_qnt = max(dishes_qnt)
    most_requested_dish_index = dishes_qnt.index(most_requested_dish_qnt)
    most_requested_dish_name = dishes[most_requested_dish_index]
    return most_requested_dish_name


def get_order_quantity_by(path_to_file, client_name, dish):
    with open(path_to_file) as file:
        reader = csv.reader(file)
        qnt = 0
        for row in reader:
            if row[0] == client_name and row[1] == dish:
                qnt += 1
        return qnt


def get_never_asked_by(path_to_file, client_name):
    with open(path_to_file) as file:
        reader = csv.reader(file)
        all_dishes_set = set()
        client_dishes_set = set()
        for row in reader:
            if row[1] not in all_dishes_set:
                all_dishes_set.add(row[1])
            if row[0] == client_name:
                client_dishes_set.add(row[1])
        return all_dishes_set.difference(client_dishes_set)


def get_days_client_never_went(path_to_file, client_name):
    with open(path_to_file) as file:
        reader = csv.reader(file)
        all_days_set = set()
        client_days_set = set()
        for row in reader:
            if row[2] not in all_days_set:
                all_days_set.add(row[2])
            if row[0] == client_name:
                client_days_set.add(row[2])
        return all_days_set.difference(client_days_set)
