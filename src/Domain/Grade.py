

class Grade:
    def __init__(self, student_id, discipline_id, grade):
        self.__s_id = student_id
        self.__d_id = discipline_id
        self.__grades = grade

    @property
    def s_id(self):
        return self.__s_id

    @s_id.setter
    def s_id(self, value):
        self.__s_id = value

    @property
    def d_id(self):
        return self.__d_id

    @d_id.setter
    def d_id(self, value):
        self.__d_id = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        self.__grades = value

    def __str__(self) -> str:
        return "Student ID: {0}, Discipline ID: {1}, Grade: {2}".format(self.__s_id, self.__d_id, self.__grades)


