import unittest

from Repository.DisciplineRepository import DisciplineRepository
from Repository.GradeRepository import GradeRepository, GradeException
from Repository.StudentRepository import StudentRepository
from Services.Handlers import UndoHandler
from Services.Service import Service
from Services.UndoService import UndoManager


class TestServiceMethods(unittest.TestCase):
    def setUp(self):
        self.__student_repo = StudentRepository()
        self.__discipline_repo = DisciplineRepository()
        self.__grade_repo = GradeRepository()
        self.__service = Service(self.__student_repo, self.__discipline_repo, self.__grade_repo)
        print("SetUp")

    def tearDown(self):
        print("tearDown")

    def testStudentService(self):
        # add method
        self.assertEqual(len(self.__student_repo), 0)
        self.__service.add_student(1, "Nea Marin")
        self.assertEqual(len(self.__student_repo), 1)
        repo = self.__student_repo.get_all()
        self.assertEqual(repo[0].id, 1)
        self.assertEqual(repo[0].name, "Nea Marin")

        # list method
        repo = self.__service.list_student()
        self.assertEqual(len(repo), 1)

        # remove method
        self.__service.add_student(2, "Cabral")
        self.__service.remove_student(1)
        self.assertEqual(len(self.__student_repo), 1)
        repo = self.__student_repo.get_all()
        self.assertEqual(repo[0].name, "Cabral")

        # update method
        self.__service.update_student(2, "Puya")
        repo = self.__student_repo.get_all()
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].name, "Puya")

        # find by id method
        repo = self.__service.find_s_id(3)
        self.assertEqual(repo, None)
        repo = self.__service.find_s_id(2)
        self.assertEqual(repo.name, "Puya")
        self.assertEqual(repo.id, 2)

        # find by name method
        repo = self.__service.find_s_name("Puya")
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].name, "Puya")
        self.assertEqual(repo[0].id, 2)
        repo = self.__service.find_s_name("puya")
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].name, "Puya")
        self.assertEqual(repo[0].id, 2)
        repo = self.__service.find_s_name("Pu")
        self.assertEqual(len(repo), 1)

        self.__student_repo.clear()
        self.__service.test_all()
        self.assertEqual(len(self.__student_repo), 10)
        self.assertEqual(len(self.__discipline_repo), 10)

        # remove method
        self.__service.add_student(44, "Cabral")
        self.assertEqual(len(self.__student_repo), 11)
        self.__service.remove_student(44)
        self.assertEqual(len(self.__student_repo), 10)

    def testDisciplineService(self):
        # add method
        self.assertEqual(len(self.__discipline_repo), 0)
        self.__service.add_discipline(1, "Cox")
        self.assertEqual(len(self.__discipline_repo), 1)

        # list method
        repo = self.__service.list_discipline()
        self.assertEqual(len(repo), 1)

        # remove method
        self.__service.add_discipline(2, "Gatit")
        remainder_list = []
        self.__service.remove_discipline(1, remainder_list)
        self.assertEqual(len(self.__discipline_repo), 1)
        repo = self.__discipline_repo.get_all()
        self.assertEqual(repo[0].name, "Gatit")

        # update method
        self.__service.update_discipline(2, "Gatit")
        repo = self.__discipline_repo.get_all()
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].name, "Gatit")

        # find by id method
        repo = self.__service.find_d_id(3)
        self.assertEqual(repo, None)
        repo = self.__service.find_d_id(2)
        self.assertEqual(repo.name, "Gatit")
        self.assertEqual(repo.id, 2)

        # find by name method
        repo = self.__service.find_d_name("Gatit")
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].name, "Gatit")
        self.assertEqual(repo[0].id, 2)
        repo = self.__service.find_d_name("gatit")
        self.assertEqual(len(repo), 1)
        self.assertEqual(repo[0].name, "Gatit")
        self.assertEqual(repo[0].id, 2)
        repo = self.__service.find_d_name("Gat")
        self.assertEqual(len(repo), 1)


