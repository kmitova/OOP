from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student('test', {'math': ['note1', 'note2'], 'english': ['note3', 'note4']})

    def test_is_initialized_correctly(self):
        student = Student('test')
        self.assertEqual('test', student.name)
        self.assertEqual({}, student.courses)
        student = Student('test', {'math': ['note1', 'note2']})
        self.assertEqual({'math': ['note1', 'note2']}, student.courses)

    def test_enroll_when_already_enrolled_and_add_notes(self):
        result = self.student.enroll('math', ['new note'])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'new note'], self.student.courses['math'])

    def test_enroll_in_new_course_with_notes_y(self):
        course = 'biology'
        notes = ['note5', 'note6']
        result = self.student.enroll(course, notes, 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_in_new_course_with_notes_empty_string(self):
        course = 'biology'
        notes = ['note5', 'note6']
        result = self.student.enroll(course, notes, '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_in_course_without_notes(self):
        course = 'biology'
        notes = ['note5', 'note6']
        result = self.student.enroll(course, notes, 'N')
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_to_course_that_doesnt_exist_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('physics', ['new'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_valid_course(self):
        course = 'math'
        notes = 'new'
        self.student.add_notes(course, notes)
        self.assertTrue(notes in self.student.courses[course])
        self.assertEqual("Notes have been updated", self.student.add_notes(course, notes))

    def test_leave_course_that_is_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('physics')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_valid_course(self):
        course = 'math'
        result = self.student.leave_course(course)
        self.assertEqual("Course has been removed", result)
        self.assertFalse(course in self.student.courses)

if __name__ == '__main__':
    main()
