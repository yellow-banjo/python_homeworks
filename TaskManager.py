class Task:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description


class ComplexTask:
    def __init__(self, name, description, subtask_name, subtask_description):
        self.__id = 0
        self.__name = name
        self.__description = description
        self.__subtasks = dict()
        self.create_subtask(subtask_name, subtask_description)

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def _id(self):
        cur = self.__id
        self.__id += 1
        return cur

    def create_subtask(self, name, description):
        idx = self._id()
        self.__subtasks[idx] = Task(name, description)

    def get_subtasks(self):
        return self.__subtasks

    def print_subtasks(self):
        print('_'*34)
        print('| id |    name    | description ')
        print('-' * 34)
        for idx, task in self.__subtasks.items():
            print('|' + f'{idx:^4}' + '|' + f'{task.get_name():^12}' + '|' + f'{task.get_description()}')

    def is_empty(self):
        if len(self.__subtasks) == 0:
            return True
        else:
            return False

    def delete_subtask(self, idx):
        self.__subtasks.pop(idx)


class TaskManager:
    def __init__(self):
        self.__id = 0
        self.__tasks = dict()

    def _id(self):
        cur = self.__id
        self.__id += 1
        return cur

    def create_task(self, name, description):
        idx = self._id()
        self.__tasks[idx] = (Task(name, description), 'task')

    def create_complex_task(self, name, description, subtask_name, subtask_description):
        idx = self._id()
        self.__tasks[idx] = (ComplexTask(name, description, subtask_name, subtask_description), 'complex task')

    def create_subtask(self, idx, name, description):
        self.__tasks[idx][0].create_subtask(name, description)

    def print_subtasks(self, idx):
        self.__tasks[idx][0].print_subtasks()

    def get_subtasks(self, idx):
        return self.__tasks[idx][0].get_subtasks()

    def get_tasks(self):
        return self.__tasks

    def print_tasks(self, filter_tasks=None):
        print('_'*34)
        print('| id |    name    | type of task |')
        print('-' * 34)
        for idx, task in self.__tasks.items():
            if filter_tasks is None:
                print('|' + f'{idx:^4}' + '|' + f'{task[0].get_name():^12}' + '|' + f'{task[1]:^14}' + '|')
            elif filter_tasks == 'tasks':
                if task[1] == 'task':
                    print('|' + f'{idx:^4}' + '|' + f'{task[0].get_name():^12}' + '|' + f'{task[1]:^14}' + '|')
            elif filter_tasks == 'complex tasks':
                if task[1] == 'complex task':
                    print('|' + f'{idx:^4}' + '|' + f'{task[0].get_name():^12}' + '|' + f'{task[1]:^14}' + '|')

    def describe_by_id(self, idx):
        task, type_of_task = self.__tasks[idx]
        print('id =', idx, 'name =', task.get_name(), 'description = ', task.get_description(), 'type =', type_of_task)

    def delete_task(self, *idx):
        if len(idx) == 2:
            a, b = idx
            self.__tasks[a][0].delete_subtask(b)
            if self.__tasks[a][0].is_empty():
                self.__tasks.pop(a)
        elif len(idx) == 1:
            a, = idx
            self.__tasks.pop(a)


def main():
    tm = TaskManager()
    tm.create_task('task 1', 'disc 1')
    tm.create_task('task 2', 'disc 2')
    tm.create_task('task 3', 'disc 3')
    tm.create_complex_task('complex', 'hm', 'subtask', 'bla bla bla')
    tm.print_tasks()
    tm.describe_by_id(3)
    tm.print_subtasks(3)
    tm.print_tasks()


if __name__ == '__main__':
    main()
