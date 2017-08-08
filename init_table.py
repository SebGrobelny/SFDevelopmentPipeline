import psycopg2
import glob
import os
import sys
import csv

def init_tables(database, cursor): 

  delete = """Drop table if exists Location CASCADE"""
  print(delete)
  cursor.execute(delete)
  database.commit()
  
  #QUARYEAR-refers to Quarter Year 
  cursor.execute("CREATE TABLE Location( COORD CHAR(64), QUARYEAR CHAR(64), NAME_ADDR CHAR(64), ZONE_SYM CHAR(64), PRIMARY KEY(COORD,QUARYEAR) );")
  database.commit()