import table
from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    group_id_fn: int

class Students(table.Table):
    def __init__(self):
        super().__init__("students",
                         {"id": "INT NOT NULL PRIMARY KEY",
                          "name": "VARCHAR(255) NOT NULL",
                          "group_id_fn": "INT"},
                         ["FOREIGN KEY (group_id_fn) REFERENCES groups (id) ON DELETE SET NULL ON UPDATE CASCADE"]
                         )

    def create(self, student: Student) -> None:
        super().create(student.__dict__)

    def select_all(self) -> list[Student] | None:
        result = []
        rows = super().select(f"SELECT * FROM {self.table_name}")

        for row in rows:
            result.append(Student(*row))

        return result
