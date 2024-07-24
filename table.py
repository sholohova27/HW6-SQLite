import typing
from typing import Iterable, Any, Union
import sqlite3
import logging

column_name = str
column_type = str

class Table:
    conn: sqlite3.Connection = None

    def __init__(self,
                 table_name: str,
                 columns: typing.Dict[column_name, column_type],
                 constrains: typing.List[str]):
        self.table_name = table_name
        self.columns = columns
        self.constrains = constrains

        values = [f"{key} {value}" for key, value in self.columns.items()]
        values.extend(constrains)
        values_str = ", ".join(values)

        sql_request = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({values_str})"
        logging.debug(sql_request)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_request)
            self.conn.commit()
        except sqlite3.Error as e:
            logging.debug(e)
        finally:
            cursor.close()

    def create(self, obj_dict: typing.Dict[str, typing.Any]):
        columns = ", ".join(self.columns.keys())
        rows_pattern = ", ".join(["?" for _ in self.columns.keys()])
        sql_request = f"INSERT INTO {self.table_name} ({columns}) VALUES ({rows_pattern})"
        logging.debug(sql_request)

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_request, list(obj_dict.values()))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.debug(e)
        finally:
            cursor.close()

    def select(self, query) -> Union[Iterable[Any], None]:
        rows = None
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            cursor.close()
        return rows





