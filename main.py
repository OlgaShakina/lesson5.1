class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"Товар '{name}' добавлен в ассортимент по цене {price}.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Товар '{name}' удален из ассортимента.")
        else:
            print(f"Товар '{name}' отсутствует в ассортименте.")

    def get_item_price(self, name):
        return self.items.get(name)

    def update_item_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print(f"Цена товара '{name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{name}' отсутствует в ассортименте.")

#Пример использования
store1 = Store("Магазин 1", "Адрес 1")
store1.add_item("Яблоки", 1.5)
store1.add_item("Груши", 2.0)
store1.update_item_price("Яблоки", 1.75)
print(store1.get_item_price("Яблоки"))
store1.remove_item("Груши")