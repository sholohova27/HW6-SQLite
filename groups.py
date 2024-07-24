import table
from dataclasses import dataclass

@dataclass
class Group:
    id: int
    name: str

class Groups(table.Table):
    def __init__(self):
        super().__init__("groups",
                         {"id": "INT NOT NULL PRIMARY KEY",
                          "name": "VARCHAR(255) NOT NULL"
                          },
                         []
                         )

    def create(self, group: Group) -> None:
        super().create(group.__dict__)

    def select_all(self) -> list[Group] | None:
        result = []
        rows = super().select(f"SELECT * FROM {self.table_name}")

        for row in rows:
            result.append(Group(*row))

        return result

