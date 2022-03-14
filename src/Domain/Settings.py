from FileRepository.DisciplinePickleRepository import DisciplinePickleRepository
from FileRepository.StudentPickleRepository import StudentPickleRepository
from FileRepository.GradePickleRepository import GradePickleRepository
from FileRepository.GradeFileRepository import GradeFileRepository
from FileRepository.StudentFileRepository import StudentFileRepository
from FileRepository.DisciplineFileRepository import DisciplineFileRepository
from FileRepository.StudentJsonRepository import StudentJsonRepository
from FileRepository.DisciplineJsonRepository import DisciplineJsonRepository
from FileRepository.GradeJsonRepository import GradeJsonRepository
from Repository.DisciplineRepository import DisciplineRepository
from Repository.GradeRepository import GradeRepository
from Repository.StudentRepository import StudentRepository
from Services.Service import Service
from UI.UI import UI


class Settings:
    def __init__(self, config):
        self.__config = config
        self.__settings = []

    def read_settings(self):
        with open(self.__config, "r+") as f:
            lines = f.read().split('\n')
            settings = []
            for line in lines:
                setting = line.split('=')
                if len(setting) > 1:
                    self.__settings.append(setting[1].strip())

    def config(self):
        student_repo = None
        discipline_repo = None
        grade_repo = None

        if self.__settings[0] == "inmemory":
            student_repo = StudentRepository()
            discipline_repo = DisciplineRepository()
            grade_repo = GradeRepository()
        elif self.__settings[0] == "textfiles":
            student_repo = StudentFileRepository(self.__settings[1])
            discipline_repo = DisciplineFileRepository(self.__settings[2])
            grade_repo = GradeFileRepository(self.__settings[3])
        elif self.__settings[0] == "binaryfiles":
            student_repo=StudentPickleRepository(self.__settings[1])
            discipline_repo=DisciplinePickleRepository(self.__settings[2])
            grade_repo=GradePickleRepository(self.__settings[3])
        elif self.__settings[0] == "json":
            student_repo = StudentJsonRepository(self.__settings[1])
            discipline_repo=DisciplineJsonRepository(self.__settings[2])
            grade_repo = GradeJsonRepository(self.__settings[3])
        else:
            print("Invalid settings input!")
        service = Service(student_repo, discipline_repo, grade_repo)
        console = UI(service)
        console.main_ui()


