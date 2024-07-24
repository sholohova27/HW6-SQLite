import table
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Mark:
    id: int
    value: int
    subject_id_fn: int
    student_id_fn: int
    created_at: datetime = field(default_factory=datetime.now)



class Marks(table.Table):
    def __init__(self):
        super().__init__("marks",
                         {"id": "INT NOT NULL PRIMARY KEY",
                          "value": "INT NOT NULL",
                          "subject_id_fn": "INT",
                          "student_id_fn": "INT",
                          "created_at": "DATETIME DEFAULT CURRENT_TIMESTAMP"},
                         ["FOREIGN KEY (subject_id_fn) REFERENCES subjects (id) ON DELETE SET NULL ON UPDATE CASCADE",
                          "FOREIGN KEY (student_id_fn) REFERENCES students (id) ON DELETE CASCADE ON UPDATE CASCADE"]
                         )

    def create(self, mark: Mark) -> None:
        super().create(mark.__dict__)

    def select_all(self) -> list[Mark] | None:
        result = []
        rows = super().select(f"SELECT * FROM {self.table_name}")

        for row in rows:
            result.append(Mark(*row))

        return result