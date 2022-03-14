from Domain.Student import Student
from copy import deepcopy
from Iterable.Iterable import IterableObj,filter,sort

class StudentRepository:
    def __init__(self):
        """List that stores all the student entries"""
        self.__entities = IterableObj()

    @staticmethod
    def check_is_int(s_id):
        """ Function also used as an ID validator for remove and update
            Returns none if no error is raised"""
        if not s_id.isnumeric():
            raise StudentException("ID must be a number!")
        elif int(s_id) < 0:
            raise StudentException("ID must be a positive number")

    def find_by_id(self, entity_id):
        """ Function that finds the given ID, also used as an ID validator for remove and update
            Returns none if id was not found"""
        for i in range(0, len(self.__entities)):
            if int(self.__entities[i].id) == int(entity_id):
                return self.__entities[i]
        return None

    def get_name(self, entity_id):
        for i in range(0, len(self.__entities)):
            if int(self.__entities[i].id) == int(entity_id):
                return self.__entities[i].name
        return None

    def clear(self):
        self.__entities.clear()

    def add(self, s_id, name):
        """ Adds a new student to the list, stud being of class Student type """
        if StudentRepository.find_by_id(self, s_id) is None:
            self.__entities.append(Student(s_id, name))
        else:
            raise StudentException("ID already used")

    def remove(self, s_id):
        if StudentRepository.check_is_int(str(s_id)) is None:
            if StudentRepository.find_by_id(self, int(s_id)) is not None:
                for i in range(0, len(self.__entities)):
                    if int(self.__entities[i].id) == int(s_id):
                        self.__entities.pop(i)
                        break
            else:
                raise StudentException("Invalid ID")

    def update(self, s_id, new_name):
        if StudentRepository.check_is_int(str(s_id)) is None:
            if StudentRepository.find_by_id(self, int(s_id)) is not None:
                for i in range(0, len(self.__entities)):
                    if int(self.__entities[i].id) == int(s_id):
                        self.__entities[i].name = new_name
                        break
            else:
                raise StudentException("Invalid ID")

    def find_by_name(self, name):
        """ Filters the original list and puts the list of required names in a new one"""
        new_list = list(filter(lambda x: x.name.lower().find(name.lower()) != -1, self.__entities))
        if not new_list:
            raise StudentException(f"No entry found for {name}")
        return new_list

    def get_all(self):
        return self.__entities

    def sort_by_id(self):
        self.__entities=sort(self.__entities,lambda x:int(x.id),reverse=False)



    def __len__(self):
        """Modified the len structure in order to fit the entities list"""
        return len(self.__entities)


class StudentException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg
