import unittest
from datetime import datetime, timedelta
import sys

sys.path.append('../src')

from time_processing import parse_time_expression, convert_to_publish_time, relative_to_absolute_time, time_converter

class TestTimeConverter(unittest.TestCase):

    def test_parse_time_expression(self):
        # Test parsing time expression
        example_time = "7 saat önce"
        expected_time = (7, 'saat')
        parsed_time = parse_time_expression(example_time)
        self.assertEqual(parsed_time, expected_time)

    def test_convert_to_publish_time(self):
        # Test converting to publish time
        current_time = datetime.now()
        example_amount = 3
        example_unit = "gün"
        publish_time = convert_to_publish_time(example_amount, example_unit, current_time)
        expected_publish_time = current_time - timedelta(days=3)

        self.assertEqual(publish_time, expected_publish_time, current_time)
    
    def test_absolule_time(self):
        # Test converting relative to absolue time
        current_time = datetime.now()
        example_time = "15 saat önce"
        converted_time = relative_to_absolute_time(example_time, current_time )
        expected_publish_time = current_time - timedelta(hours=15)
        self.assertEqual(converted_time, str(expected_publish_time))

    def test_time_converter(self):
        # Test time converting
        example_time = '15:23'
        converted_time_expression = time_converter(example_time)
        expected_convert_expression = 923
        self.assertEqual(converted_time_expression, expected_convert_expression)

if __name__ == '__main__':
    unittest.main()