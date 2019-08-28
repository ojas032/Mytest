#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/')
def start():
	return render_template('index.html')

@app.route('/success/<name>/<word>')
def success(name,word):
   return 'welcome %s %s'%(name,word)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      password=request.form['pass']
      return redirect(url_for('success',name = user,word=password))

   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)