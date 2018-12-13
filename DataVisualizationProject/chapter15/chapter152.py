import matplotlib.pyplot as plt


class Draw:

    @staticmethod
    def draw_line():

        input_value = [1, 2, 3, 4, 5]
        square = [1, 4, 9, 16, 25]
        plt.plot(input_value, square, linewidth=5)
        plt.title('Square Numbers', fontsize=24)
        plt.xlabel('Value', fontsize=14)
        plt.ylabel('Square of Value', fontsize=14)
        plt.tick_params(axis='both', labelsize=14)
        plt.show()

    @staticmethod
    def draw_point():

        x_values = [1, 2, 3, 4, 5]
        y_values = [1, 4, 9, 16, 25]
        plt.scatter(x_values, y_values, s=100)
        plt.title('Square Numbers', fontsize=24)
        plt.xlabel('Value', fontsize=14)
        plt.ylabel('Square of Value', fontsize=14)
        plt.tick_params(axis='both', labelsize=24)
        plt.show()

    @staticmethod
    def draw_points():

        x_values = list(range(1, 1001))
        y_values = [x ** 2 for x in x_values]
        plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=20)
        plt.title('Square Numbers', fontsize=24)
        plt.xlabel('Value', fontsize=14)
        plt.ylabel('Square of Value', fontsize=14)
        plt.tick_params(axis='both', labelsize=24)
        plt.axis([0, 1100, 0, 1100000])
        # plt.show()
        plt.savefig('square_plot.png', bbox_inches='tight')

# Draw.draw_line()
# Draw.draw_point()


Draw.draw_points()
