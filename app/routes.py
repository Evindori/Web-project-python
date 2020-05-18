# -*- coding: utf-8 -*-

from flask import render_template
from collections import namedtuple
from app import app
import codecs
import requests
import os
import sys


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def reveresed(dict):
    ans = {}
    for i in range(10):
        rev = 10 - i
        ans.update({i: dict.get(i)})
    return ans


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


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/today')
def now():
    tdata = getdata('test.html')
    return render_template('today.html', data=tdata)


@app.route('/statis')
def rnow():
    tdata = getstat('test.html')
    return render_template('graph.html', data=tdata)
