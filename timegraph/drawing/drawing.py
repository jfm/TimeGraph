from numbers import Number
from timegraph.drawing.plotter import Plotter


class Drawing:

    def __init__(self):
        self.plotter = Plotter()

    def create_graph(self, title, db_response):
        value_list = self.get_value_list(db_response.get_points())

        self.plotter.plot_timeseries(value_list)

    def get_value_list(self, points):

        result = []
        for point in points:
            point_keys = point.keys()
            for key in point_keys:
                if key != 'time':
                    if (point[key] is not None and
                            isinstance(point[key], Number)):
                        result.append(point[key])

        return result

    def print_graph(self, lines):
        for line in lines:
            print(line)


class DrawingException(Exception):
    def __init__(self, code, message):
        super().__init__(code, message)
        self.code = code
        self.message = message
