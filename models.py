# Popular convention by ORM developers
import psycopg2
# Singular form of a class name to represent a table 
# table will be mostly plural


connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="flask_intro",
)

cur = connection.cursor()


class Reminder:

    # constructor?
    # SERIAL  data types -- numbers that are increased 1, 2, 3
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    def save(self):
        """
        Stores the values of title and description in the table
        """
        cur.execute(f"""INSERT INTO reminders (title, description) 
            VALUES('{self.title}', '{self.description}') RETURNING id, title, description""")
        # persist the changes
        connection.commit()

        values = cur.fetchone()
        print(values)

        # Return the instance 