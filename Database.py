import pymysql


def add_item(id, name, type, qty, cost):
    db = pymysql.connect("localhost", "admin", "admin", "INVENTORY_SYSTEM")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Create table as per requirement
    sql_table = """CREATE TABLE IF NOT EXISTS INVENTORY (
             ITEM_ID  CHAR(30) NOT NULL, 
             DESCRIPTION  CHAR(30) NOT NULL,
             TYPE CHAR(20),  
             QTY INT NOT NULL,
             COST FLOAT NOT NULL)"""

    cursor.execute(sql_table)

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO INVENTORY(ITEM_ID, DESCRIPTION, TYPE, QTY, COST) \
           VALUES ('%s', '%s', '%s', '%d', '%f')" % (id, name, type, qty, cost)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def get_item_list():
    # Open database connection
    db = pymysql.connect("localhost", "admin", "admin", "INVENTORY_SYSTEM")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    sql = "SELECT * FROM INVENTORY"
    cursor.execute(sql)
    get = cursor.fetchall()
    # disconnect from server
    db.close()
    return get


def remove_item(item_id):
    # Open database connection
    db = pymysql.connect("localhost", "admin", "admin", "INVENTORY_SYSTEM")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM INVENTORY WHERE ITEM_ID = '%s'" % item_id
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def add_costumer_order(costumer, qty_order, item_id):
    db = pymysql.connect("localhost", "admin", "admin", "INVENTORY_SYSTEM")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Create table as per requirement
    sql_table = """CREATE TABLE IF NOT EXISTS INVENTORY (
                 ITEM_ID  CHAR(30) NOT NULL, 
                 DESCRIPTION  CHAR(30) NOT NULL,
                 TYPE CHAR(20),  
                 QTY INT NOT NULL,
                 COST FLOAT NOT NULL)"""

    cursor.execute(sql_table)
    sql = "UPDATE INVENTORY SET  COSTUMER = '%s', QUANTITY_ORDER = '%d' " \
          "WHERE ITEM_ID = '%s'" % (costumer, qty_order, item_id)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()



def empty():
    # Open database connection
    db = pymysql.connect("localhost", "admin", "admin", "INVENTORY_SYSTEM")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM INVENTORY"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

