import uproot
import logging
from utils.validators import check_file_exists
from objects.varset import Varset
from rich import print
from rich.console import Console
from rich.table import Table
logger = logging.getLogger(__name__)

class Sample(object):
    def __init__(self, filename, samplename):
        self.filename = filename
        self.samplename = samplename
        self.dataframe = None
        self.variables = None
        self.selection = ""
        self.name = samplename
        self.varsetname = ""

    def add_varset(self, varset):
        self.variables = varset

    def generate_varset(self, varsetname):
        self.varsetname = varsetname
        self.variables = Varset(varsetname, self)

    def add_selection(self, selection_string):
        self.selection = selection_string

class RootNtuple(Sample):
    """
        Container for a Root ntuple file, requires
        filename - path to the root file
        samplename - name to identify the sample
        rootfolder - if existent, the folder within the root file that should be used
        tree - name of the roottree
        friends - list of friend trees to the original sample to be considered
    """
    def __init__(self, filename, samplename, folder, treename, friends=[]):
        super().__init__(filename, samplename)
        self.rootfolder = folder
        self.treename = treename
        self.friends = friends
        self.tree = None
        if self.rootfolder is not "":
            self.histhash = "{folder}/{tree}"
        else:
            self.histhash = "{tree}"
        self.keys = self.open_and_get_keys()

    def __repr__(self):
        table = Table(title=self.name)
        console = Console()
        table.add_column("Configuration", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        table.add_row("Samplename", str(self.samplename))
        table.add_row("File", str(self.filename))
        table.add_row("Folder", str(self.rootfolder))
        table.add_row("tree", str(self.treename))
        table.add_row("Friendfiles", str(self.friends))
        table.add_row("Variables", str(self.variables.all_names()))

        console.print(table)
        return ""

    def validate_varset(self):
        # TODO implement a check here to vaildate, if a quantity can be calculated
        logger.warning("Validation of variables not implemented yet")
        # missing = []
        # for variable in self.variables.all_names():
        #     if variable not in self.keys:
        #         logger.warning("{var} not available in {sample}/{hash}".format(var=variable, sample=self.samplename, hash=self.histhash))
        #         missing.append(variable)
        #         self.variables.get_variable.set_unavailable()
        # if len(missing) > 0:
        #     return False
        # else:
        #     return True

    def open_and_get_keys(self):
        pathhash = self.histhash.format(folder=self.rootfolder,
                                        tree=self.treename)
        check_file_exists(self.filename)
        self.tree = uproot.open(self.filename)[pathhash]
        return self.tree.keys()

    def get_data(self):
        self.validate_varset()
        self.dataframe = self.tree.pandas.df(self.variables.available_varstrings())
