import pandas
import numpy as np


class Plot(object):
    def __init__(self, name, variablename, plotlines=[]):
        self.name = name
        self.variablename = variablename
        self.plotlines = []
        self.samples = []
        self.binning = []

    # def add_plotline(self, plotline):
    #     self.plotlines.append(plotline)

    def add_sample(self, sample):
        self.samples.append(sample)
        if len(self.binning) == 0:
            self.binning = sample.variables.get_variable(self.variablename).binning

    def collect_plotlines(self):
        for sample in self.samples:
            if sample.dataframe is None:
                sample.get_data()
            variable = sample.variables.get_variable(self.variablename)
            plotline = Plotline(sample, variable)
            plotline.add_data()
            self.plotlines.append(plotline)

    def style_plotline(self, name, styledict):
        matching = list(filter(lambda x: x.name == name, self.plotlines))
        for plotline in matching:
            plotline.define_style(styledict)


class Plotline(object):
    def __init__(self, sample, variable):
        self.sample = sample
        self.name = sample.name + variable.name
        self.color = "black"
        self.plotstyle = "line"
        self.linewidth = 1
        self.legendstyle = "line"
        self.data = None
        self.variable = variable
        self.histogram_array = None

    def define_style(self, styledict):
        for setting in styledict:
            try:
                result = getattr(self, "set_{}".format(setting))(styledict[setting])
            except AttributeError:
                available = [
                    func
                    for func in dir(self)
                    if callable(getattr(self, func)) and not func.startswith("__")
                ]
                print(
                    "This option is not available, available options are {}".format(
                        available
                    )
                )

    def set_color(self, color):
        self.color = color

    def set_plotstyle(self, plotstyle):
        self.plotstyle = plotstyle

    def set_linewidth(self, linewidth):
        self.linewidth = int(linewidth)

    def set_legendstyle(self, legendstyle):
        self.legendstyle = legendstyle

    def set_name(self, name):
        self.name = name

    def add_data(self):
        self.data = getattr(self.sample.dataframe, self.variable.varstring)
        self.histogram_array = np.histogram(self.data, bins=self.variable.binning)
