from ascii_graph import Pyasciigraph


class Drawing:

    def __init__(self):
        self.graphtool = Pyasciigraph()

    def create_graph(self, db_response):
        value_key = self.get_value_key(db_response)
        if value_key is not None:
            value_list = self.get_value_list(db_response.get_points(), value_key)
        else:
            raise DrawingException(100, 'Could not determine value key')

        # Create graph
        return self.graphtool.graph('test', value_list)

    def get_value_key(self, result_set):
        result = ""

        for point in result_set.get_points():
            point_keys = point.keys()
            if not len(point_keys) > 2:
                for key in point_keys:
                    if key != 'time':
                        result = key
                        break
            else:
                result = None
            break

        return result

    def get_value_list(self, points, key):
        filtered_points = list(filter(lambda point: point[key] is not None, points))
        return [(point['time'], point[key]) for point in filtered_points]

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