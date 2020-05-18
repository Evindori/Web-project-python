from __init__ import app
from routes import reveresed, create_file, getnmbr, getdata, getstat
import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_create_file(self):
        web = 'file:///' + os.path.join(os.path.dirname(os.path.abspath('test0.html')), 'test0.html')
        create_file(web, 'anstest0.html')
        with open('test0.html', 'r') as t:
            with open('anstest0.html', 'r') as at:
                self.assertEqual(at.read(), t.read())


if __name__ == '__main__':
    unittest.main()
