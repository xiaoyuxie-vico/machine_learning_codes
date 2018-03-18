# -*- coding:utf-8 -*-

"""
Created on 2018年3月17日
@author: Vico Xie
@email: xiaoyuxie.vico@gmail.com
Code for 'Statistical learning method', Hang Li, 2017, p29, example 2.1
"""

import numpy as np


class Perception:
    """
    Using perception method to process the dataset in order to get the best parameters. 
    """
    def __init__(self, dataset, lebls):
        self.dataset = dataset
        self.labels = labels
        self.w = np.zeros(dataset[0].shape[0])
        self.b = 0
        self.update_num = 0
        self.update_flag = True

    def check_parameters_correction(self):
        """
        Check whether the parameters are correct.
        """
        result_sum = self.label * (np.sum(self.w * self.point) + self.b)

        if result_sum > 0:
            self.check_result = True
        else:
            self.check_result = False

    def update_patematers(self):
        """
        Update the parameters.
        """
        self.w = self.w + self.label * self.point
        self.b = self.b + self.label

    def iteration(self):
        """
        Iteration
        """
        self.update_flag = False

        for num, self.point in enumerate(self.dataset):

            self.label = self.labels[num]
            self.check_parameters_correction()
            # print '\t[INFO] point: {}, label: {}, check_result: {}, w: {}, b: {}'.format(self.point, self.label, self.check_result, self.w, self.b)

            if self.check_result == False:

                self.update_patematers()
                self.update_flag = True
                self.update_num += 1

    def get_best_parameters(self):
        """
        Iterate to get the best parameters.
        """
        while self.update_flag == True:
            self.iteration()

        print 'The times of update parameters: {}'.format(self.update_num)
        print 'The best parameters: w: {}; b: {}'.format(self.w, self.b)


if __name__ == '__main__':

    # dataset
    dataset = np.array([[3, 3], [4, 3], [1, 1]])
    labels = np.array([1, 1, -1])

    perception = Perception(dataset, labels)
    perception.get_best_parameters()

    