import table
from dataclasses import dataclass

@dataclass
class Subject:
    id: int
    name: str
    lector_id_fn: int



class Subjects(table.Table):
    def __init__(self):
        super().__init__("subjects",
                         {"id": "INT NOT NULL PRIMARY KEY",
                          "name": "VARCHAR(255) NOT NULL",
                          "lector_id_fn": "INT"
                          },
                         ["FOREIGN KEY (lector_id_fn) REFERENCES lectors (id) ON DELETE SET NULL ON UPDATE CASCADE"]
                         )

    def create(self, subject: Subject) -> None:
        super().create(subject.__dict__)


    def select_all(self) -> list[Subject] | None:
        result = []
        rows = super().select(f"SELECT * FROM {self.table_name}")

        for row in rows:
            result.append(Subject(*row))

        return result