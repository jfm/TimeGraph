import shutil


class Plotter():

    def __init__(self, is_test=False):
        if not is_test:
            terminal_size = shutil.get_terminal_size()
            print(terminal_size)
            self.terminal_height = terminal_size[1]
            self.height = terminal_size[1] - 4
            self.terminal_width = terminal_size[0]
            self.width = terminal_size[0] - 5
        else:
            self.terminal_height = 10
            self.height = 10
            self.terminal_width = 40
            self.width = 40

    def plot_timeseries(self, value_list):
        scaled_values = self.scale_values(value_list)
        y_scale = self.get_y_scale(scaled_values)

        x_values = [scaled for (original, scaled) in scaled_values]

        matrix = self.generate_matrix(x_values)
        self.print_matrix(y_scale, matrix)

    def scale_values(self, value_list):
        result = []
        z = [abs(i) for i in value_list]
        for i in value_list:
            temp = i / float(max(z))
            temp2 = temp * self.height - 1
            result.append((i, int(temp2)))
        return result

    def generate_matrix(self, values):
        matrix = [[' ' for x in range(self.width)] for y in range(self.height)]
        splice_start = len(values) - self.width
        if splice_start > 0:
            values = values[splice_start:]

        for index, value in enumerate(values):
            matrix[value][index] = '*'
        return matrix

    def print_matrix(self, y_scale, matrix):

        self.print_line(self.terminal_width - 1)
        for point_y in reversed(range(len(matrix))):
            print(y_scale[point_y], end='')
            for point_x in range(len(matrix[0])):
                print(matrix[point_y][point_x], end='')
            print('')
        self.print_line(self.terminal_width - 1)

    def get_y_scale(self, values):
        original_values = [original for (original, scaled) in values]
        is_originals_floats = isinstance(original_values[0], float)
        scaled_values = [scaled for (original, scaled) in values]
        original_max = max(original_values)
        original_min = min(original_values)
        original_diff = original_max - original_min
        scaled_max = max(scaled_values)
        scaled_min = min(scaled_values)
        scaled_diff = scaled_max - scaled_min + 1

        scale = original_diff / scaled_diff
        y_scale = [0 for x in range(self.height)]
        next_value = original_max
        for index in reversed(range(self.height)):
            if is_originals_floats:
                value_string = '{0:.2f} '.format(next_value)
                y_scale[index] = value_string
            else:
                value_string = str(next_value)
                y_scale[index] = value_string.rjust(10)
            next_value -= scale

        return y_scale

    def print_line(self, length):
        for index in range(length):
            print('-', end='')
        print()
