import sqlite3

CONN = sqlite3.connect('main.db')
CURSOR = CONN.cursor()

class carStore:
    def __init__(self, car_id, carType, available_cars, cars_rented):
        self.car_id = car_id
        self.carType = carType
        self.available_cars = available_cars
        self.cars_rented = cars_rented

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        if not isinstance(value, int):
            raise ValueError("car_id must be an integer")
        self._car_id = value

    @property
    def carType(self):
        return self._carType

    @carType.setter
    def carType(self, value):
        if not isinstance(value, str):
            raise ValueError("carType must be a string")
        self._carType = value

    @property
    def available_cars(self):
        return self._available_cars

    @available_cars.setter
    def available_cars(self, value):
        if not isinstance(value, int):
            raise ValueError("available_cars must be an integer")
        self._available_cars = value

    @property
    def cars_rented(self):
        return self._cars_rented

    @cars_rented.setter
    def cars_rented(self, value):
        if not isinstance(value, int):
            raise ValueError("cars_rented must be an integer")
        self._cars_rented = value

    @classmethod
    def create(cls, car_id, carType, available_cars, cars_rented):
        CURSOR.execute("""
            INSERT INTO carStore (car_id, carType, available_cars, cars_rented)
            VALUES (?, ?, ?, ?)
        """, (car_id, carType, available_cars, cars_rented))
        CONN.commit()

    @classmethod
    def delete(cls, car_id):
        CURSOR.execute("""
            DELETE FROM carStore
            WHERE car_id = ?
        """, (car_id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("""
            SELECT * FROM carStore
        """)
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, car_id):
        CURSOR.execute("""
            SELECT * FROM carStore
            WHERE car_id = ?
        """, (car_id,))
        return CURSOR.fetchone()

class Customer:
    def __init__(self, cust_id, car_rented, carTypeid, rentType, rentPeriod, invoice):
        self.cust_id = cust_id
        self.car_rented = car_rented
        self.carTypeid = carTypeid
        self.rentType = rentType
        self.rentPeriod = rentPeriod
        self.invoice = invoice

    @property
    def cust_id(self):
        return self._cust_id

    @cust_id.setter
    def cust_id(self, value):
        if not isinstance(value, int):
            raise ValueError("cust_id must be an integer")
        self._cust_id = value

    @property
    def car_rented(self):
        return self._car_rented

    @car_rented.setter
    def car_rented(self, value):
        if not isinstance(value, CarStore):
            raise ValueError("car_rented must be a CarStore object")
        self._car_rented = value

    @property
    def carTypeid(self):
        return self._carTypeid

    @carTypeid.setter
    def carTypeid(self, value):
        if not isinstance(value, int):
            raise ValueError("carTypeid must be an integer")
        self._carTypeid = value

    @property
    def rentType(self):
        return self._rentType

    @rentType.setter
    def rentType(self, value):
        if not isinstance(value, int):
            raise ValueError("rentType must be an integer")
        self._rentType = value

    @property
    def rentPeriod(self):
        return self._rentPeriod

    @rentPeriod.setter
    def rentPeriod(self, value):
        if not isinstance(value, int):
            raise ValueError("rentPeriod must be an integer")
        self._rentPeriod = value

    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, value):
        if not isinstance(value, float):
            raise ValueError("invoice must be a float")
        self._invoice = value

    @classmethod
    def create(cls, cust_id, car_rented, carTypeid, rentType, rentPeriod, invoice):
        CURSOR.execute("""
            INSERT INTO Customer (cust_id, car_rented, carTypeid, rentType, rentPeriod, invoice)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (cust_id, car_rented, carTypeid, rentType, rentPeriod, invoice))
        CONN.commit()

    @classmethod
    def delete(cls, cust_id):
        CURSOR.execute("""
            DELETE FROM Customer
            WHERE cust_id = ?
        """, (cust_id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("""
            SELECT * FROM Customer
        """)
        return CURSOR.fetchall()

    @classmethod
    def find_by_id(cls, cust_id):
        CURSOR.execute("""
            SELECT * FROM Customer
            WHERE cust_id = ?
        """, (cust_id,))
        return CURSOR.fetchone()