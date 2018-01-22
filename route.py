from __future__ import print_function # In python 2.7
import sys
import csv
from database_tools import useDatabase
import preprocess_chemicals_data
import collections
from collections import Counter
from flask import Flask, render_template, json, request,redirect, url_for
import sqlite3
import csv
import logging
from logging.handlers import RotatingFileHandler
import os
import pandas as pd

#To connect with mysql install flask-mysql using pip install flask-mysql


app = Flask(__name__)



@app.route('/')
def main(methods=['POST','GET']):
  return render_template('index1.html')

@app.route('/showSearch')
def showSearch():
  try:
    return render_template('srch.html')
  except Exception as e:
  	return json.dumps({'error':str(e)})


@app.route('/elementSearch',methods=['POST','GET'])
def elementSearch():

  path = os.path.dirname(os.path.realpath('__file__')) +  '/' + 'chem_data.csv'

  if not os.path.isfile(path):
    execfile('preprocess_chemicals_data.py')

  db = useDatabase ()
  table_name = 'Chemicals'
 
  #connects to sql table
  cur, con = db.createTable(table_name)

  #moves data from csv file to sql table
  cur, con = db.transferDataToTable(path,cur,con)

  #structuring a query
  query = "SELECT * from " + table_name + " WHERE "

  #searches using element formula
  if request.form.get('elementFormula'):
    set_element = str(request.form.get('elementFormula'))
    query += "Chemical_formula = '" + set_element + "'"
    print (query)
  
  #searches using properties 
  else:
    color_flag = 0
    if request.form.get('colorchbox'): 
      set_color = str(request.form.get('colordisplayValue'))

      color_flag = 1
      query += "Color = '" + set_color + "'" 

    
    if request.form.get('bandgapchbox'):
      set_bandgap_start = (float)(request.form.get('startrange'))
      set_bandgap_end = (float)(request.form.get('endrange'))

      #if color is also selected
      if color_flag:
        query += ' and '

      query += 'Band_gap BETWEEN %f AND %f' % (set_bandgap_start, set_bandgap_end)

    #logging query
    print (query)
    
  
  #gets result from query  
  data = db.executeQuery (cur, con, query)

  if data:
    names = []
    for item in data:
      f = [str(it) for it in item]
      names.append(f)


    return render_template('view.html',r1 = names)
  else:
    return render_template('retry.html')
    

if __name__ == "__main__":
	app.run(port=5002, debug = True)