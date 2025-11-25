from datetime import date
from school.create_tables import init_db
from school.crud import (
    create_student,
    get_students,
    get_one_student,
    search_students_by_first_name,
    search_students_by_name,
)

init_db()


# create_student('ali', 'valiyev3', date(2005, 9, 3))

# students = get_students()
# print(students)


# s = get_one_student(3)
# print(s)


# sts = search_students_by_first_name('ali')
# print(sts)

sts = search_students_by_name('vali')
print(sts)
