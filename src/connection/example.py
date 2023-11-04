from crud import Crud

table = Crud(
    user='postgres',
    password='123456',
    host='localhost',
    port='5432',
    dbname='datn')

table.connect()

# table.insert(city= 'fayoum',address=)