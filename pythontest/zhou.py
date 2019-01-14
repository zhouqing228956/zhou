# -*- coding: utf-8 -*-

import unittest
from typing import Any


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score<0 or self.score >100:
            raise ValueError
        elif self.score >= 60 and self.score < 80  :
            return 'B'
        elif self.score >= 80 :
            return 'A'
        else:
            return 'C'

class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')
        print(s1.get_grade())
        print(s2.get_grade())

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

    def zhou():
        L = [(1, 2, 3), (3, 4, 5), (3, 1, 1)]
        for s in L:
            yield {
                'd': s[0],
                'k': s[1],
                'p': s[2]
            }
if __name__ == '__main__':
    unittest.main()



