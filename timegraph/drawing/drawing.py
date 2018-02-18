import numbers

import dateutil.parser as dp
from ascii_graph import Pyasciigraph
from timegraph.drawing.plotter import Plotter


class Drawing:

    def __init__(self):
        self.graphtool = Pyasciigraph()
        self.plotter = Plotter()

    def create_graph(self, title, db_response):
        value_list = self.get_value_list(db_response.get_points())

        self.plotter.plot_timeseries(value_list)

        # Create graph
        #return self.graphtool.graph(title, value_list)

    def get_value_list(self, points):
        # filtered_points = list(filter(lambda point: point[key] is not None, points))

        result = []
        for point in points:
            point_keys = point.keys()
            for key in point_keys:
                if key != 'time':
                    if point[key] is not None and isinstance(point[key], numbers.Number):
                        result.append(point[key])

        return result
        # return [(point['time'], point[key]) for point in filtered_points]

    def print_graph(self, lines):
        for line in lines:
            print(line)


class DrawingException(Exception):
    def __init__(self, code, message):
        super().__init__(code, message)
        self.code = code
        self.message = message

### Code definitions
# 100 series is problems converting query to x/y value list
