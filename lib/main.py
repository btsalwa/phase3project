from models.cars import carStore, Customer
from tqdm import tqdm


def main():
    # Create an object of class CarStore
    store = carStore(1, 'sedan', 10, 0)
    # Create an object of class Customer
    cust = Customer(101)

    # Run the menu option for the store
    while True:
        print("""
        *************************************************
        1. Show available number of cars in store
        2. Rent a Car on hourly basis for $9/hr
        3. Rent a Car on daily basis for $22/day
        4. Rent a Car on weekly basis for $100/week
        5. Return a rented Car back.
        6. Exit
        *************************************************
        """)
        # Get an input from user for his choice
        choice = int(input("\nHow would you like to use our services\n"))

        # Show inventory cars
        if choice == 1:
            store.show_number_of_cars()

        # Rent on hourly basis
        elif choice == 2:
            # Update the rental type as 1: hourly
            cust.rentType = 1

            # How much time would the customer rent the car? Update rental time in hours.
            n = cust.car_request()
            if n != 0:
                # Use tqdm to show a progress bar
                for _ in tqdm(range(n), desc="Renting cars..."):
                    store.rent_hourly(1)
                hours = int(input("\nHow many hours would you like to rent the car?\n"))
                cust.rentPeriod = hours

        # Rent a car on daily basis
        elif choice == 3:
            # Update the rental type as 2: daily
            cust.rentType = 2

            # How many days would the customer rent the car? Update rental time in days.
            n = cust.car_request()
            if n != 0:
                # Use tqdm to show a progress bar
                for _ in tqdm(range(n), desc="Renting cars..."):
                    store.rent_daily(1)
                days = int(input("\nHow many days would you like to rent the car?\n"))
                cust.rentPeriod = days

        # Rent a car on weekly basis
        elif choice == 4:
            # Update the rental type as 3: weekly
            cust.rentType = 3

            # How many weeks would the customer rent the car? Update rental time in days.
            n = cust.car_request()
            if n != 0:
                # Use tqdm to show a progress bar
                for _ in tqdm(range(n), desc="Renting cars..."):
                    store.rent_weekly(1)
                weeks = int(input("\nHow many weeks would you like to rent the car?\n"))
                cust.rentPeriod = weeks

        # Return car back to the store
        elif choice == 5:
            # Refill the store inventory and calculate bill
            store.return_car(cust)

        # Exit the store
        else:
            print("\nThanks for your visit\n")
            exit()


if __name__ == '__main__':
    main()