from datetime import date, datetime, timedelta
from university import Course, Mentor, Teacher, Student, University

python_course = Course("Python", datetime.now()-timedelta(days=2), datetime.now() + timedelta(days= 0)) #30))
js_course = Course("JavaScript", datetime.now(), datetime.now() + timedelta(days=60))

alex_student = Student("Alex", "Stp", date(1995, 7, 8))
nik_student = Student("Nik", "Fial", date(1998, 10, 22))

bred_teacher = Teacher("Bred", "Cmp", date(1974, 6, 25), 2000, python_course)

koli_mentor = Mentor("Koli", "Key", date(1987, 3, 13), 1200, [python_course, js_course])

harvard_university = University(
    "Harvard",
    [python_course, js_course],
    [bred_teacher, koli_mentor],
    [alex_student, nik_student],
)

#print (f"Course.is_active(): {python_course.is_active()}")
#
#print (f"Teacher.get_yearly_salary(): {bred_teacher.get_yearly_salary()}")
#print (f"Teacher.answer_question(): {bred_teacher.answer_question(python_course,'WTF?')}")
#print (f"Teacher.answer_question(): {bred_teacher.answer_question(js_course,'WTF?')}")
#print (f"Teacher.change_course(): {bred_teacher.change_course(js_course)}")
#print (f"Teacher.change_course(): {bred_teacher.change_course(python_course)}")
#
#print (f"Mentor.get_yearly_salary(): {koli_mentor.get_yearly_salary()}")
#
#print(len(koli_mentor.courses)) # -> 2 # менторить на 2ух курсах
#print(koli_mentor.answer_question(js_course, 'Яка домашка?')) # -> True # на перше питання відповіли
#print(koli_mentor.answer_question(js_course, 'Чи можу я здати пізніше?')) # -> False # на друге питання НЕ відповіли
#print(koli_mentor.answer_question(js_course, 'Чи можу я здати пізніше?')) #-> True # теж саме питання, але вже знайшли час відповісти
#print(koli_mentor.answer_question(js_course, 'Яка оцінка?')) #-> False # не вистачило часу відповісти на це питання
#
#print(koli_mentor.answer_question(python_course, 'Чи можу я здати пізніше?')) # -> False
#        # питання на яке відповідали, і є час відповісти, але питання стосується курсу який вже закінчився
#
#print(koli_mentor.answer_question(js_course, 'Що було на уроці?')) #-> True
#        # так як на минуле питання ми не відповідали, на наступне питання є можливість відповісти
#
#
#print(koli_mentor.answer_question(js_course, 'Що було на уроці?')) #-> True
#        # не дивлячись на те що ми дуже зайняті, але маємо змогу відповісти на питання, на яке вже відповідали.
#
#print(koli_mentor.answer_question(js_course, 'Як мені виконати ДЗ?')) # -> False
#        # знову зайняті, False
#
#print(koli_mentor.answer_question(js_course, 'Як мені виконати ДЗ?')) # -> True
#        # те саме питання по іншому курсу, знайшли час відповісти в цей раз
#
#print(koli_mentor.answer_question(js_course, 'Як мені виконати ДЗ?')) #-> True
#        # те саме питання по першому курсу, можемо відповідати на це питання поза чергою
#
#print(f"Mentor.change_courses(): {koli_mentor.change_courses([js_course, python_course])}")
#
#nik_student.add_mark(0)
#nik_student.add_mark(102)
#nik_student.add_mark(9)
#alex_student.add_mark(10)
#alex_student.add_mark(10)
#print(f"Student.get_all_marks(): {nik_student.get_all_marks()}")
#print(f"Student.get_avarage_mark(): {nik_student.get_avarage_mark()}")
#print(f"Student.get_average_by_last_n_marks(): {nik_student.get_average_by_last_n_marks(2)}")
#print(f"Student.get_average_from_date(): {nik_student.get_average_from_date(from_date=datetime(2022, 8, 5))}")
##nik_student.get_average_from_date(from_date=datetime(2022, 8, 5))
#
#print(harvard_university.get_average_salary())
#print(harvard_university.get_average_mark())
#print(harvard_university.get_active_courses())
#
#print(koli_mentor.__str__())
#print(bred_teacher.__str__())
#print(alex_student.__str__())
#print(harvard_university.__str__())
