from datetime import datetime, timedelta
from typing import Iterable

from matplotlib import pyplot as plt

from src.models import Task


def plot(tasks: Iterable[Task]) -> None:
    start_at = min(tasks, key=lambda t: t.done_at).done_at.date()
    end_at = max(tasks, key=lambda t: t.done_at).done_at.date()

    current_date = start_at
    done_tasks_by_date = []
    dates = []
    while current_date <= end_at:
        dates.append(current_date)
        done_tasks_by_date.append(len([t for t in tasks if t.done_at.date() <= current_date]))
        current_date += timedelta(days=1)

    plt.figure(figsize=(10, 6))
    plt.plot(dates, done_tasks_by_date)

    # Labeling axes
    plt.xlabel('Data da entrega')
    plt.ylabel('Quantidade de entregas')

    plt.title(f'Burn Up')
    plt.xticks(rotation=20)  # 20 degrees inclination

    plt.show()