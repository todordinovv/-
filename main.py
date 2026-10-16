from models import Avtosalon

salon = Avtosalon()

salon.add_car("BMW", "320d", 15000)
salon.add_car("Mercedes", "C220", 18000)
salon.add_car("Audi", "A4", 12000)

while True:
    print("\n--- АВТОСАЛОН ---")
    print("1. Покажи автомобилите")
    print("2. Добави автомобил")
    print("3. Търси по марка")
    print("4. Подреди по цена")
    print("5. Изход")

    choice = input("Избери опция: ")

    if choice == "1":
        salon.show_cars()

    elif choice == "2":
        brand = input("Марка: ")
        model = input("Модел: ")

        try:
            price = float(input("Цена в лева: "))
            if price <= 0:
                print("Цената трябва да е положително число.")
            else:
                salon.add_car(brand, model, price)
        except ValueError:
            print("Моля, въведи валидна цена.")

    elif choice == "3":
        brand = input("Въведи марка: ")
        salon.search_car(brand)

    elif choice == "4":
        salon.sort_cars()

    elif choice == "5":
        print("Програмата приключи.")
        break

    else:
        print("Невалидна опция!")
