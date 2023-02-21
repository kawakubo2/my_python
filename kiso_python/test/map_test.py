# -*- coding: utf-8 -*-

label_list = ['Iris-setosa',
              'Iris-versicolor',
              'Iris-versinica',
              'Iris-versinica',
              'Iris-versicolor',
              'Iris-setosa',
              'Iris-setosa',
              'Iris-versinica',
              'Iris-versicolor',
              'Iris-versicolor',
              'Iris-versicolor',
              'Iris-versinica',
              'Iris-setosa',
              'Iris-versicolor',
              'Iris-versinica',
              'Iris-versicolor']

labels = {
       'Iris-setosa': [1, 0, 0],
       'Iris-versicolor': [0, 1, 0],
       'Iris-versinica': [0, 0, 1]
}

result = list(map(lambda v: labels[v], label_list))
print(result)