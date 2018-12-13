import matplotlib.pyplot as plt


class Draw:

    @staticmethod
    def draw_line_show_infos():
        input_values = [1, 2, 3, 4, 5]
        squares = [1, 4, 9, 16, 25]
        plt.plot(input_values, squares, linewidth=5)
        plt.title("Square Numbers", fontsize=24)
        plt.xlabel("Value", fontsize=14)
        plt.ylabel("Square of Value", fontsize=14)
        plt.tick_params(axis='both', labelsize=14)
        plt.show()

    @staticmethod
    def draw_point_show():
        plt.scatter(2, 4)
        plt.show()


# Draw.draw_line_show_infos()
Draw.draw_point_show()

