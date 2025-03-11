import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Team metrics CSV path.")
    parser.add_argument("input", type=Path, help="CSV file path")
    return parser.parse_args()