class TestGradeMethods(unittest.TestCase):
    def setUp(self):
        self.__student_repo = StudentRepository()
        self.__discipline_repo = DisciplineRepository()
        self.__grade_repo = GradeRepository()
        self.__service = Service(self.__student_repo, self.__discipline_repo, self.__grade_repo)

        print("SetUp")

    def tearDown(self):
        print("tearDown")

    def testGradeService(self):
        self.__service.add_student(1, "Puya")
        self.__service.add_discipline(1, "Gatit")
        # add grade method
        self.assertEqual(len(self.__grade_repo), 0)
        self.assertEqual(len(self.__student_repo), 1)
        self.assertEqual(len(self.__discipline_repo), 1)
        self.__service.add_grade(1, 1, 6)
        self.assertEqual(len(self.__grade_repo), 1)
        repo = self.__service.list_grade()
        self.assertEqual(len(repo), 1)
        self.assertRaises(GradeException, self.__service.add_grade, 1, 1, 11)
        self.assertRaises(GradeException, self.__service.add_grade, 3, 1, 5)
        self.assertRaises(GradeException, self.__service.add_grade, 1, 3, 5)
        self.assertRaises(GradeException, self.__service.add_grade, 1, 1, "11")

        # remove student id
        self.__service.add_student(2, "Cabral")
        remainder_list = []
        self.__service.remove_student(1, remainder_list)
        self.assertEqual(len(self.__student_repo), 1)
        repo = self.__student_repo.get_all()
        self.assertEqual(repo[0].name, "Cabral")
        self.assertEqual(len(self.__grade_repo), 0)
        self.__service.add_grade(2, 1, 6)
        self.assertEqual(len(self.__grade_repo), 1)

        # remove discipline method
        self.__service.add_discipline(2, "Stuff")
        remainder_list = []
        self.__service.remove_discipline(1, remainder_list)
        self.assertEqual(len(self.__discipline_repo), 1)
        repo = self.__discipline_repo.get_all()
        self.assertEqual(repo[0].name, "Stuff")
        self.assertEqual(len(self.__grade_repo), 0)
        self.__service.add_grade(2, 2, 6)
        self.assertEqual(len(self.__grade_repo), 1)

        # failing students method
        self.__service.add_student(3, "Florin")
        self.assertEqual(len(self.__student_repo), 2)
        repo = self.__student_repo.get_all()
        self.assertEqual(repo[0].id, 2)
        self.assertEqual(repo[1].id, 3)
        self.__service.add_student(4, "Catalin")  # 4
        self.__service.add_student(5, "Catalin")  # 5
        self.__service.add_discipline(3, "Music")
        repo = self.__discipline_repo.get_all()
        self.assertEqual(len(repo), 2)
        self.assertEqual(repo[0].id, 2)
        self.assertEqual(repo[1].id, 3)
        self.__service.add_discipline(4, "Music")  # 4
        self.__service.add_discipline(5, "Music")  # 5

        self.__service.add_grade(2, 3, 2)
        self.__service.add_grade(4, 3, 6)
        self.assertEqual(len(self.__service.print_failing_students()), 1)
        self.__service.add_grade(2, 3, 3)
        self.__service.add_grade(3, 4, 8)
        self.__service.add_grade(4, 5, 7)
        self.__service.add_grade(3, 4, 5)
        self.__service.add_grade(4, 5, 2)
        self.__service.add_grade(4, 3, 2)
        self.__service.add_grade(2, 5, 5)

        repo = self.__service.list_grade()
        self.assertEqual(len(repo), 10)
        self.assertEqual(self.__service.get_student_avg_grade_at_discipline(2, 2), 6.0)  # passing
        self.assertEqual(self.__service.get_student_avg_grade_at_discipline(2, 3), 2.5)  # failing
        self.assertEqual(self.__service.get_student_avg_grade_at_discipline(2, 5), 5.0)  # failing but same student
        self.assertEqual(self.__service.get_student_avg_grade_at_discipline(3, 4), 6.5)
        self.assertEqual(self.__service.get_student_avg_grade_at_discipline(4, 5), 4.5)  # failing
        self.assertEqual(self.__service.get_student_avg_grade_at_discipline(4, 3), 4.0)  # failing but same student

        avg_list, student_list = self.__service.get_discipline_avg_grade(2)
        self.assertEqual(len(avg_list), 1)
        self.assertEqual(len(student_list), 1)
        self.assertEqual(avg_list[0], 6.0)
        self.assertEqual(student_list[0], 2)
        avg_list, student_list = self.__service.get_discipline_avg_grade(5)
        self.assertEqual(len(avg_list), 2)
        self.assertEqual(len(student_list), 2)
        self.assertEqual(avg_list[0], 4.5)
        self.assertEqual(student_list[0], 4)
        self.assertEqual(student_list[1], 2)

        final_repo = self.__service.get_failing_students()
        self.assertEqual(len(final_repo), 2)  # 2 failing students as seen above

        final_repo = self.__service.get_student_avg_at_all_disciplines(4)
        self.assertEqual(final_repo, 4.25)  # (4.0+4.5)/2 see above verification

        avg_list, student_list = self.__service.get_all_student_avg()
        self.assertEqual(len(avg_list), 3)
        self.assertEqual(len(student_list), 3)
        self.assertEqual(student_list[1], 2)
        self.assertEqual(avg_list[0], 6.5)
        self.assertEqual(avg_list[1], 4.5)
        self.assertEqual(avg_list[2], 4.25)

        avg_list, discipline_list = self.__service.get_all_discipline_avg()
        self.assertEqual(len(avg_list), 4)
        self.assertEqual(len(discipline_list), 4)
        self.assertEqual(avg_list[0], 6.5)
        self.assertEqual(avg_list[1], 6.0)
        self.assertEqual(avg_list[2], 4.75)
        self.assertEqual(avg_list[3], 3.25)
        self.assertEqual(discipline_list[3], 3)
        student_list,avg_list=self.__service.print_best_students()
        self.assertEqual(len(student_list),3)
        self.assertEqual(len(avg_list), 3)

        discipline_list, avg_list = self.__service.print_best_disciplines()
        self.assertEqual(len(discipline_list),4)
        self.assertEqual(len(avg_list), 4)



