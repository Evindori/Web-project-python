# -*- coding: utf-8 -*-

from flask import render_template
from app import app
import codecs
import requests
import os
import sys

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
def create_file():
  response = requests.get('http://coronavirus-monitor.ru/coronavirus-v-moskve/')
  with open('test.html', 'wb') as output_file:
    output_file.write(response.content)

def getnmbr(string):
    ans = 0
    for i in string:
        if i.isdigit():
            ans = ans*10 + int(i)
    return ans

def getdata():
    create_file()

    with open('test.html', 'r', encoding='utf-8') as input_file:
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
    return {'data_disease': str(data_disease), 'data_healed': str(data_healed), 'data_deathes': str(data_deathes)}

@app.route('/')
def main():
    return '''
    <html>
           <head>
              <meta charset="utf-8" />
              <title>Статистика по короновирусу в Москве</title>
               <style>
                   .btn {
                       display: inline-block;
                       background: #333300;
                       color: #fff; 
                       padding: 1rem 1.5rem; 
                       text-decoration: none; 
                       border-radius: 5px;
                       font-size: 20px
               }
              </style>
           </head>
           <body text="#333300"; 
                 link="#333300"; 
                 alink="#9900CC"; 
                 vlink="#DEDE00"; 
                 style = "background-color:#FFFF99">
                 <p style = "font-size:30px" 
                     align="center">
                     Что бы вы хотели узнать?
                 </p>
                <p align="center">
                      <a href= '/today' class = "btn"> Графики</a>
                </p>
                <p align="center">
                      <a href="/today" class = "btn">Изменения за день</a>
                </p>
                <p> 
                      Источники: <a href="https://coronavirus-control.ru/coronavirus-moscow/">Коронавирус в Москве</a>
                </p>
        </body>
    </html>
    '''

@app.route('/today')
def now():
    data = getdata()
    return render_template('today.html', data = data)
