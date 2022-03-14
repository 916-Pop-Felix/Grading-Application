from Domain.Student import Student
from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Repository.DisciplineRepository import DisciplineRepository, DisciplineException
from Repository.StudentRepository import StudentRepository, StudentException
from Repository.GradeRepository import GradeRepository
import unittest


class TestStudentRepository(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def testStudentRepository(self):
        repo = StudentRepository()
        examples = ["Skinny Pete", "Jesse Pinkman", "Badger", "Combo"]
        for i in range(0, len(examples)):
            repo.add(i + 1, examples[i])
        repo.add(5, "Gus")
        value = repo.find_by_id(5)
        value1 = repo.find_by_id(100)
        final_repo = repo.get_all()
        self.assertIsNotNone(value)
        self.assertEqual(value1, None)

        # add test
        self.assertEqual(len(final_repo), 5)
        self.assertEqual(final_repo[0].name, "Skinny Pete")
        self.assertEqual(final_repo[1].name, "Jesse Pinkman")

        # remove test
        repo.remove(2)
        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 4)
        self.assertNotEqual(final_repo[1].name, "Jesse Pinkman")
        self.assertEqual(final_repo[1].name, "Badger")
        self.assertEqual(final_repo[0].name, "Skinny Pete")

        # update test
        repo.update(1, "Big Pete")
        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 4)
        self.assertEqual(final_repo[0].name, "Big Pete")
        self.assertEqual(final_repo[1].name, "Badger")

        # find by name test
        final_repo = repo.find_by_name("Combo")  # full correct name search
        self.assertEqual(len(final_repo), 1)
        self.assertEqual(final_repo[0].name, "Combo")
        final_repo = repo.find_by_name("coMbo")  # lower and upper case name search
        self.assertEqual(len(final_repo), 1)
        self.assertEqual(final_repo[0].name, "Combo")
        final_repo = repo.find_by_name("Comb")  # partial string match
        self.assertEqual(len(final_repo), 1)

        # get_name for undo
        name = repo.get_name(4)
        self.assertEqual(name, "Combo")
        name = repo.get_name(10)
        self.assertIsNone(name)
        repo.sort_by_id()
        repo.clear()
        self.assertEqual(len(repo), 0)


class TestDisciplineRepository(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def testDisciplineRepository(self):
        repo = DisciplineRepository()
        examples = ["Math", "Programming",
                    "PE", "Talent"]

        for i in range(0, len(examples)):
            repo.add(i+1,examples[i])
        repo.add(5, "Logic")

        value = repo.find_by_id(5)
        value1 = repo.find_by_id(0)
        final_repo = repo.get_all()
        self.assertNotEqual(value, None)
        self.assertEqual(value1, None)
        self.assertNotEqual(value1, 100)
        self.assertEqual(len(final_repo), 5)
        self.assertEqual(final_repo[0].name, "Math")
        self.assertEqual(final_repo[1].name, "Programming")

        repo.remove(2)
        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 4)
        self.assertNotEqual(final_repo[1].name, "Programming")
        self.assertEqual(final_repo[1].name, "PE")
        self.assertEqual(final_repo[0].name, "Math")

        repo.update(1, "Totally not math")
        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 4)
        self.assertEqual(final_repo[0].name, "Totally not math")
        self.assertEqual(final_repo[1].name, "PE")


        # find by name test
        final_repo = repo.find_by_name("Talent")  # full correct name search
        self.assertEqual(len(final_repo), 1)
        self.assertEqual(final_repo[0].name, "Talent")
        final_repo = repo.find_by_name("tAlENt")  # lower and upper case name search
        self.assertEqual(len(final_repo), 1)
        self.assertEqual(final_repo[0].name, "Talent")
        final_repo = repo.find_by_name("Tale")  # partial string match
        self.assertEqual(len(final_repo), 1)
        self.assertEqual(final_repo[0].name, "Talent")

        #get_name for undo
        name=repo.get_name(4)
        self.assertEqual(name,"Talent")
        name=repo.get_name(10)
        self.assertIsNone(name)
        repo.sort_by_id()
        repo.clear()
        self.assertEqual(len(repo),0)