class TestUndoServiceStudent(unittest.TestCase):
    def setUp(self):
        self.__student_repo = StudentRepository()
        self.__discipline_repo = DisciplineRepository()
        self.__grade_repo = GradeRepository()
        self.__undo = UndoManager()
        self.__service = Service(self.__student_repo, self.__discipline_repo, self.__grade_repo)

    def tearDown(self):
        print("teardown")

    def testUndoMethods(self):
        # add undo student

        self.__service.add_student(1, "Rip maradonna")
        self.assertEqual(len(self.__student_repo), 1)
        self.__undo.register_operation(self.__service, UndoHandler.ADD_STUDENT, 1, "Rip maradonna")
        self.assertEqual(self.__undo.undo(), 1)
        self.assertEqual(len(self.__student_repo), 0)
        # self.assertEqual(self.__undo.undo(), -1)
        self.assertEqual(self.__undo.redo(), 1)
        self.assertEqual(len(self.__student_repo), 1)
        self.assertEqual(self.__undo.redo(), -1)

        # remove undo student
        self.__service.add_student(2, "Cipri Kiraly")
        self.__service.add_discipline(1, "da")
        self.__service.add_grade(2, 1, 8)
        self.__service.add_grade(2, 1, 3)
        self.__service.add_grade(2, 1, 4)
        self.assertEqual(len(self.__student_repo), 2)
        self.assertEqual(len(self.__grade_repo), 3)
        remainder_list = []
        self.__service.remove_student(2, remainder_list)
        self.assertEqual(len(self.__student_repo), 1)
        self.__undo.register_operation(self.__service, UndoHandler.DELETE_STUDENT, 2, "Cipri Kiraly", remainder_list)
        self.assertEqual(len(self.__grade_repo), 0)
        self.assertEqual(len(remainder_list), 3)
        self.__undo.undo()
        self.assertEqual(len(self.__student_repo), 2)
        self.assertEqual(len(self.__grade_repo), 3)  # student grades are added back in the grade repo
        self.assertEqual(self.__undo.redo(), 1)
        # self.assertEqual(len(self.__student_repo), 1)
        # self.assertEqual(len(self.__grade_repo), 0)

        # update undo student
        old_name = self.__service.get_student_name(1)
        self.__service.update_student(1, "Cipri Sonea")
        self.__undo.register_operation(self.__service, UndoHandler.UPDATE_STUDENT, 1, old_name)
        self.assertEqual(self.__service.get_student_name(1), "Cipri Sonea")
        self.__undo.undo()
        self.assertEqual(self.__service.get_student_name(1), "Rip maradonna")
        self.__undo.redo()
        self.assertEqual(self.__service.get_student_name(1), "Cipri Sonea")

        # add undo discipline
        self.__service.add_discipline(2, "Rip maradonna")
        self.assertEqual(len(self.__discipline_repo), 2)
        self.__undo.register_operation(self.__service, UndoHandler.ADD_DISCIPLINE, 2, "Rip maradonna")
        self.assertEqual(self.__undo.undo(), 1)
        self.assertEqual(len(self.__discipline_repo), 1)
        self.assertEqual(self.__undo.redo(), 1)
        self.assertEqual(len(self.__discipline_repo), 2)

        # remove undo
        self.__service.add_discipline(3, "Cipri Kiraly")
        self.__service.add_student(3,"da")
        self.__service.add_grade(3, 3, 8)
        self.__service.add_grade(3, 3, 3)
        self.__service.add_grade(3, 3, 4)
        self.assertEqual(len(self.__student_repo), 2)
        self.assertEqual(len(self.__grade_repo), 3)
        remainder_list = []
        self.__service.remove_discipline(3, remainder_list)
        self.assertEqual(len(self.__discipline_repo), 2)
        self.__undo.register_operation(self.__service, UndoHandler.DELETE_DISCIPLINE, 3, "Cipri Kiraly", remainder_list)
        self.assertEqual(len(self.__grade_repo), 0)
        self.assertEqual(len(remainder_list), 3)
        self.__undo.undo()
        self.assertEqual(len(self.__discipline_repo), 3)
        self.assertEqual(len(self.__grade_repo), 3)  # discipline grades are added back in the grade repo
        self.assertEqual(self.__undo.redo(), 1)
        self.assertEqual(len(self.__discipline_repo), 2)
        self.assertEqual(len(self.__grade_repo), 0)

        # update undo
        old_name = self.__service.get_discipline_name(1)
        self.assertEqual(old_name,"da")
        self.__service.update_student(1, "Cipri Kiraly")
        self.__undo.register_operation(self.__service, UndoHandler.UPDATE_DISCIPLINE, 1, old_name)
        self.assertEqual(self.__service.get_student_name(1), "Cipri Kiraly")
        self.__undo.undo()
        self.__undo.redo()


class TestUndoGradeStudent(unittest.TestCase):
    def setUp(self):
        self.__student_repo = StudentRepository()
        self.__discipline_repo = DisciplineRepository()
        self.__grade_repo = GradeRepository()
        self.__undo = UndoManager()
        self.__service = Service(self.__student_repo, self.__discipline_repo, self.__grade_repo)
        self.assertEqual(self.__undo.undo(), -1)

    def tearDown(self):
        print("Teardown")

    def testUndoGrade(self):
        self.assertEqual(len(self.__grade_repo),0)
        self.__service.add_student(1,"da")
        self.__service.add_discipline(1,"da")
        self.__service.add_grade(1,1,5)
        self.assertEqual(len(self.__grade_repo), 1)
        self.__undo.register_operation(self.__service, UndoHandler.ADD_GRADE)
        self.__undo.undo()
        self.assertEqual(len(self.__grade_repo), 0)
        # self.__undo.redo()
        # self.assertEqual(len(self.__grade_repo), 1)