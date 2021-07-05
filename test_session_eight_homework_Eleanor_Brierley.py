#QUESTION 1
#HOMEWORK_HWK9_ELEANOR_BRIERLEY

import unittest
from unittest import TestCase,  main
from session_eight_homework_Eleanor_Brierley import log_in, run_atm, verify_pin

class TestPinCodeFunction(unittest.TestCase):
    def test_pin_code_correct(self):
        expected = True
        result = log_in(1234)
        self.assertEqual(expected, result)
    def test_pin_code_incorrect(self):
        expected = False
        result = log_in!= (1234)
        self.assertNotEqual(expected, result)

class TestLoginFunction(unittest.TestCase):
    def test_less_than_four(self):
        expected = True
        result = 3
        self.assertLessEqual(expected, result)
    def test_more_or_four(self):
        expected = 4
        result = 4
        self.assertLessEqual(expected, result)

class TestRunAtmFunction(unittest.TestCase):
    def test_withdrawal_amount_less_than_balance(self):
        expected = run_atm(100)
        result = 100
        self.assertLessEqual(expected, result)
    def test_withdrawal_more_than_balance(self):
        expected = 150
        result = 101
        self.assertGreaterEqual(expected, result)

if __name__ == '__main__':
    main()