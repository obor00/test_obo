import unittest
import argparse

# Step 1: Define a test case that accepts parameters
class MyTestCase(unittest.TestCase):
    param = None

    @classmethod
    def setUpClass(cls):
        cls.param = MyTestCase.param

    def test_example(self):
        print(f"Parameter received: {self.param}")
        self.assertIsNotNone(self.param)
        self.assertEqual(self.param, 'expected_value')

# Step 2: Use argparse to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Run unittest with parameters.')
    parser.add_argument('--param', type=str, help='Parameter for the test', required=True)
    return parser.parse_args()

# Step 3: Set up the test runner to initialize the parameters
if __name__ == '__main__':
    args = parse_args()
    MyTestCase.param = args.param

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
