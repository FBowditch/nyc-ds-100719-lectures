db_name = 'Plumbs'

TABLES = {}
TABLES["Plumb_biz"] = (
   "CREATE TABLE Plumb_biz ("
   "  biz_id varchar(100) NOT NULL PRIMARY KEY,"
   "  biz_name varchar(100) NOT NULL,"
   "  review_count int(16) NOT NULL,"
   "  rating int(7) NOT NULL"
   ") ENGINE=InnoDB")

TABLES['Plumb_Reviews'] = (
    "CREATE TABLE Plumb_Reviews ("
    "  rev_id int(71) NOT NULL,"
    "  rev_rating int(8) NOT NULL,"
    "  name varchar(40) NOT NULL,"
    "  user_id varchar(40) NOT NULL,"
    "  review_text varchar(5000) NOT NULL,"
    "  rev_date date NOT NULL,"
    "  biz_id int(40) NOT NULL,"
    "  PRIMARY KEY (rev_id)"
    ") ENGINE=InnoDB")



    for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
