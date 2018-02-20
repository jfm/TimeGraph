from influxdb.resultset import ResultSet
from timegraph.drawing.drawing import Drawing


class TestDrawing:

    def setup(self):
        self.test_result_set = ResultSet(
            {'series': [{'values': [['value', 'integer']],
                         'name': 'cpu',
                         'columns': ['fieldKey', 'fieldType']},
                        {'values': [['value', 'integer']],
                         'name': 'iops',
                                 'columns': ['fieldKey', 'fieldType']},
                        {'values': [['value', 'integer']],
                         'name': 'load',
                         'columns': ['fieldKey', 'fieldType']},
                        {'values': [['value', 'integer']],
                         'name': 'memory',
                         'columns': ['fieldKey', 'fieldType']}]})

        self.dummy_points = [
            {
                "measurement": "cpu_load_short",
                "tags": {
                    "host": "server01",
                    "region": "us-west"
                },
                "time": "2009-11-10T23:00:00.123456Z",
                "fields": {
                    "value": 0.64
                }
            },
            {
                "measurement": "cpu_load_short",
                "tags": {
                    "host": "server01",
                    "region": "us-west"
                },
                "time": "2009-11-11T23:00:00.123456Z",
                "fields": {
                    "value": 0.64
                }
            }
        ]

    def test_get_value_list(self):
        self.drawing = Drawing()
        self.drawing.get_value_list(self.dummy_points)
