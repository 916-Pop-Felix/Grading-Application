from Domain.Grade import Grade
from random import *
from Repository.GradeRepository import GradeException


class Service:
    def __init__(self, student_repo, discipline_repo, grade_repo):
        """ All three repos are present as service attributes """
        self.__students = student_repo
        self.__disciplines = discipline_repo
        self.__grades = grade_repo
        # self.__undo_service = undo_service

    def add_student(self, s_id, name):
        """ Appends the student's name and its implicit id to the list """
        self.__students.add(s_id, name)

    def add_discipline(self, d_id, name):
        """ Appends the discipline's name and its implicit id to the list """
        self.__disciplines.add(d_id, name)

    def get_student_name(self, s_id):
        return self.__students.get_name(int(s_id))

    def get_discipline_name(self, d_id):
        return self.__disciplines.get_name(int(d_id))

    def list_student(self):
        return self.__students.get_all()

    def list_discipline(self):
        return self.__disciplines.get_all()

    def update_student(self, s_id, name):
        self.__students.update(int(s_id), name)

    def update_discipline(self, d_id, name):
        self.__disciplines.update(int(d_id), name)

    def remove_student(self, s_id, remainder_list=None):
        self.__students.remove(int(s_id))
        self.__grades.remove_s(int(s_id), remainder_list)

    def remove_discipline(self, d_id, remainder_list):
        self.__disciplines.remove(int(d_id))
        self.__grades.remove_d(int(d_id), remainder_list)

    def sort_student_by_id(self):
        self.__students.sort_by_id()

    def sort_discipline_by_id(self):
        self.__disciplines.sort_by_id()

    def add_grade(self, s_id, d_id, value):
        """
        Checks if the entered values are valid and appends them afterwards to the existing list, otherwise
        it will print a custom error
        :param s_id: id of the student
        :param d_id: id of the discipline
        :param value: grade
        :return: appends the list of attributes to the existing repository
        """
        if 0 <= float(value) <= 10:
            if self.__students.find_by_id(int(s_id)) is not None and self.__disciplines.find_by_id(
                    int(d_id)) is not None:
                self.__grades.add(Grade(s_id, d_id, value))
            else:
                raise GradeException("Invalid student or discipline ID!")
        else:
            raise GradeException("Grade must be between 0 and 10!")

    def add_remainder_grades(self, remainder_list):
        """Method used for undo, in order to add back the deleted grades from a deleted student or discipline"""
        if remainder_list:
            for i in range(len(remainder_list)):
                self.__grades.add(Grade(remainder_list[i].s_id, remainder_list[i].d_id, remainder_list[i].grades))

    def remove_grade(self):
        self.__grades.remove_last_grade()

    def list_grade(self):
        return self.__grades.get_all()

    def get_last_added(self):
        return self.__grades.get_last_added_grade()

    def find_s_id(self, s_id):
        return self.__students.find_by_id(int(s_id))

    def find_d_id(self, d_id):
        return self.__disciplines.find_by_id(int(d_id))

    def find_s_name(self, name):
        return self.__students.find_by_name(name)

    def find_d_name(self, name):
        return self.__disciplines.find_by_name(name)

    def get_student_avg_grade_at_discipline(self, s_id, d_id):
        """
        Calculates the average grade of a given student at a given discipline
        :param s_id: student id
        :param d_id: discipline id
        :return: returns a float type result consisting of the sum of grades divided by the counter
        """
        avg = 0
        avg = float(avg)
        counter = 0
        grade_repo = self.__grades.get_all()
        for i in range(0, len(grade_repo)):
            if int(grade_repo[i].s_id) == int(s_id) and int(grade_repo[i].d_id) == int(d_id):
                avg += float(grade_repo[i].grades)
                counter += 1
        if counter:
            return float(avg / counter)

    def get_discipline_avg_grade(self, d_id):
        """
        Calculates all the averages of students who have a grade at a given discipline
        :param d_id: discipline id
        :return: returns two lists: avg_grade -> containing average values for students
                                    student_list -> containing student ids
        """
        avg_grade = []
        student_list = []
        grade_repo = self.__grades.get_all()
        for i in range(0, len(grade_repo)):
            if int(grade_repo[i].d_id) == int(d_id):
                if int(grade_repo[i].s_id) not in student_list:
                    avg_grade.append(Service.get_student_avg_grade_at_discipline(self, grade_repo[i].s_id,
                                                                                 grade_repo[i].d_id))
                    student_list.append(grade_repo[i].s_id)
        if len(avg_grade):
            return avg_grade, student_list

    def get_failing_students(self):
        """
        Function that provides all the failing students
        :return: a list containing the ids of the failing students
        """
        failing_students = []
        passing_grade = 5
        grade_list = self.__grades.get_all()
        for i in range(0, len(self.__grades)):
            avg_grade_list, check_list = Service.get_discipline_avg_grade(self, grade_list[i].d_id)
            for j in range(0, len(avg_grade_list)):
                if avg_grade_list[j] < passing_grade:
                    if check_list[j] not in failing_students:
                        failing_students.append(check_list[j])
        if failing_students:
            return failing_students
        raise GradeException("Hooray! All the students are passing!")

    def get_student_avg_at_all_disciplines(self, s_id):
        """
        Function that calculates all the discipline averages a student has
        :param s_id: student id
        :return: returns a float type result consisting of the sum of averages divided by the counter
        """
        final_avg = 0
        final_avg = float(final_avg)
        final_counter = 0
        disc_list = []
        grade_list = self.__grades.get_all()
        for i in range(0, len(grade_list)):
            if int(grade_list[i].s_id) == int(s_id):
                if int(grade_list[i].d_id) not in disc_list:
                    final_avg += Service.get_student_avg_grade_at_discipline(self, grade_list[i].s_id,
                                                                             grade_list[i].d_id)
                    final_counter += 1
                    disc_list.append(grade_list[i].d_id)
        if final_avg:
            return float(final_avg / final_counter)
        raise GradeException("Student has no grades")

    @staticmethod
    def sort_two_lists(list1, list2):
        """
        Modified quick-sort function that allows us to also swap elements from the id list while sorting the average
         list
        :param list1: average_list, which will be sorted in descending order
        :param list2: id_list, containing the corresponding ids for the averages
        :return: modifies the introduced params
        """
        for i in range(0, len(list1) - 1):
            for j in range(i + 1, len(list1)):
                if list1[i] < list1[j]:
                    list1[i], list1[j] = list1[j], list1[i]
                    list2[i], list2[j] = list2[j], list2[i]

    @staticmethod
    def convert_list_to_avg(list1):
        """
        Since we already have a function that returns all the student averages in the form of list of grades this
        list only converts all the elements of said list into a final average
        :param list1: the average disciplines list
        :return: final discipline average
        """
        return float(sum(list1) / len(list1))

    def get_all_student_avg(self):
        """
        Gets the average discipline grade for each student and sorts the final list using the method above
        :return: This function returns two lists:
                    avg_list -> the list of all the general averages of students
                    student_list -> list containing students ids which also acts as a validator so that we won't enter
                    the same student two times

        """
        avg_list = []
        student_list = []
        grade_list = self.__grades.get_all()
        for i in range(0, len(grade_list)):
            if int(grade_list[i].s_id) not in student_list:
                student_list.append(grade_list[i].s_id)
                avg_list.append(Service.get_student_avg_at_all_disciplines(self, grade_list[i].s_id))
        Service.sort_two_lists(avg_list, student_list)
        if len(student_list):
            return avg_list, student_list
        raise GradeException("No grades available!")

    def get_all_discipline_avg(self):
        """
        Gets the average student grade for each discipline and sorts the final list using the method above
        We are also using the convert list_to_avg method from above to get the final discipline average grade
        :return: This function returns two lists:
                avg_list -> the list of all the general averages of disciplines
                student_list -> list containing discipline ids which also acts as a validator so that we won't enter
                the same discipline two times

                """
        avg_list = []
        discipline_list = []
        grade_list = self.__grades.get_all()
        for i in range(0, len(grade_list)):
            if int(grade_list[i].d_id) not in discipline_list:
                discipline_list.append(grade_list[i].d_id)
                disc_avg, s = Service.get_discipline_avg_grade(self, grade_list[i].d_id)
                avg_list.append(Service.convert_list_to_avg(disc_avg))
        Service.sort_two_lists(avg_list, discipline_list)
        if len(discipline_list):
            return avg_list, discipline_list
        raise GradeException("No grades available!")

    def print_failing_students(self):
        id_list = Service.get_failing_students(self)
        student_list = []
        for i in range(0, len(id_list)):
            student_list.append(self.__students.find_by_id(id_list[i]))
        return student_list

    def print_best_students(self):
        avg_grades, id_list = Service.get_all_student_avg(self)
        student_list = []
        for i in range(0, len(id_list)):
            student_list.append(self.__students.find_by_id(id_list[i]))
        return student_list, avg_grades

    def print_best_disciplines(self):
        avg_grades, id_list = Service.get_all_discipline_avg(self)
        discipline_list = []
        for i in range(0, len(id_list)):
            discipline_list.append(self.__disciplines.find_by_id(id_list[i]))
        return discipline_list, avg_grades

    def test_all(self):
        names = ["Ionel", "Marcel", "Dorel", "Sorin", "Lorin", "Florin", "Marin", "Daniel", "Daniela", "Marcela"]
        for i in range(len(names)):
            self.__students.add(i + 1, names[i])

        disciplines = ["Statistics", "Business", "Trade", "Deals", "Math", "PE", "Psychology", "English", "Physics",
                       "Logic"]
        for i in range(len(disciplines)):
            self.__disciplines.add(i + 1, disciplines[i])

        for i in range(0, 10):
            self.__grades.add(Grade(randint(1, 10), randint(1, 10), randint(1, 10)))
