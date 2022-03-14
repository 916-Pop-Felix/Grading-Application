class Student:
    def __init__(self,s_id ,name):
        self.__id = s_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self) -> str:
        return "Student: {0}. {1}".format(self.__id, self.__name)
