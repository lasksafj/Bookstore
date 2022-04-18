import sqlite3
# con = sqlite3.connect('example.db')

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return con

def close_connection(con):
    """ close the connection to the database
    """
    con.close()

def insert_db(con, table_name:str, value:list) -> None:
    """ insert data to the database
    :con: connection
    :table_name: name of the table
    :value: list of data needed to insert
    """

    query = "INSERT INTO " + table_name + " VALUES ({})".format(
        ", ".join("?" * len(value)))
    try:
        cur = con.cursor()
        cur.execute(query, tuple(value))
        con.commit()
    except Exception as e:
        print(str(e))

def search_db(con, table_name:str, search:dict) -> list:
    """ search data in the database
    :con: connection
    :table_name: name of the table
    :search: data to search
    :return: list of data found
    """

    query = "SELECT * from " + table_name + " WHERE "
    value = tuple()
    for field in search:
        query += field + "=? AND "
        value = value + (search[field],)
    query = query[:-4]
    try:
        cur = con.cursor()
        cur.execute(query, value)
        result = cur.fetchall()
    except Exception as e:
        print(str(e))
    return result

def update_db(con, table_name:str, id:str, update:dict) -> None:
    """ update data in the database
    :con: connection
    :table_name: name of the table
    :id: id of the field needed to update
    :update: new data
    """

    query = "UPDATE " + table_name + " SET "
    value = tuple()
    for field in update:
        query += field + "=?, "
        value += (update[field],)
    query = query[:-2] + " WHERE id=?"
    value += (id,)
    try:
        cur = con.cursor()
        cur.execute(query, value)
        con.commit()
    except Exception as e:
        print(str(e))

def delete_db(con, table_name:str, id_list:list) -> None:
    """ delete data in the database
    :con: connection
    :table_name: name of the table
    :id_list: list of ids of the fields needed to delete
    """
    query = "DELETE FROM " + table_name + " WHERE id IN ({})".format(
        ", ".join("?" * len(id_list)))
    try:
        cur = con.cursor()
        cur.execute(query, tuple(id_list))
        con.commit()
    except Exception as e:
        print(str(e))

# --------------------------------------------------
con = create_connection("bookstore.db")

# insert = ['2222harr',
#         'Harry Potter 7','JK Rowling',
#         'nxb',2000,2,
#         200,500,'new','available',
#         'fiction', '1-1-2000', 'n/a', 'n/a']
#
# insert_db(con, "books", insert)
#
# search = {
#     'cost': 100,
# }
# print(search_db(con, 'books', search))
#

# update = {
#     "cost": 200,
#     'retail': 700,
# }
#
# update_db(con, "books", "1111harr", update)
#
#
# id_list = ["1156lord", "1334lord"]
# delete_db(con, "books", id_list)

con.close()
