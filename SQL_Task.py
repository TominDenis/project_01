import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_detail(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?"""
    cursor.execute(select_query,(student_id,))
    records = cursor.fetchall()
    print ("Данные по учителям")
    for row in records:
      print ("ID студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[3])
      print ("Название школы: ", row[4])
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

get_student_detail(204)

