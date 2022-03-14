from Repository.DisciplineRepository import  DisciplineRepository
import pickle

class DisciplinePickleRepository(DisciplineRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        f = open(self.__file_name, "rb")
        try:
            self._DisciplineRepository__entities=pickle.load(f)
        except Exception as e:
            print(e)
        finally:
            f.close()


    def add(self, s_id,name):
        super().add(s_id,name)
        self.__save()

    def remove(self, s_id):
        super().remove(s_id)
        self.__save()

    def update(self, s_id, new_name):
        super().update(int(s_id),new_name)
        self.__save()

    def __save(self):
        f = open(self.__file_name, 'wb')
        pickle.dump(self.get_all(),f)
        f.close()