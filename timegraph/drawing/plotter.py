class Plotter():

    def __init__(self):
        self.height = 10
        self.width = 40

    def plot_timeseries(self, value_list):
        #print(value_list)
        x_values = self.scale_values(value_list)
        #print(x_values)

        matrix = self.generate_matrix(x_values)
        self.print_matrix(matrix)

    def scale_values(self, value_list):
        result = []
        z = [abs(i) for i in value_list]
        for i in value_list:
            temp = i / float(max(z))
            temp2 = temp * self.height - 1
            result.append(int(temp2))
        return result

    def generate_matrix(self, values):
        matrix = [[' ' for x in range(self.width)] for y in range(self.height)]

        for index, value in enumerate(values):
            # print('i: ', index, ' v: ', value)
            matrix[value][index] = '*'
        return matrix

    def print_matrix(self, matrix):
        #print('y_length: ', len(matrix))
        #print('x_length: ', len(matrix[0]))

        for point_y in reversed(range(len(matrix))):
            for point_x in range(len(matrix[0])):
                #print(point_x, ',', point_y)
                print(matrix[point_y][point_x], end='')
            print('')