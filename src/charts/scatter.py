from math import ceil
from typing import Iterable

import numpy as np
from matplotlib import pyplot as plt

from src.models import Task


def plot(tasks: Iterable[Task]) -> None:
    valuable_tasks = [task for task in tasks if task.is_valuable()]
    bug_tasks = [task for task in tasks if task.is_bug()]
    tech_tasks = [task for task in tasks if task.is_tech()]
    other_tasks = [task for task in tasks if
                   not task.is_tech() and not task.is_bug() and not task.is_valuable()]

    dates_valuable = [task.done_at for task in valuable_tasks]
    lead_times_valuable = [task.lead_time.total_seconds() / (24 * 3600) for task in valuable_tasks]
    p80 = ceil(max([lt for lt in lead_times_valuable if lt < np.percentile(lead_times_valuable, 80)], default=0))

    dates_bugs = [task.done_at for task in bug_tasks]
    dates_tech = [task.done_at for task in tech_tasks]
    dates_other = [task.done_at for task in other_tasks]
    lead_times_bugs = [task.lead_time.total_seconds() / (24 * 3600) for task in bug_tasks]
    lead_times_tech = [task.lead_time.total_seconds() / (24 * 3600) for task in tech_tasks]
    lead_times_other = [task.lead_time.total_seconds() / (24 * 3600) for task in other_tasks]

    plt.figure(figsize=(10, 6))
    plt.scatter(dates_bugs, lead_times_bugs, c='red', alpha=0.6, edgecolors='w', s=100, label='Bug')
    plt.scatter(dates_tech, lead_times_tech, c='green', alpha=0.6, edgecolors='w', s=100, label='Tech')
    plt.scatter(dates_other, lead_times_other, c='grey', alpha=0.6, edgecolors='w', s=100, label='Outro')
    plt.scatter(dates_valuable, lead_times_valuable, c='blue', alpha=0.8, edgecolors='w', s=200, label='Story/Task')
    plt.axhline(y=p80, color='red', linestyle='--', linewidth=2,
                label=f'p80: {p80:.0f} dias')

    # Labeling axes
    plt.xlabel('Data de entrega')
    plt.ylabel('Lead Time (dias)')

    # Title and legend
    plt.title('Data de entrega -vs- Lead Time')
    plt.legend()

    plt.xticks(rotation=20)  # 20 degrees inclination
    plt.show()