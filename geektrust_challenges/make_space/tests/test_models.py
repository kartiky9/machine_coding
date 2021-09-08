import unittest

from models import Time, TimeInterval
from utils.exceptions import IncorrectInputError
from utils.constants import MINUTE_INTERVALS


class TestTimeModel(unittest.TestCase):

    def test_raise_error_for_invalid_time_string(self):
        alphabet_string = "aa:bb"
        alphanumeric_string = "o3:4s"
        out_of_bound_string = "100:52"

        with self.assertRaises(IncorrectInputError):
            Time(alphabet_string)

        with self.assertRaises(IncorrectInputError):
            Time(alphanumeric_string)

        with self.assertRaises(IncorrectInputError):
            Time(out_of_bound_string)

    def test_valid_time(self):
        time_string = "23:45"

        time = Time(time_string)

        self.assertEqual(time.hours, 23)
        self.assertEqual(time.minutes, 45)
        self.assertEqual(time.minutes % MINUTE_INTERVALS, 0)

    def test_raise_error_on_invalid_hours(self):
        invalid_hours_string = "32:00"

        with self.assertRaises(IncorrectInputError):
            Time(invalid_hours_string)

    def test_raise_error_on_invalid_minutes(self):
        invalid_minutes_string = "13:66"

        with self.assertRaises(IncorrectInputError):
            Time(invalid_minutes_string)

    def test_equate_times(self):
        time_one_string = '01:00'
        time_one = Time(time_one_string)
        time_two = Time('02:00')
        same_time_two = Time('02:00')

        self.assertGreater(time_two, time_one)
        self.assertLess(time_one, time_two)
        self.assertGreaterEqual(time_one, time_one)
        self.assertEqual(time_two, same_time_two)
        self.assertNotEqual(time_one, time_two)
        self.assertEqual(str(time_one), time_one_string)
        self.assertLessEqual(time_one, time_two)
