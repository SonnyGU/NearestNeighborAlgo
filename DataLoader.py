import csv


class DataLoader:
    #  loads csv files
    @staticmethod
    def load_csv(filename):
        with open(filename, 'r') as file:
            return list(csv.reader(file))

