# copied from https://github.com/prashgec/bbk.git
# run from project root with:
# python -m unittest discover -s tests -v
# discover: scan your project folders and automatically find any files containing tests
# -s tests: The -s stands for "start directory": start looking for tests inside folder named tests
# -v: "verbose": forces the output to print the exact name of every test function it runs alongside its status

import unittest
from fastapi import HTTPException

from main import home
from routers.students import get_student, get_students

class UniversityApiTests(unittest.TestCase):
    def test_home_returns_api_summary(self):
        response = home()

        self.assertEqual(response["name"], "University API")
        self.assertEqual(response["version"], "1.0.0")
        self.assertIn("all_students", response["endpoints"])

    def test_get_students_returns_seeded_students(self):
        response = get_students()

        self.assertEqual(set(response), {"s1", "s2", "s3"})
        self.assertEqual(response["s2"]["name"], "Maria Garcia")

    def test_get_student_returns_matching_student(self):
        response = get_student("s1")

        self.assertEqual(response["name"], "John Smith")
        self.assertEqual(response["student_id"], "S12345")

    def test_get_student_raises_not_found_for_unknown_id(self):
        with self.assertRaises(HTTPException) as context:
            get_student("unknown")

        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Student not found")


if __name__ == "__main__":
    unittest.main()