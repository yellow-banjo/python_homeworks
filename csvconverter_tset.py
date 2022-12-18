import unittest
import CsvConverter


class CsvConverterTest(unittest.TestCase):
    def test_convert(self):
        feature = ['id', 'name', 'birth', 'salary', 'department']
        data = '1,Ivan,1980,150000,1'
        output = {'id': '1', 'name': 'Ivan', 'birth': '1980', 'salary': '150000', 'department': '1'}
        self.assertEqual(CsvConverter.convert(feature, data), output)


if __name__ == '__main__':
    unittest.main()
