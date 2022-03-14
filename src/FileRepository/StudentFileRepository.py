from Repository.StudentRepository import StudentRepository


class StudentFileRepository(StudentRepository):
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
                    super().add(line[0], line[1])
        except IOError:
            print("File error in "+str(self.__file_name))



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
        try:
            f = open(self.__file_name, 'wt')
            print(len(self.get_all()))
            for stud in self.get_all():
                line = str(stud.id) + ';' + stud.name+'\n'
                f.write(line)
            f.close()
        except Exception as e:
            print(str(e)+" File error in "+str(self.__file_name))