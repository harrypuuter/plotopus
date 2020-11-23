import matplotlib.pyplot as plt
from utils.validators import save_create_folder


class Plotter(object):
    def __init__(self):
        self.name = "default"
        self.plotobject = plt.figure()
        self.outputpath = save_create_folder("output")

    @classmethod
    def style(self, **plot_options):
        pass

    @classmethod
    def add_legend(self, plot):
        pass

    @classmethod
    def draw_plot(self, plot):
        pass

    def set_outputpath(self, outputpath):
        self.outputpath = save_create_folder("outputpath")

    def make_plot(self, plot):
        self.style()
        self.draw_plot(plot)
        self.add_legend(plot)
        self.save_plot(plot)
        pass

    def save_plot(self, plot):
        self.plotobject.tight_layout()
        self.plotobject.savefig("{}/{}.pdf".format(self.outputpath, plot.name))
        self.plotobject.savefig("{}/{}.png".format(self.outputpath, plot.name))


class HistogramPlotter(Plotter):
    def __init__(self):
        super().__init__(self)
        self.type = "hist"
        self.stacked = True

    def style(self, **plot_options):
        pass

    def draw_plot(self, plot):
        dataset = [plotline.data.to_numpy() for plotline in plot.plotlines]
        colors = [plotline.color() for plotline in plot.plotlines]
        self.plotobject.hist(
            dataset, plot.binning, histtype="bar", stacked=self.stacked, color=colors
        )

    def add_legend(self, plot):
        labeldict = {}
        for i, plotline in enumerate(self.plotlines):
            labeldict["label{}".format(i)] = plotline.name
        self.plotobject.legend(plot)
