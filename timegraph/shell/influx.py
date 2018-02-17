from cmd import Cmd
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
from timegraph.drawing.drawing import Drawing, DrawingException
import json


class InfluxShell(Cmd):
    prompt = 'query> '

    def __init__(self):
        super().__init__()
        self.client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'NOAA_water_database')
        self.drawing = Drawing()

    def do_select(self, line):
        query = 'select ' + line
        if not query.endswith(';'):
            query = query + ';'

        try:
            response = self.client.query(query)
            graph = self.drawing.create_graph(response)
            self.drawing.print_graph(graph)

        except InfluxDBClientError as error:
            self.influx_error_handler(error.code, error.content)
        except DrawingException as drawing_error:
            self.graphtool_error_handler(drawing_error.code, drawing_error.message)

    def do_list(self):
        print('list - Not implemented yet')

    def do_create_db(self, line):
        response = self.client.create_database(line)
        print(response)

    def default(self, line):
        print('Unrecognized command')
        print(' ', line)

    def do_EOF(self, line):
        return True

    def main(self):
        InfluxShell.cmdloop(self, intro='TimeGraph - Influx Query Shell')

    def influx_error_handler(self, code, content):
        contentJson = json.loads(content)
        print(code, ' -- ', contentJson['error'])

    def graphtool_error_handler(self, code, message):
        print(code, ' -- ', message)

# select count(water_level) from h2o_feet
# select * from h2o_feet limit 5
# select field(value) from h2o_feet limit 5
# select water_level from h2o_feet limit 5
# select mean("water_level") from h2o_feet group by time(1d) limit 100

# curl https://s3.amazonaws.com/noaa.water-database/NOAA_data.txt -o NOAA_data.txt
# influx -import -path=NOAA_data.txt -precision=s -database=testdb
