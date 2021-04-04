from abc import ABC, abstractmethod
import os
import re
import random as rnd


def pick_from_roll_options(result):
    return rnd.choice(result.split("/"))


def roll(dice_string):
    instructions = []
    dice_string


def roll(dice_number, dice_type):
    return [rnd.randint(1, dice_type) for i in range(dice_number)]


class TableRoller:
    def __init__(self, dir_path):
        self.path = dir_path
        self.files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        self.tables = dict()
        for file in self.files:
            table = self.parse_table(dir_path, file)
            self.tables[table.name] = table

    @staticmethod
    def parse_table(dir_path, filename):
        simple_match = re.match("(.*)\.txt$", filename)
        if simple_match:
            return SimpleTable(dir_path, filename, simple_match.group(1))
        range_match = re.match("(.*)range\.txt$", filename)
        if range_match:
            return SimpleTable(dir_path, filename, range_match.group(1))
        composite_match = re.match("(.*)\.csv$", filename)
        if composite_match:
            return SimpleTable(dir_path, filename, composite_match.group(1))

    def roll(self, table_name):
        return self.tables[table_name].roll()


class RandomTable(ABC):
    def __init__(self, path, filename, table_name):
        self.table = self.parse_table(path, filename)
        self.validate_table()
        self.name = table_name

    @abstractmethod
    def roll(self):
        raise NotImplementedError

    @abstractmethod
    def parse_table(self, path, filename):
        raise NotImplementedError

    def validate_table(self):
        pass


class SimpleTable(RandomTable):

    def parse_table(self, path, filename):
        with open(os.path.join(path, filename)) as f:
            table = [line.strip() for line in f.readlines()]
        return table

    def roll(self):
        return rnd.choice(self.table)


class CompositeTable(RandomTable):

    def roll(self):
        raise NotImplementedError

    def parse_table(self, path, filename):
        raise NotImplementedError


class RangeTable(RandomTable):

    def roll(self):
        raise NotImplementedError

    def parse_table(self, path, filename):
        raise NotImplementedError
