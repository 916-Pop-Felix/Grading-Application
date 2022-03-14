from copy import deepcopy

from Iterable.Iterable import IterableObj


class GradeRepository:
    def __init__(self):
        """List that stores all the grade entries"""
        self.__entities = IterableObj()

    def clear(self):
        """Removes all entries form entities
           Used for tests"""
        self.__entities.clear()

    def add(self, grade):
        """ Adds a new grade to the list, disc being of class Grade type """
        self.__entities.append(grade)

    def get_all(self):
        """Returns all entries from entities in a list format"""
        return self.__entities

    def remove_s(self, stud_id,remainder_list=None):
        new_list = []
        for i in range(0, len(self.__entities)):
            if int(self.__entities[i].s_id) != int(stud_id):
                new_list.append(self.__entities[i])
            else:
                remainder_list.append(self.__entities[i])
        self.__entities.clear()
        self.__entities = deepcopy(new_list)

    def remove_d(self, disc_id,remainder_list=None):
        new_list = []
        for i in range(0, len(self.__entities)):
            if int(self.__entities[i].d_id) != int(disc_id):
                new_list.append(self.__entities[i])
            else:
                remainder_list.append(self.__entities[i])

        self.__entities.clear()
        self.__entities = deepcopy(new_list)

    def remove_last_grade(self):
        self.__entities.pop(len(self.__entities)-1)

    def get_last_added_grade(self):
        return self.__entities[len(self.__entities)-1]

    def __len__(self):
        return len(self.__entities)

class GradeException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg
