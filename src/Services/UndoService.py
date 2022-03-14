from dataclasses import dataclass


@dataclass
class UndoOperation:
    target_object: object
    handler: object
    args: tuple


class UndoManager:
    __undo_operations = []
    __redo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *args):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, args))
        UndoManager.__redo_operations.clear()

    @staticmethod
    def register_operation_redo(target_object, handler, *args):
        UndoManager.__redo_operations.append(UndoOperation(target_object, handler, args))

    @staticmethod
    def undo():
        if len(UndoManager.__undo_operations)!=0:
            undo_operation = UndoManager.__undo_operations.pop()
            undo_operation.handler(undo_operation.target_object, *undo_operation.args)
            return 1
        else:
            return -1

    @staticmethod
    def redo():
        if len(UndoManager.__redo_operations)!=0:
            redo_operation = UndoManager.__redo_operations.pop()
            redo_operation.handler(redo_operation.target_object, *redo_operation.args)
            return 1
        else:
            return -1

