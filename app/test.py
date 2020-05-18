# -*- coding: utf-8 -*-
import unittest
import requests
from flask import render_template
from collections import namedtuple
import codecs
import sys
import os

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
def create_file(web, address):
  response = requests.get(web)
  with open(address, 'wb') as output_file:
    output_file.write(response.content)


def getnmbr(string):
    ans = 0
    for i in string:
        if i.isdigit():
            ans = ans*10 + int(i)
    return ans


def getdata(address, web='http://coronavirus-monitor.ru/coronavirus-v-moskve/'):
    create_file(web, address)

    with open(address, 'r', encoding='utf-8') as input_file:
        data_disease = 0
        data_healed = 0
        data_deathes = 0
        fincome = 1
        for line in input_file:
            if line.find("Заражений") != -1 and fincome:
                data_disease = getnmbr(line)
            if line.find("Выздоровлений") != -1 and fincome:
                data_healed = getnmbr(line)
            if line.find("Смертей") != -1 and fincome:
                data_deathes = getnmbr(line)
                fincome = 0
    return {'data_disease': str(data_disease),
            'data_healed': str(data_healed),
            'data_deathes': str(data_deathes)}


def getstat(address, web='https://coronavirusstat.ru/country/moskva/263672/'):
    create_file(web, address)
    data = {}
    with open(address, 'r', encoding='utf-8') as input_file:
            line = input_file.readline()
            while line != '</html>':
                line = input_file.readline()
                if line.find("Случаев</th>") != -1:
                    n = 9
                    while line.find('</tbody>') == -1:
                        while line.find("<th>") == -1:
                            line = input_file.readline()
                        date = line.strip()
                        clis = []
                        clis.append(str(date[4:-7]))
                        while line.find('</tr>') == -1:
                            line = input_file.readline()
                            if line.find('<td>') != -1:
                                line = input_file.readline()
                                clis.append(getnmbr(line))
                        data.update({n : clis})
                        n -= 1
                        line = input_file.readline()
                        line = input_file.readline()
    return reveresed(data)


class MyTestCase(unittest.TestCase):
    def test_create_file(self):
        web = 'file:///' + os.path.join(os.path.dirname(os.path.abspath('test0.html')), 'test0.html')
        create_file(web.replace("\\", "/"), 'anstest0.html')
        with open('test0.html', 'r') as t:
            with open('anstest0.html', 'r') as at:
                self.assertEqual(at.read(), t.read())

    def test_getnmbr(self):
        self.assertEqual(getnmbr('asasdsd sad9111hj kk', '9111'))

    def test_getdata(self):
        web = 'file:///' + os.path.join(os.path.dirname(os.path.abspath('test2.html')), 'test2.html')
        self.assertEqual(getdata('anstest2.html', web.replace("\\", "/")), {'data_disease': '1',
            'data_healed': '2',
            'data_deathes': '3'})

    def test_getstat(self):
        web = 'file:///' + os.path.join(os.path.dirname(os.path.abspath('test3.html')), 'test3.html')
        self.assertEqual(getstat('anstest3.html', web.replace("\\", "/")), {0: ['09.05.20', 90400, 12779, 1010],
         1: ['10.05.20', 1, 1, 1],
         2: ['11.05.20', 2, 2, 2],
         3: ['12.05.20', 3, 3, 3],
         4: ['13.05.20', 103266, 21506, 1232],
         5: ['14.05.20', 106099, 23327, 1290],
         6: ['15.05.20', 109544, 24562, 1358],
         7: ['16.05.20', 111505, 26032, 1432],
         8: ['17.05.20', 113831, 27490, 1503],
         9: ['18.05.20', 113831, 27490, 1503]})


if __name__ == '__main__':
    unittest.main()
