from Repository.DisciplineRepository import DisciplineException
from Repository.StudentRepository import StudentException
from Repository.GradeRepository import GradeException
from Services.Handlers import UndoHandler
from Services.UndoService import UndoManager


class UI:
    def __init__(self, main_service):
        """Class used in order to call the required functionalities from the service class"""
        self.__service = main_service

    @staticmethod
    def print_menu_options():
        """ Prints the available options at each iteration of the program """
        print("\n1.Display the list of students\n"
              "2.Add a student to the list\n"
              "3.Remove a student from the list\n"
              "4.Update a student from the list\n"
              "5.Display the list of disciplines\n"
              "6.Add a discipline to the list\n"
              "7.Remove a discipline from the list\n"
              "8.Update a discipline from the list\n"
              "9.Add a grade\n"
              "10.Display all grades\n"
              "11.Display student by ID\n"
              "12.Display student by name\n"
              "13.Display discipline by ID\n"
              "14.Display discipline by name\n"
              "15.Display all students that are failing\n"
              "16.Display all students in descending order by their grade\n"
              "17.Display all disciplines in descending order by their grade\n"
              "18.Undo\n"
              "19.Redo\n"
              "20.Populate entries\n"
              "0.Exit\n")

    @staticmethod
    def ui_list(final_list):
        """ UI static function that prints a given class list"""
        for elem in final_list:
            print(elem)

    def ui_print_students(self):
        """Option 1"""
        final_list = self.__service.list_student()
        UI.ui_list(final_list)

    def ui_add_student(self):
        """Option 2"""
        s_id = input("Enter the new student's ID: ")
        name = input("Enter the new student's name: ")
        # remainder_list = []
        self.__service.add_student(s_id, name)
        UndoManager.register_operation(self.__service, UndoHandler.ADD_STUDENT, int(s_id),name)

    def ui_remove_student(self):
        """Option 3"""
        remainder_list = []
        s_id = input("Enter the id of the student you want to remove: ")
        old_name = self.__service.get_student_name(s_id)
        self.__service.remove_student(s_id, remainder_list)
        UndoManager.register_operation(self.__service, UndoHandler.DELETE_STUDENT, int(s_id),
                                       old_name, remainder_list)

    def ui_update_student(self):
        """Option 4"""
        s_id = input("Enter the id of the student you want to update: ")
        name = input("Enter the updated name: ")
        old_name = self.__service.get_student_name(s_id)
        self.__service.update_student(s_id, name)
        UndoManager.register_operation(self.__service, UndoHandler.UPDATE_STUDENT, int(s_id), old_name)

    def ui_print_disciplines(self):
        """Option 5"""
        final_list = self.__service.list_discipline()
        UI.ui_list(final_list)

    def ui_add_discipline(self):
        """Option 6"""
        d_id = input("Enter the new discipline's ID: ")
        name = input("Enter the new discipline's name: ")
        # remainder_list = []
        self.__service.add_discipline(d_id, name)
        UndoManager.register_operation(self.__service, UndoHandler.ADD_DISCIPLINE, int(d_id),name)

    def ui_remove_discipline(self):
        """Option 7"""
        remainder_list = []
        d_id = input("Enter the id of the discipline you want to remove: ")
        old_name = self.__service.get_discipline_name(d_id)

        self.__service.remove_discipline(d_id, remainder_list)
        UndoManager.register_operation(self.__service, UndoHandler.DELETE_DISCIPLINE, int(d_id),
                                       old_name, remainder_list)

    def ui_update_discipline(self):
        """Option 8"""
        d_id = input("Enter the id of the discipline you want to update: ")
        name = input("Enter the updated name: ")
        old_name = self.__service.get_discipline_name(d_id)
        self.__service.update_discipline(d_id, name)
        UndoManager.register_operation(self.__service, UndoHandler.UPDATE_DISCIPLINE, int(d_id), old_name)

    def ui_add_grade(self):
        """Option 9"""
        s_id = input("Enter the id of the student: ")
        d_id = input("Enter the id of the discipline: ")
        grade = input("Enter the grade: ")
        self.__service.add_grade(s_id, d_id, grade)
        UndoManager.register_operation(self.__service, UndoHandler.ADD_GRADE)

    def ui_print_grades(self):
        """Option 10"""
        final_list = self.__service.list_grade()
        UI.ui_list(final_list)

    def ui_find_student_by_id(self):
        """Option 11"""
        s_id = input("Enter ID:")
        print(self.__service.find_s_id(s_id))

    def ui_find_student_by_name(self):
        """Option 12"""
        name = input("Enter name: ")
        filtered_list = self.__service.find_s_name(name)
        print(f"{len(filtered_list)} student(s) matching '{name}': ")
        UI.ui_list(filtered_list)

    def ui_find_discipline_by_id(self):
        """Option 13"""
        d_id = input("Enter ID: ")
        print(self.__service.find_d_id(d_id))

    def ui_find_discipline_by_name(self):
        """Option 14"""
        name = input("Enter name: ")
        filtered_list = self.__service.find_d_name(name)
        print(f"{len(filtered_list)} discipline(s) matching '{name}': ")
        UI.ui_list(filtered_list)

    def ui_print_failing_students(self):
        """Option 15"""
        filtered_list = self.__service.print_failing_students()
        print(f"There are {len(filtered_list)} students that are failing at least at one discipline : ")
        UI.ui_list(filtered_list)

    def ui_print_best_students(self):
        """Option 16"""
        name_list, grade_list = self.__service.print_best_students()
        for i in range(0, len(name_list)):
            print(name_list[i], "Avg Grade: ", grade_list[i], sep=' ')

    def ui_print_best_disciplines(self):
        """Option 17"""
        name_list, grade_list = self.__service.print_best_disciplines()
        for i in range(0, len(name_list)):
            print(name_list[i], "Avg Grade: ", grade_list[i], sep=' ')

    def ui_undo(self):
        if UndoManager.undo()==-1:
            print("No more undos available!")
        else:
            UndoManager.undo()
            print("Undo successful!")

    def ui_redo(self):
        if UndoManager.redo()==-1:
            print("No more redos available")
        else:
            UndoManager.redo()
            print("Redo successful!")

    def ui_populate_db(self):
        self.__service.test_all()

    def main_ui(self):
        """ Directs the option inputed from the console to its required functionality """
        options = {1: UI.ui_print_students, 2: UI.ui_add_student, 3: UI.ui_remove_student, 4: UI.ui_update_student,
                   5: UI.ui_print_disciplines, 6: UI.ui_add_discipline, 7: UI.ui_remove_discipline,
                   8: UI.ui_update_discipline, 9: UI.ui_add_grade, 10: UI.ui_print_grades, 11: UI.ui_find_student_by_id,
                   12: UI.ui_find_student_by_name, 13: UI.ui_find_discipline_by_id, 14: UI.ui_find_discipline_by_name,
                   15: UI.ui_print_failing_students, 16: UI.ui_print_best_students, 17: UI.ui_print_best_disciplines,
                   18: UI.ui_undo, 19: UI.ui_redo,20:UI.ui_populate_db}
        while True:
            try:
                UI.print_menu_options()
                opt = int(input("Enter your option: "))
                if opt in options:
                    options[opt](self)
                elif opt == 0:
                    break
                else:
                    print("Invalid command")
            except ValueError as ex:  # value error for non integer option
                print(ex)
            except DisciplineException as de:
                print(de)
            except StudentException as st:
                print(st)
            except GradeException as gr:
                print(gr)
