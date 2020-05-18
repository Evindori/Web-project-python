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

    def test_getnmbr(self):
        self.assertEqual(getnmbr('asasdsd sad9111hj kk', '9111'))

    def test_getdata(self):
        web = 'file:///' + os.path.join(os.path.dirname(os.path.abspath('test2.html')), 'test2.html')
        self.assertEqual(getdata('anstest2.html', web), {'data_disease': '1',
            'data_healed': '2',
            'data_deathes': '3'})

    def test_getstat(self):
        web = 'file:///' + os.path.join(os.path.dirname(os.path.abspath('test3.html')), 'test3.html')
        self.assertEqual(getstat('anstest3.html', web), {0: ['09.05.20', 90400, 12779, 1010],
         1: ['10.05.20', 94882, 13790, 1068],
         2: ['11.05.20', 96963, 17822, 1124],
         3: ['12.05.20', 100480, 19642, 1179],
         4: ['13.05.20', 103266, 21506, 1232],
         5: ['14.05.20', 106099, 23327, 1290],
         6: ['15.05.20', 109544, 24562, 1358],
         7: ['16.05.20', 111505, 26032, 1432],
         8: ['17.05.20', 113831, 27490, 1503],
         9: ['18.05.20', 113831, 27490, 1503]})


if __name__ == '__main__':
    unittest.main()
