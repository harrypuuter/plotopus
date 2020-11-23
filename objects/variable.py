import logging
logger = logging.getLogger(__name__)
from rich.console import Console
from rich.table import Table
from rich import box


class Variable(object):
    def __init__(self, label, variablestring, binning=None):
        self.name = label
        self.varstring = variablestring
        if binning is None:
            binning = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.binning = binning
        self.available = True
        self.table = self.build_details_table()

    def build_details_table(self):
        table = Table(box=box.MINIMAL)
        table.add_column("Parameter", justify="right", style="cyan", no_wrap=True)
        table.add_column("Configuration", style="magenta")

        table.add_row("name", self.name)
        table.add_row("varstring", self.varstring)
        table.add_row("available", str(self.available))
        table.add_row("binning", str(self.binning))
        return table

    def __repr__(self):
        console = Console()
        console.print(self.table)
        return ""
    #     printout = """ --- Configuration of Variable {var} --- \n| --> name:    {var}\n| --> varstring:      {varstring}\n| --> binning:    {binning}\n| --> available:    {avail}\n---------------------------------------------
    #    """.format(var=self.name, varstring=self.varstring, binning=self.binning, avail=self.available)
    #     return printout

    def add_binning(self, binning):
        self.binning = binning

    def set_unavailable(self):
        self.available = False

