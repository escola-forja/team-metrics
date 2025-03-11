from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt

from src.models import Task


def plot(tasks: Iterable[Task]) -> None:
    historical_lead_times = [task.lead_time.days for task in tasks]

    # Actual simulation
    simulated_lead_times = np.random.choice(historical_lead_times, size=10_000, replace=True)

    percentiles = {
        'p50 (mediana)': {
            'value': np.percentile(simulated_lead_times, 50),
            'color': 'green',
        },
        'p80': {
            'value': np.percentile(simulated_lead_times, 80),
            'color': 'purple',
        },
        'p90': {
            'value': np.percentile(simulated_lead_times, 90),
            'color': 'red',
        }
    }

    plt.figure(figsize=(10, 6))
    plt.hist(simulated_lead_times, bins=30, alpha=0.7, color='blue', edgecolor='black')

    for label, percentile in percentiles.items():
        plt.axvline(percentile['value'], linestyle='dashed', linewidth=2, color=percentile['color'], label=f'{label}: {round(percentile['value'])} dias')

    plt.xlabel('Lead Time (dias)')
    plt.ylabel('Frequência')
    plt.title('Simulação de Monte Carlo (previsão de Lead Time)')
    plt.legend()

    plt.show()
