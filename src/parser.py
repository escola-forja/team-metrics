import csv
from datetime import datetime
from typing import Iterable

from src.models import Task


def read_tasks(path: str) -> Iterable[Task]:
    tasks = []
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            started_at = datetime.strptime(row['Finished at'], '%Y-%m-%d %H:%M:%S')
            done_at = datetime.strptime(row['Started at'], '%Y-%m-%d %H:%M:%S')

            tasks.append(Task(
                uid=row['UID'],
                type_=row['Type'],
                started_at=started_at,
                done_at=done_at,
                lead_time=started_at - done_at
            ))

    return tasks
