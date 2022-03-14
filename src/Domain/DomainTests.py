import unittest
from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.Student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStudent(self):
        g1 = Student(1,"Jimmy")
        g2 = Student(2,"Kim")

        # verification for getters
        self.assertEqual(g1.name, "Jimmy")
        self.assertEqual(g1.id, 1)
        self.assertEqual(g2.name, "Kim")
        self.assertEqual(g2.id, 2)

        # verification for setters
        g1.id = 3
        g1.name = "Hector"
        self.assertEqual(g1.id, 3)
        self.assertEqual(g1.name, "Hector")
        print(g1)


class TestDiscipline(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDiscipline(self):
        g1 = Discipline(1,"Math")
        g2 = Discipline(2,"English")

        # verification for getters
        self.assertEqual(g1.name, "Math")
        self.assertEqual(g1.id, 1)
        self.assertEqual(g2.name, "English")
        self.assertEqual(g2.id, 2)

        # verification for setters
        g1.id = 3
        g1.name = "Stuff"
        self.assertEqual(g1.id, 3)
        self.assertEqual(g1.name, "Stuff")
        print(g1)


class TestGrade(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGrade(self):
        g1 = Grade(1, 1, 7.5)
        g2 = Grade(2, 2, 10)

        # verification for getters
        self.assertEqual(g1.grades, 7.5)
        self.assertEqual(g2.grades, 10)
        self.assertEqual(g1.s_id, 1)
        self.assertEqual(g2.d_id, 2)

        # verification for setters
        g1.s_id = 3
        g1.d_id = 2
        g1.grades = 5
        self.assertEqual(g1.s_id, 3)
        self.assertEqual(g1.d_id, 2)
        self.assertEqual(g1.grades, 5)
        print(g1)





