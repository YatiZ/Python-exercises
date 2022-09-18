import mysql.connector
db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "doraemon",
    database = "secondDB"
)

dataType = "INSERT INTO Data(id,user_name,age,item_code,ph_number)values(%s,%s,%s,%s,%s)"
id = int(input("Enter your Id: "))
user_name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
item_code = int(input("Enter your code: "))
ph_number = int(input("Enter your ph-number: "))
user_data = []
user_data.append(id)
user_data.append(user_name)
user_data.append(age)
user_data.append(item_code)
user_data.append(ph_number)
data = tuple(user_data)
print(user_data)

# db_cursor.execute("CREATE TABLE Data(id int primary key AUTO_INCREMENT, user_name VARCHAR(30), age SMALLINT, item_code INT, ph_number INT)")

db_cursor = db_connection.cursor()
db_cursor.execute(dataType,data)
db_connection.commit()

db_cursor.execute("SELECT * FROM Data")
for db in db_cursor:
    print(db)
    