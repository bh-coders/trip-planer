import sqlite3 as db

from backend.src.attraction.interfaces.repository import Repository


# TODO all of this to delete
class SQLRepository(Repository):
    def __init__(self, connection_string):
        self._connection_string = connection_string
        self._connection = db.connect(connection_string)

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM items")
        results = cursor.fetchall()
        return results

    def get_by_id(self, item_id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM items WHERE id=?", (item_id,))
        result = cursor.fetchone()
        return result if result is not None else None

    def create(self, item):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO items(name, description) VALUES (?, ?)",
            (item["name"], item["description"]),
        )
        self._connection.commit()
        item["id"] = cursor.lastrowid
        return item

    def update(self, item):
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE items SET name=?, description=? WHERE id=?",
            (item["name"], item["description"], item["id"]),
        )
        self._connection.commit()
        return cursor.rowcount > 0

    def delete(self, item_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
        self._connection.commit()
        return cursor.rowcount > 0
