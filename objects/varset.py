import logging
import yaml
logger = logging.getLogger(__name__)
from objects.variable import Variable
from rich import print
from rich.console import Console
from rich.table import Table


class Varset(object):
    def __init__(self, setname, sample=None):
        self.setname = setname
        self.samples = []
        self.variables = []
        self.binning_dict = yaml.load(open("data/binning.yaml"),
                                      Loader=yaml.FullLoader)["variable"]

    def add_variable(self, label, variablestring, binning=[]):
        if len(binning) == 0:
            try:
                binning = self.binning_dict[label]
            except KeyError:
                binning = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
                logger.warning("Using default binning {}".format(binning))
        var = Variable(label, variablestring, binning)
        self.variables.append(var)

    def all_names(self):
        return [var.name for var in self.variables]

    def available_names(self):
        return [var.name for var in self.variables if var.available]

    def available_varstrings(self):
        return [var.varstring for var in self.variables if var.available]

    def get_variable(self, name):
        temp = list(filter(lambda x: x.name == name, self.variables))
        if len(temp) == 1:
            return temp[0]
        else:
            print("Variable {} not found in Varset {}".format(
                name, self.setname))

    def __repr__(self):
        table = Table(title=self.setname)

        table.add_column("Number", justify="right", style="cyan", no_wrap=True)
        table.add_column("Variable", style="magenta")
        for i, var in enumerate(self.variables):
            table.add_row(str(i), var.name)
        console = Console()
        console.print(table)
        return ""

    def print_details(self, console):
        for i, var in enumerate(self.variables):
            console.print(var.table)

    def link_to_sample(self, sample):
        self.samples.append(sample)