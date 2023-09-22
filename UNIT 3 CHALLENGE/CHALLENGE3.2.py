class Student:

  def __init__(self, name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, 
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students

students = [
  Student("TAMILAN", "A12", 7.8),
  Student("ARUMUGAM", "A13", 8.9),
  Student("HARI", "A14", 9.1),
  Student("ANANTH", "A15", 9.9),
  ]
sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
       student.roll_number,
       student.cgpa))
