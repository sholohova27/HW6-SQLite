import table
from dataclasses import dataclass

@dataclass
class Lector:
    id: int
    name: str


class Lectors(table.Table):
    def __init__(self):
        super().__init__("lectors",
                         {"id": "INT NOT NULL PRIMARY KEY",
                          "name": "VARCHAR(255) NOT NULL"
                          },
                         []
                         )

    def create(self, lector: Lector) -> None:
        super().create(lector.__dict__)

    def select_all(self) -> list[Lector] | None:
        result = []
        rows = super().select(f"SELECT * FROM {self.table_name}")

        for row in rows:
            result.append(Lector(*row))

        return result