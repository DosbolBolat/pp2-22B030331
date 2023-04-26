import psycopg2  
con = psycopg2.connect(host = "localhost", database = "dos", user = "postgres", password = "D0SBO1@B")
current = con.cursor()
current.execute('''CREATE TABLE PhoneBook(name varchar, number varchar);''')
current.close()
con.commit()
con.close()