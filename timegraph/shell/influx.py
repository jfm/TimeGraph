from cmd import Cmd
from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError
from influxdb.exceptions import InfluxDBClientError
from timegraph.drawing.drawing import Drawing, DrawingException
import json


class InfluxShell(Cmd):
    prompt = 'query> '

    def __init__(self, db_host, db_port, db_name):
        super().__init__()
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.client = InfluxDBClient(
            host=db_host, port=db_port, database=db_name)
        self.drawing = Drawing()

    def do_auth(self, line):
        args = line.split(' ')
        dbuser = args[0]
        dbpass = args[1]
        self.client.switch_user(dbuser, dbpass)

    def do_select(self, line):
        query = 'select ' + line
        if not query.endswith(';'):
            query = query + ';'

        try:
            response = self.client.query(query)
            self.drawing.create_graph(query, response)

        except ConnectionError as conn_error:
            self.connection_error_handler(conn_error)
        except InfluxDBClientError as error:
            self.influx_error_handler(error.code, error.content)
        except DrawingException as drawing_error:
            self.graphtool_error_handler(
                drawing_error.code, drawing_error.message)

    def do_list(self, line):
        print('list - Not implemented yet')

    def do_import(self, line):
        print('improt - Not implemented yet')
        # Convert input(file) to valid json
        # self.client.write_points(json)

    def do_create_db(self, line):
        response = self.client.create_database(line)
        print(response)

    def do_disconnect(self, line):
        return True

    def do_EOF(self, line):
        return True

    def default(self, line):
        print('Unrecognized command')
        print(' ', line)

    def main(self):
        InfluxShell.cmdloop(self, intro='Connected to Influx Query Shell')

    def connection_error_handler(self, exception):
        print('Could not connect to {0} on {1}:{2}'.format(
            self.db_name, self.db_host, self.db_port))

    def influx_error_handler(self, code, content):
        if code is None:
            print(content)
        else:
            contentJson = json.loads(content)
            print(code, ' -- ', contentJson['error'])

    def graphtool_error_handler(self, code, message):
        print(code, ' -- ', message)

# select count(water_level) from h2o_feet
# select * from h2o_feet limit 5
# select field(value) from h2o_feet limit 5
# select water_level from h2o_feet limit 5
# select mean("water_level") from h2o_feet group by time(1d) limit 100

# curl https://s3.amazonaws.com/noaa.water-database/NOAA_data.txt
# -o NOAA_data.txt
# influx -import -path=NOAA_data.txt -precision=s -database=testdb
