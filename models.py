class Avtosalon:
    def __init__(self):
        self.cars = []

    def add_car(self, brand, model, price):
        car = {
            "brand": brand,
            "model": model,
            "price": price
        }
        self.cars.append(car)
        print("Автомобилът е добавен успешно!")

    def show_cars(self):
        if len(self.cars) == 0:
            print("Няма налични автомобили.")
        else:
            for car in self.cars:
                print(car["brand"], car["model"], "-", car["price"], "лв.")

    def search_car(self, brand):
        found = False

        for car in self.cars:
            if car["brand"].lower() == brand.lower():
                print(car["brand"], car["model"], "-", car["price"], "лв.")
                found = True

        if not found:
            print("Няма намерен автомобил от тази марка.")

    def sort_cars(self):
        self.cars.sort(key=lambda car: car["price"])
        print("Автомобилите са подредени по цена.")
        self.show_cars()