class TestGradeRepository(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Teardown")

    def testGradeRepository(self):
        repo = GradeRepository()
        examples = [Grade(1, 1, 3), Grade(2, 3, 5),
                    Grade(3, 4, 2), Grade(3, 4, 7)]

        for i in range(0, len(examples)):
            repo.add(examples[i])
        repo.add(Grade(3, 6, 9))
        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 5)
        self.assertEqual(final_repo[4].s_id, 3)
        self.assertEqual(final_repo[4].d_id, 6)
        self.assertEqual(final_repo[4].grades, 9)
        self.assertEqual(final_repo[0].s_id, 1)
        self.assertEqual(final_repo[1].d_id, 3)


        remainder_list=[]
        repo.remove_s(2,remainder_list)

        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 4)
        self.assertNotEqual(final_repo[1].s_id, 2)
        self.assertEqual(final_repo[1].s_id, 3)
        self.assertEqual(final_repo[1].d_id, 4)

        repo.remove_d(4,remainder_list)
        self.assertEqual(len(remainder_list),3)
        final_repo = repo.get_all()
        self.assertEqual(len(final_repo), 2)
        self.assertEqual(final_repo[1].s_id, 3)
        self.assertEqual(final_repo[1].d_id, 6)

        last_grade=repo.get_last_added_grade()
        self.assertEqual(last_grade.s_id, 3)
        self.assertEqual(last_grade.d_id, 6)
        self.assertEqual(last_grade.grades, 9)
        repo.remove_last_grade()
        final_repo=repo.get_all()
        self.assertEqual(len(final_repo),1)

        repo.clear()
        final_repo=repo.get_all()
        self.assertEqual(len(final_repo),0)


class TestStudentException(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.__repo = StudentRepository()
        examples = ["Skinny Pete", "Jesse Pinkman"
            , "Badger", "Combo"]
        for i in range(0, len(examples)):
            self.__repo.add(i+1,examples[i])

    def tearDown(self):
        print("tearDown")

    def testExceptions(self):
        self.assertEqual(len(self.__repo), 4)
        #add exceptions
        self.assertRaises(StudentException,self.__repo.add,1,"yes")

        # remove exceptions
        self.assertRaises(StudentException, self.__repo.remove, 5)
        self.assertRaises(StudentException, self.__repo.remove, -21)
        self.assertRaises(StudentException, self.__repo.remove, "miau")

        # update exceptions
        self.assertRaises(StudentException, self.__repo.update, 5, "yes")
        self.assertRaises(StudentException, self.__repo.update, -21, "yes")
        self.assertRaises(StudentException, self.__repo.update, "miau", "yes")

        # find by ID exceptions
        self.assertEqual(self.__repo.find_by_id(-23), None)
        self.assertRaises(ValueError, self.__repo.find_by_id, "yes")

        # find by name exceptions
        self.assertRaises(StudentException, self.__repo.find_by_name, "Gus")


class TestDisciplineException(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.__repo = DisciplineRepository()
        examples = ["Bani",  "Afaceri",
                     "Scheme",  "Combinatii"]
        for i in range(0, len(examples)):
            self.__repo.add(i+1,examples[i])

    def tearDown(self):
        print("tearDown")

    def testExceptions(self):
        self.assertEqual(len(self.__repo), 4)

        # add exceptions
        self.assertRaises(DisciplineException, self.__repo.add, 1, "yes")
        # remove exceptions
        self.assertRaises(DisciplineException, self.__repo.remove, 5)
        self.assertRaises(DisciplineException, self.__repo.remove, -21)
        self.assertRaises(DisciplineException, self.__repo.remove, "miau")

        # update exceptions
        self.assertRaises(DisciplineException, self.__repo.update, 5, "yes")
        self.assertRaises(DisciplineException, self.__repo.update, -21, "yes")
        self.assertRaises(DisciplineException, self.__repo.update, "miau", "yes")

        # find by ID exceptions
        self.assertEqual(self.__repo.find_by_id(-23), None)
        self.assertRaises(ValueError, self.__repo.find_by_id, "yes")

        # find by name exceptions
        self.assertRaises(DisciplineException, self.__repo.find_by_name, "Bisnita")
