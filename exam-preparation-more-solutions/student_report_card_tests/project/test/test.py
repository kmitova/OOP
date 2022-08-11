from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def test_init_is_correct(self):
        card = StudentReportCard('student', 9)
        self.assertEqual('student', card.student_name)
        self.assertEqual(9, card.school_year)
        self.assertEqual({}, card.grades_by_subject)

    def test_name_setter_invalid_raises(self):
        card = StudentReportCard('student', 9)
        with self.assertRaises(ValueError) as ex:
            card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_year_setter_invalid_raises_less_than_one(self):
        card = StudentReportCard('student', 9)
        with self.assertRaises(ValueError) as ex:
            card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_year_setter_invalid_raises_less_more_than_twelve(self):
        card = StudentReportCard('student', 9)
        with self.assertRaises(ValueError) as ex:
            card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_new_subject(self):
        card = StudentReportCard('student', 9)
        self.assertEqual(0, len(card.grades_by_subject))
        card.add_grade('math', 6)
        self.assertEqual({'math': [6]}, card.grades_by_subject)

    def test_add_grade_existing_subject(self):
        card = StudentReportCard('student', 9)
        card.grades_by_subject = {'math': [6]}
        card.add_grade('math', 4)
        self.assertEqual({'math': [6, 4]}, card.grades_by_subject)
        self.assertTrue(2, len(card.grades_by_subject['math']))

    def test_avg_grade_subject(self):
        card = StudentReportCard('student', 9)
        card.grades_by_subject = {'math': [6, 4]}
        result = card.average_grade_by_subject()
        expected = "math: 5.00"
        self.assertEqual(expected, result)

    def test_avg_grade_all(self):
        card = StudentReportCard('student', 9)
        card.grades_by_subject = {'math': [6, 4]}
        result = card.average_grade_for_all_subjects()
        expected = "Average Grade: 5.00"
        self.assertEqual(expected, result)

    def test_repr_method(self):
        card = StudentReportCard('student', 9)
        card.grades_by_subject = {'math': [6, 4]}
        expected = """Name: student
Year: 9
----------
math: 5.00
----------
Average Grade: 5.00"""
        result = repr(card)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

