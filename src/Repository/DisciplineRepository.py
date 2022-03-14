from copy import deepcopy
from Domain.Discipline import Discipline
from Iterable.Iterable import IterableObj,filter,sort


class DisciplineRepository:
    def __init__(self):
        """List that stores all the discipline entries"""
        self.__entities = IterableObj()

    @staticmethod
    def check_is_int(d_id):
        """ Function also used as an ID validator for remove and update
            Returns none if no error is raised"""
        if not d_id.isnumeric():
            raise DisciplineException("ID must be a number!")
        elif int(d_id) < 0:
            raise DisciplineException("ID must be a positive number")
        return None

    def find_by_id(self, entity_id):
        """ Function that finds the given ID, also used as an ID validator for remove and update
            Returns none if id was not found"""
        for i in range(0, len(self.__entities)):
            if int(self.__entities[i].id) == int(entity_id):
                return self.__entities[i]
        return None

    def get_name(self,entity_id):
        for i in range(0, len(self.__entities)):
            if int(self.__entities[i].id) == int(entity_id):
                return self.__entities[i].name
        return None

    def clear(self):
        self.__entities.clear()

    def add(self, d_id,name):
        """ Adds a new discipline to the list, disc being of class Discipline type """
        if DisciplineRepository.find_by_id(self,d_id) is None:
            self.__entities.append(Discipline(d_id,name))
        else:
            raise DisciplineException("ID already used")

    def remove(self, d_id):
        if DisciplineRepository.check_is_int(str(d_id)) is None:
            if DisciplineRepository.find_by_id(self, int(d_id)) is not None:
                for i in range(0, len(self.__entities)):
                    if int(self.__entities[i].id) == int(d_id):
                        self.__entities.pop(i)
                        break
            else:
                raise DisciplineException("Invalid ID")

    def update(self, d_id, new_name):
        if DisciplineRepository.check_is_int(str(d_id)) is None:
            if DisciplineRepository.find_by_id(self, int(d_id)) is not None:
                for i in range(0, len(self.__entities)):
                    if int(self.__entities[i].id) == int(d_id):
                        self.__entities[i].name = new_name
                        break
            else:
                raise DisciplineException("Invalid ID")

    def find_by_name(self, name):
        """ Filters the original list and puts the list of required names in a new one"""
        new_list = list(filter(lambda x: x.name.lower().find(name.lower()) != -1, self.__entities))
        if not new_list:
            raise DisciplineException(f"No entry found for {name}")
        return new_list

    def get_all(self):
        return self.__entities

    def sort_by_id(self):
        self.__entities=sort(self.__entities,lambda x:int(x.id),reverse=False)

    def __len__(self):
        """Modified the len structure in order to fit the entities list"""
        return len(self.__entities)


class DisciplineException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg
