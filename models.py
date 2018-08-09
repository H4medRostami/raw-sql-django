from django.db import connection
cursor=connection.cursor()
cursor.execute("""
  SELECT DISTINCT first_name
  FROM people_person
  WHERE last_name=%s""", ['Rostami'])
  row = cursor.fethone()
  
