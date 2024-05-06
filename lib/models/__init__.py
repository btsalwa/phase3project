# import sqlite3

# CONN = sqlite3.connect('main.db')
# CURSOR = CONN.cursor()


# CURSOR.execute("""
# CREATE TABLE IF NOT EXISTS carStore (
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     carType TEXT NOT NULL,
#     available_cars INTEGER NOT NULL,
#     cars_rented INTEGER NOT NULL
# )
# """)

# # Create Customer table
# CURSOR.execute("""
# CREATE TABLE IF NOT EXISTS Customer (
#     cust_id INTEGER PRIMARY KEY,
#     car_rented INTEGER NOT NULL,
#     carTypeid INTEGER NOT NULL,
#     rentType INTEGER NOT NULL,
#     rentPeriod INTEGER NOT NULL,
#     invoice REAL
# )
# """)

# # Populate carStore table
# CURSOR.execute("""
# INSERT INTO carStore (car_id, carType, available_cars, cars_rented)
# VALUES
#     (1, 'sedan', 10, 0),
#     (2, 'suv', 15, 0),
#     (3, 'truck', 8, 0)
# """)

# # Save changes
# CONN.commit()