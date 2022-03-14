from Repository.StudentRepository import StudentRepository
import json
class StudentJsonRepository(StudentRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        f = open(self.__file_name, "rb")
        try:
            data=json.loads(f.read().decode())
            for line in data:
                super().add(line["_Student__id"],line["_Student__name"])
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
        f.write(json.dumps([x.__dict__ for x in list(self._StudentRepository__entities)], indent=4, sort_keys=True,
                           ).encode())  #  dict presents the list of entities in a dictionary format
        f.close()