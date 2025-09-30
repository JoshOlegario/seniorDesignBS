import csv, time, os

class CsvLogger:
    def __init__(self, path="logs.csv"):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w", newline="") as f:
                csv.writer(f).writerow(["ts","event","value"])

    def log(self, event, value=None):
        with open(self.path, "a", newline="") as f:
            csv.writer(f).writerow([time.time(), event, value])
