import lib.helper as helper


def display_menu():
    print("""
    **************************************************
    Welcome to Rent-A-Car! How can we help?
    **************************************************
    1. Rent a car
    2. Return an already rented car
    3. Exit
    **************************************************
    """)

def display_car_menu():
    print("""
    **************************************************
    Car Store Menu
    **************************************************
    1. Create a car
    2. Delete a car
    3. Display all cars
    4. View related objects
    5. Find a car by id
    6. Go back
    **************************************************
    """)

def display_customer_menu():
    print("""
    **************************************************
    Customer Menu
    **************************************************
    1. Create a customer
    2. Delete a customer
    3. Display all customers
    4. View related objects
    5. Find a customer by id
    6. Go back
    **************************************************
    """)

def main():
    display_menu()
    flag = 1

    while flag == 1:
        case = int(input("Enter your request\n"))

    if case != 1 and case !=2 and case!=3:
            print("The input is not valid. Please enter 1 or 2")

    elif case == 1:
        while True:
                display_car_menu()
                case = int(input("Enter your request\n"))

                if case == 1:
                    car_id = int(input("Enter car id\n"))
                    carType = input("Enter car type\n")
                    available_cars = int(input("Enter available cars\n"))
                    cars_rented = int(input("Enter cars rented\n"))
                    helper.CarStore.create(car_id, carType, available_cars, cars_rented)

                elif case == 2:
                    car_id = int(input("Enter car id\n"))
                    helper.CarStore.delete(car_id)

                elif case == 3:
                    cars = helper.CarStore.get_all()
                    for car in cars:
                        print(car)

                elif case == 4:
                    cust_id = int(input("Enter customer id\n"))
                    customer = helper.Customer.find_by_id(cust_id)
                    if customer:
                        print(customer.car_rented)

                elif case == 5:
                    car_id = int(input("Enter car id\n"))
                    car = helper.CarStore.find_by_id(car_id)
                if car:
                    print(car)

                elif case == 6:
    
                    break

                else:
                    print("The input is not valid. Please enter 1, 2, 3, 4, 5, or 6")

    elif case == 2:
        while True:
                display_customer_menu()
                case = int(input("Enter your request\n"))

                if case == 1:
                    cust_id = int(input("Enter customer id\n"))
                    car_id = int(input("Enter car id\n"))
                    carTypeid = car_id
                    rentType = int(input("Enter rent type\n"))
                    rentPeriod = int(input("Enter rent period\n"))
                    invoice = 0
                    helper.Customer.create(cust_id, car_id, carTypeid, rentType, rentPeriod, invoice)

                elif case == 2:
                    cust_id = int(input("Enter customer id\n"))
                    helper.Customer.delete(cust_id)

                elif case == 3:
                    customers = helper.Customer.get_all()
                    for customer in customers:
                        print(customer)

                elif case == 4:
                    cust_id = int(input("Enter customer id\n"))
                    customer = helper.Customer.find_by_id(cust_id)
                    if customer:
                        print(customer.car_rented)

                elif case == 5:
                    cust_id = int(input("Enter customer id\n"))
                    customer = helper.Customer.find_by_id(cust_id)
                    if customer:
                        print(customer)

                elif case == 6:
                    break

                else:
                    print("The input is not valid. Please enter 1, 2, 3, 4, 5, or 6")
    elif case == 3:
            flag = 0

    else:
        print("The input is not valid. Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()