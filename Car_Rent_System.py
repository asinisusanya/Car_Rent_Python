def create_car_inventory():
    return {
        "C001": {
            "brand": "Toyota",
            "model": "Camry",
            "price_per_day": 60.0,
            "is_available": True
        },
        "C002": {
            "brand": "Honda",
            "model": "Accord",
            "price_per_day": 70.0,
            "is_available": True
        },
        "C003": {
            "brand": "Mahindra",
            "model": "Thar",
            "price_per_day": 150.0,
            "is_available": True
        }
    }


def create_rental_records():
    return {}  # car_id: {"customer_name": name, "days": days}


def show_available_cars(inventory):
    print("\nAvailable Cars:")
    for car_id, car in inventory.items():
        if car["is_available"]:
            print(f"{car_id} - {car['brand']} {car['model']} - ${car['price_per_day']}/day")


def rent_car(inventory, rental_records, car_id, customer_name, days):
    if car_id not in inventory:
        print("Invalid car ID.")
        return False

    car = inventory[car_id]
    if not car["is_available"]:
        print("Car is not available for rent.")
        return False

    total_price = car["price_per_day"] * days
    print("\n== Rental Information ==")
    print(f"Customer Name: {customer_name}")
    print(f"Car: {car['brand']} {car['model']}")
    print(f"Rental Days: {days}")
    print(f"Total Price: ${total_price:.2f}")

    confirm = input("\nConfirm rental (Y/N): ")
    if confirm.lower() == "y":
        car["is_available"] = False
        rental_records[car_id] = {
            "customer_name": customer_name,
            "days": days
        }
        print("\nCar rented successfully.")
        return True

    print("\nRental canceled.")
    return False


def return_car(inventory, rental_records, car_id):
    if car_id not in inventory:
        print("Invalid car ID.")
        return

    if car_id not in rental_records:
        print("This car was not rented.")
        return

    customer_name = rental_records[car_id]["customer_name"]
    inventory[car_id]["is_available"] = True
    del rental_records[car_id]
    print(f"Car returned successfully by {customer_name}")


def main_menu():
    inventory = create_car_inventory()
    rental_records = create_rental_records()

    while True:
        print("\n===== Car Rental System =====")
        print("1. Rent a Car")
        print("2. Return a Car")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n== Rent a Car ==")
            show_available_cars(inventory)
            if not any(car["is_available"] for car in inventory.values()):
                print("No cars available for rent.")
                continue

            car_id = input("\nEnter the car ID you want to rent: ")
            if car_id in inventory:
                customer_name = input("Enter your name: ")
                try:
                    days = int(input("Enter the number of days for rental: "))
                    if days <= 0:
                        raise ValueError
                    rent_car(inventory, rental_records, car_id, customer_name, days)
                except ValueError:
                    print("Please enter a valid number of days.")
            else:
                print("Invalid car ID.")

        elif choice == "2":
            print("\n== Return a Car ==")
            if not rental_records:
                print("No cars are currently rented.")
                continue

            print("\nRented Cars:")
            for car_id in rental_records:
                car = inventory[car_id]
                customer = rental_records[car_id]["customer_name"]
                print(f"{car_id} - {car['brand']} {car['model']} - Rented by {customer}")

            car_id = input("\nEnter the car ID to return: ")
            return_car(inventory, rental_records, car_id)

        elif choice == "3":
            print("\nThank you for using the Car Rental System!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main_menu()