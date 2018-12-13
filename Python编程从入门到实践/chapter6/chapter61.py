class Practise:

    allen_0 = {'color': 'green', 'points': 5, 'clothColor': 'green'}
    allens = []

    def dist_test(self):

        self.allen_0['x_position'] = 0
        self.allen_0['y_position'] = 25
        print(self.allen_0)

    def dist_delete(self, key):

        del self.allen_0[key]
        print(self.allen_0)

    def dist_loop(self):

        print(self.allen_0.items())

        for k, v in self.allen_0.items():
            print('\nKey:' + k)
            print('Value:' + str(v))

    def dist_keys(self):

        for key in self.allen_0.keys():
            print(key.title())

    def dist_except(self):

        if 'name' not in self.allen_0.keys():
            print('this is not in keys')

    def dist_sort(self):

        for key in sorted(self.allen_0.keys()):
            print(key)

    def dist_values(self):

        for value in self.allen_0.values():
            print(value)

    def dist_values_single(self):

        for value in set(self.allen_0.values()):
            print(value)

    def dist_allens(self):

        for allen_number in range(30):
            new_allen = {'color': 'black', 'name': 'zhg', 'age': allen_number}
            self.allens.append(new_allen)
        else:
            print(self.allens)


allen = Practise()
allen.dist_test()
# allen.dist_delete('color')
allen.dist_loop()
allen.dist_keys()
allen.dist_except()
allen.dist_sort()
allen.dist_values()
allen.dist_values_single()
allen.dist_allens()
