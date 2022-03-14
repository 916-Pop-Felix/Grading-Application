from Repository.GradeRepository import  GradeRepository
import pickle

class GradePickleRepository(GradeRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        f = open(self.__file_name, "rb")
        try:
            self._GradeRepository__entities=pickle.load(f)
        except Exception as e:
            print(e)
        finally:
            f.close()


    def add(self,grade):
        super().add(grade)
        self.__save()

    def remove_s(self, stud_id,remainder_list=None):
        super().remove_s(stud_id,remainder_list)
        self.__save()

    def remove_d(self, disc_id,remainder_list=None):
        super().remove_d(disc_id,remainder_list)
        self.__save()

    def __save(self):
        f = open(self.__file_name, 'wb')
        pickle.dump(self.get_all(),f)
        f.close()