import unittest
from compress import Compress
import os


class TestCompress(unittest.TestCase):
    
    def setUp(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        files = ['ci.txt', 'cv.txt', 'ct.txt', 'oop.txt', 'tdd.txt']
        
        for i, file in enumerate(files, start=1):
            file_path = os.path.join(current_directory, file)
            text = self.read_file(file_path)
            setattr(self, f'text_{i}', text)
            compress = Compress()
            compressed, values = compress.compress(text)
            setattr(self, f'compressed_{i}', compressed)
            setattr(self, f'values_{i}', values)
            
    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def test_compress_1(self):
        compress = Compress()
        compressed, values = compress.compress(self.text_1)
        self.assertDictEqual(values, self.values_1)
        self.assertListEqual(compressed, self.compressed_1)

    def test_uncompress_1(self):
        compress = Compress()
        self.assertEqual(compress.uncompress(
            self.compressed_1, self.values_1), self.text_1)

    def test_compress_2(self):
        compress = Compress()
        compressed, values = compress.compress(self.text_2)
        self.assertDictEqual(values, self.values_2)
        self.assertListEqual(compressed, self.compressed_2)

    def test_uncompress_2(self):
        compress = Compress()
        self.assertEqual(compress.uncompress(
            self.compressed_2, self.values_2), self.text_2)

    def test_compress_3(self):
        compress = Compress()
        compressed, values = compress.compress(self.text_3)
        self.assertDictEqual(values, self.values_3)
        self.assertListEqual(compressed, self.compressed_3)

    def test_uncompress_3(self):
        compress = Compress()
        self.assertEqual(compress.uncompress(
            self.compressed_3, self.values_3), self.text_3)

    def test_compress_4(self):
        compress = Compress()
        compressed, values = compress.compress(self.text_4)
        self.assertDictEqual(values, self.values_4)
        self.assertListEqual(compressed, self.compressed_4)

    def test_uncompress_4(self):
        compress = Compress()
        self.assertEqual(compress.uncompress(
            self.compressed_4, self.values_4), self.text_4)

    def test_compress_5(self):
        compress = Compress()
        compressed, values = compress.compress(self.text_5)
        self.assertDictEqual(values, self.values_5)
        self.assertListEqual(compressed, self.compressed_5)

    def test_uncompress_5(self):
        compress = Compress()
        self.assertEqual(compress.uncompress(
            self.compressed_5, self.values_5), self.text_5)


if __name__ == '__main__':
    unittest.main()
