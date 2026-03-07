from django.test import TestCase
from .models import Department, Student

class DepartmentModelTest(TestCase):
    def test_department_creation(self):
        department = Department.objects.create(
            name="Computer Science",
            head_of_department="Dr. Smith",
            description="CS Department"
        )
        self.assertEqual(department.name, "Computer Science")
        self.assertEqual(str(department), "Computer Science")

class StudentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name="Computer Science",
            head_of_department="Dr. Smith"
        )

    def test_student_creation(self):
        student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            department=self.department
        )
        self.assertEqual(student.first_name, "John")
        self.assertEqual(str(student), "John Doe")
