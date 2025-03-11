from src.charts import burnup, histogram, scatter, monte_carlo
from src.cmd import parse_args
from src.parser import read_tasks

if __name__ == '__main__':
    args = parse_args()

    tasks = read_tasks(path=args.input)

    histogram.plot(tasks)
    scatter.plot(tasks)
    burnup.plot(tasks)
    monte_carlo.plot(tasks)
