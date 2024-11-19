import unittest

from solution import appearance


class TestSolution3(unittest.TestCase):
    def setUp(self) -> None:
        self.tests = [
            {'intervals': {'lesson': [1594663200, 1594666800],
                           'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                           'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
             'answer': 6300
             },
            {'intervals': {'lesson': [1594702800, 1594706400],
                           'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                                     1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                                     1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                                     1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579,
                                     1594706641],
                           'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
             'answer': 11410
             },
            {'intervals': {'lesson': [1594692000, 1594695600],
                           'pupil': [1594692033, 1594696347],
                           'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
             'answer': 8636
             },
        ]

    def test_main(self):
        for i, test in enumerate(self.tests):
            test_answer = appearance(test['intervals'])
            self.assertEqual(test_answer, test['answer'],
                             f'Error on test case {i}, got {test_answer}, expected {test["answer"]}')

    def test_data(self):
        self.assertEqual(type(self.tests), list)
        self.assertEqual(type(self.tests[0]), dict)
        self.assertEqual(type(self.tests[1]), dict)
        self.assertEqual(type(self.tests[2]), dict)
        with self.assertRaises(IndexError):
            self.assertEqual(type(self.tests[3]), dict)
        less_1_intervals = self.tests[0]['intervals']
        sum_lesson_1 = appearance(less_1_intervals)
        sum_ = 0
        for idx, item in enumerate(less_1_intervals['pupil']):
            if idx % 2 == 0:
                sum_ -= item
            else:
                sum_ += item
        for idx, item in enumerate(less_1_intervals['tutor']):
            if idx % 2 == 0:
                sum_ -= item
            else:
                sum_ += item
        # print(sum_)
        self.assertEqual(sum_lesson_1, sum_)