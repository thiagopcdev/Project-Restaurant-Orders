class TrackOrders:
    def __init__(self):
        self.orders = []
        self.client_orders_set = set()
        self.client_days_set = set()
        self.orders_set = set()
        self.days_set = set()
        self.days_dict = {}
        self.better_day = ''
        self.better_day_count = 0
        self.worst_day = ''
        self.worst_day_count = 10

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.days_set.add(day)
        self.orders_set.add(order)
        self.orders.append((customer, order, day))

        if day not in self.days_dict:
            self.days_dict[day] = 1
        else:
            self.days_dict[day] += 1

    def top_order(self, top_ordered, dishes_dict, order):
        if top_ordered == '':
            top_ordered = order
        if dishes_dict[order] > dishes_dict[top_ordered]:
            top_ordered = order
        return top_ordered

    def get_most_ordered_dish_per_customer(self, customer):
        dishes_dict = {}
        top_ordered = ''

        for name, order, _ in self.orders:
            if name == customer:
                if order not in dishes_dict:
                    dishes_dict[order] = 1
                else:
                    dishes_dict[order] += 1

                top_ordered = self.top_order(top_ordered, dishes_dict, order)
        return top_ordered

    def get_never_ordered_per_customer(self, customer):
        for name, order, _ in self.orders:
            if name == customer:
                self.client_orders_set.add(order)
        return self.orders_set.difference(self.client_orders_set)

    def get_days_never_visited_per_customer(self, customer):
        for name, order, day in self.orders:
            if name == customer:
                self.client_days_set.add(day)
        return self.days_set.difference(self.client_days_set)

    def get_busiest_day(self):
        for day in self.days_dict:
            if self.days_dict[day] > self.better_day_count:
                self.better_day = day
                self.better_day_count = self.days_dict[day]
        return self.better_day

    def get_least_busy_day(self):
        for day in self.days_dict:
            if self.days_dict[day] < self.worst_day_count:
                self.worst_day = day
                self.worst_day_count = self.days_dict[day]
        return self.worst_day
