import unittest
import TaskManager


class MyTestCase(unittest.TestCase):
    def test_task(self):
        task = TaskManager.Task('Name', 'Ooof')
        self.assertEqual(task.get_name(), 'Name')
        self.assertEqual(task.get_description(), 'Ooof')

    def test_complex_task(self):
        comp_task = TaskManager.ComplexTask('complex task name', 'complex task description',
                                            'subtask name', 'subtask description')
        self.assertFalse(comp_task.is_empty())
        self.assertEqual(comp_task.get_description(), 'complex task description')
        comp_task.delete_subtask(0)
        self.assertTrue(comp_task.is_empty())

    def test_taskmanager(self):
        tm = TaskManager.TaskManager()
        tm.create_task('Name', 'Ooof')
        self.assertEqual(tm.get_tasks()[0][0].get_name(), 'Name')
        self.assertEqual(tm.get_tasks()[0][0].get_description(), 'Ooof')
        tm.create_complex_task('complex task name', 'complex task description',
                                            'subtask name', 'subtask description')
        self.assertEqual(len(tm.get_tasks()), 2)
        tm.delete_task(1, 0)
        tm.delete_task(0)
        self.assertEqual(tm.get_tasks(), {})


if __name__ == '__main__':
    unittest.main()
