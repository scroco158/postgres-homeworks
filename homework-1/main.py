"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')

try:
    with conn:
        with conn.cursor() as curs:
            with open('north_data/employees_data.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tuple_to_insert = (row['employee_id'],
                                       row['first_name'],
                                       row['last_name'],
                                       row['title'],
                                       row['birth_date'],
                                       row['notes'])
                    curs.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', tuple_to_insert)

            with open('north_data/customers_data.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tuple_to_insert = (row['customer_id'],
                                       row['company_name'],
                                       row['contact_name'])
                    curs.execute('INSERT INTO customers VALUES (%s, %s, %s)', tuple_to_insert)

            with open('north_data/orders_data.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tuple_to_insert = (row['order_id'],
                                       row['customer_id'],
                                       row['employee_id'],
                                       row['order_date'],
                                       row['ship_city'])
                    curs.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', tuple_to_insert)
finally:
    conn.close()
