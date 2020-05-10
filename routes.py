# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from otpt import getdata

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
    <form action = "otpt.py" method = 'post'>
          <button type='submit' color: #fff>Графики</button>
    </form>
    </p>
    <p align="center">
          <a href="info.html" class = "btn">Изменения за день</a>
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
