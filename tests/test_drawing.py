from nose.tools import assert_equal
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
                "cpu_load": 0.50,
                "time": "2009-11-10T23:00:00.123456Z",
            },
            {
                "cpu_load": 0.50,
                "time": "2009-11-10T23:00:00.123456Z",
            },
            {
                "cpu_load": 0.50,
                "time": "2009-11-10T23:00:00.123456Z",
            }
        ]

    def test_get_value_list(self):
        drawing = Drawing()
        result = drawing.get_value_list(self.dummy_points)
        assert_equal(len(result), 3)
