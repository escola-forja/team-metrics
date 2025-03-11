from typing import Iterable
import matplotlib.pyplot as plt

from src.models import Task


def plot(tasks: Iterable[Task]):
    plt.figure(figsize=(10, 6))
    plt.hist([task.lead_time.days for task in tasks if task.is_valuable()])

    plt.title('Tamanho das tarefas -vs- Quantidade de tarefas')
    plt.xlabel('Lead Time (dias)')
    plt.ylabel('Quantidade de tarefas')

    plt.show()