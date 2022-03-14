from Repository.DisciplineRepository import DisciplineRepository


class DisciplineFileRepository(DisciplineRepository):
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

    def add(self, d_id,name):
        super().add(d_id,name)
        self.__save()

    def remove(self, d_id):
        super().remove(d_id)
        self.__save()

    def __save(self):
        try:
            f = open(self.__file_name, 'wt')
            for disc in self.get_all():
                line = str(disc.id) + ';' + disc.name+'\n'
                f.write(line)
            f.close()
        except Exception as e:
            print(str(e)+" File error in "+str(self.__file_name))