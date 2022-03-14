from Domain.Grade import Grade
import json
from Repository.GradeRepository import  GradeRepository

class GradeJsonRepository(GradeRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        f = open(self.__file_name, "rb")
        try:
            data=json.loads(f.read().decode())
            for line in data:
                super().add(Grade(line["_Grade__s_id"],line["_Grade__d_id"],line["_Grade__grades"]))
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
        f.write(json.dumps([x.__dict__ for x in list(self._GradeRepository__entities)], indent=4, sort_keys=True,
                           ).encode())
        f.close()