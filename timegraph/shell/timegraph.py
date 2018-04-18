from cmd import Cmd
from timegraph.shell.influx import InfluxShell


class TimeGraphShell(Cmd):
    prompt = 'timegraph>'

    def __init__(self):
        super().__init__()

    def do_connect(self, line):
        args = line.split(' ')
        if len(args) < 4:
            self.print_help_missing_args()
        else:
            db_type = args[0]
            db_host = args[1]
            db_port = args[2]
            db_name = args[3]
            if db_type == 'influx':
                influx_shell = InfluxShell(db_host, db_port, db_name)
                influx_shell.main()
            else:
                self.print_help_influx_only()

    def help_connect(self):
        self.print_help_missing_args()

    def main(self):
        TimeGraphShell.cmdloop(self, intro='TimeGraph Shell')

    def do_EOF(self, line):
        return True

    def do_exit(self, line):
        return True

    def print_help_missing_args(self):
        print('connect takes the following arguments:')
        print('  connect <dbtype> <host> <port> <db>')
        print('Example:')
        print('  connect influx localhost 8086 exampledb')

    def print_help_influx_only(self):
        print('Only the dbtype "influx" is currently supported')
