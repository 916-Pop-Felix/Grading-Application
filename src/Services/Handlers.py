from enum import Enum

from Services.UndoService import UndoManager


def add_student_handler(s_service, s_id, name):
    remainder_list = []
    s_service.remove_student(s_id, remainder_list)
    s_service.sort_student_by_id()
    UndoManager.register_operation_redo(s_service, RedoHandler.ADD_STUDENT_REDO, int(s_id), name, remainder_list)


def delete_student_handler(s_service, s_id, s_name, remainder_list):
    s_service.add_student(s_id, s_name)
    s_service.add_remainder_grades(remainder_list)
    s_service.sort_student_by_id()
    UndoManager.register_operation_redo(s_service, RedoHandler.DELETE_STUDENT_REDO,int(s_id), s_name)


def update_student_handler(s_service, s_id, s_name):
    old_name = s_service.get_student_name(s_id)
    s_service.update_student(s_id, s_name)
    UndoManager.register_operation_redo(s_service,RedoHandler.UPDATE_STUDENT_REDO,s_id,old_name)


def add_discipline_handler(d_service, d_id, name):
    remainder_list = []
    d_service.remove_discipline(d_id, remainder_list)
    d_service.sort_discipline_by_id()
    UndoManager.register_operation_redo(d_service, RedoHandler.ADD_DISCIPLINE_REDO, int(d_id), name, remainder_list)


def delete_discipline_handler(d_service, d_id, d_name, remainder_list):
    d_service.add_discipline(d_id, d_name)
    d_service.add_remainder_grades(remainder_list)
    d_service.sort_discipline_by_id()
    UndoManager.register_operation_redo(d_service, RedoHandler.DELETE_DISCIPLINE_REDO, int(d_id), d_name)


def update_discipline_handler(d_service, d_id, d_name):
    old_name = d_service.get_discipline_name(d_id)
    d_service.update_discipline(d_id, d_name)
    UndoManager.register_operation_redo(d_service, RedoHandler.UPDATE_DISCIPLINE_REDO, d_id, old_name)

def add_grade_handler(g_service):
    added_grade=g_service.get_last_added()
    g_service.remove_grade()
    UndoManager.register_operation(g_service,RedoHandler.ADD_GRADE_REDO,added_grade.s_id,
                                   added_grade.d_id,added_grade.grades)

class UndoHandler(Enum):
    ADD_STUDENT = add_student_handler
    DELETE_STUDENT = delete_student_handler
    UPDATE_STUDENT = update_student_handler
    ADD_DISCIPLINE = add_discipline_handler
    DELETE_DISCIPLINE = delete_discipline_handler
    UPDATE_DISCIPLINE = update_discipline_handler
    ADD_GRADE = add_grade_handler


def add_student_handler_redo(s_service, s_id, s_name, remainder_list):
    s_service.add_student(s_id, s_name)
    s_service.add_remainder_grades(remainder_list)
    s_service.sort_student_by_id()
    UndoManager.register_operation(s_service, UndoHandler.ADD_STUDENT, int(s_id), s_name)


def delete_student_handler_redo(s_service, s_id, name):
    remainder_list = []
    s_service.remove_student(s_id, remainder_list)
    s_service.sort_student_by_id()
    UndoManager.register_operation(s_service, UndoHandler.DELETE_STUDENT, int(s_id), name, remainder_list)

def update_student_handler_redo(s_service,s_id,s_name):
    old_name=s_service.get_student_name(s_id)
    s_service.update_student(s_id,s_name)
    UndoManager.register_operation(s_service,UndoHandler.UPDATE_STUDENT,int(s_id),old_name)

def add_discipline_handler_redo(d_service, d_id, d_name, remainder_list):
    d_service.add_discipline(d_id, d_name)
    d_service.add_remainder_grades(remainder_list)
    d_service.sort_discipline_by_id()
    UndoManager.register_operation(d_service, UndoHandler.ADD_DISCIPLINE, int(d_id), d_name)

def delete_discipline_handler_redo(d_service, d_id, name):
    remainder_list = []
    d_service.remove_discipline(d_id, remainder_list)
    d_service.sort_discipline_by_id()
    UndoManager.register_operation(d_service, UndoHandler.DELETE_DISCIPLINE, int(d_id), name, remainder_list)

def update_discipline_handler_redo(d_service,d_id,d_name):
    old_name=d_service.get_discipline_name(d_id)
    d_service.update_discipline(d_id,d_name)
    UndoManager.register_operation(d_service,UndoHandler.UPDATE_DISCIPLINE,int(d_id),old_name)

def add_grade_handler_redo(g_service, s_id, d_id, grade):
    g_service.add_grade(s_id, d_id, grade)
    UndoManager.register_operation(g_service,UndoHandler.ADD_GRADE)

class RedoHandler(Enum):
    ADD_STUDENT_REDO = add_student_handler_redo
    DELETE_STUDENT_REDO = delete_student_handler_redo
    UPDATE_STUDENT_REDO=update_student_handler_redo
    ADD_DISCIPLINE_REDO=add_discipline_handler_redo
    DELETE_DISCIPLINE_REDO = delete_discipline_handler_redo
    UPDATE_DISCIPLINE_REDO = update_discipline_handler_redo
    ADD_GRADE_REDO = add_grade_handler_redo
