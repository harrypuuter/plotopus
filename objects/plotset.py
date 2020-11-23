import logging
logger = logging.getLogger(__name__)


class Plotset(object):
    def __init__(self, setname):
        self.setname = setname
        self.samples = []
        self.plots = []

    def __repr__(self):
        printout = """
            --- Configuration of Plotset {setname} ---
            ---------------------------------------------
        """.format(setname=self.setname)
        for i, plot in enumerate(self.plots):
            printout += """
            | --> {i}. Plot:    {plot}
            """.format(i=i, var=plot.name)
        printout += """
            ---------------------------------------------
        """
        return printout

    def link_to_sample(self, sample):
        self.samples.append(sample)

    def build_plots(self, variables):
        for var in variables:
            plot = Plot(plotname, variable, plotlines=[]):