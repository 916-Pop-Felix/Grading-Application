from Domain.Grade import Grade
from Repository.GradeRepository import GradeRepository


class GradeFileRepository(GradeRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            f = open(self.__file_name, "rt")
            lines = f.readlines()
            f.close()
            for line in lines:
                if not line.strip():
                    continue
                else:
                    line = line.split(';')
                    super().add(Grade(line[0], line[1],line[2]))
        except IOError:
            print("File error in "+str(self.__file_name))

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
        try:
            f = open(self.__file_name, 'wt')
            for grade in self.get_all():
                line = str(grade.s_id) + ';' + str(grade.d_id)+';'+str(grade.grades)+'\n'
                f.write(line)
            f.close()
        except Exception as e:
            print(str(e)+" File error in "+str(self.__file_name))