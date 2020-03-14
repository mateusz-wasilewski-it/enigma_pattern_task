import _sqlite3

class Database:
    def __init__(self):
        self.conn = _sqlite3.connect("flick_images.db")
        self.cursor = self.conn.cursor()

    def createTable(self):
        with self.conn:
            self.cursor.execute("""CREATE TABLE  images_urls
                    (
                    url text
                    )""")

    def add_image(self, url_):
        with self.conn:
            self.cursor.execute("""Insert into images_urls values (?)""", (url_,))

    def select_all(self):
        urls = []
        with self.conn:
            print(self.cursor.execute("""Select  * from images_urls"""))
            rows = self.cursor.fetchall()

            for row in rows:
                print(row[0])
                urls.append(row[0])


        return urls

    def close(self):
        self.cursor.close()
        self.conn.close()


