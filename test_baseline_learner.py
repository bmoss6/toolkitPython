from unittest import TestCase
from baseline_learner import BaselineLearner
from matrix import Matrix


class TestBaselineLearner(TestCase):

    labels = Matrix()
    labels.load_arff("tests/cm1_req.arff")
    l = BaselineLearner()

    def test_train(self):
        self.l.train(Matrix(), self.labels)
        self.assertAlmostEqual(self.l.labels[0], 1.426966, places=4)

    def test_predict(self):
        self.l.train(Matrix(), self.labels)
        labels = []
        self.l.predict([], labels)

        self.assertListEqual(self.l.labels, labels)
