from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import Bug


# Create your tests here.
# Creating four automated bug models tests
# test 1 - to ensure that the bug can be successfully created

class BugModelTests(TestCase):
    def test_was_published_recently_with_future_bug(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_bug = Bug(report_date=time)
        self.assertIs(future_bug.was_published_recently(), False)

class BugModelTest(TestCase):
    def test_create_bug(self):
        bug = Bug.objects.create(
            title="Test Bug",
            description="This is a test bug.",
            bug_type="ERROR",
            status="TO_DO"
        )
        self.assertEqual(bug.title, "Test Bug")
        self.assertEqual(bug.description, "This is a test bug.")
        self.assertEqual(bug.bug_type, "ERROR")
        self.assertEqual(bug.status, "TO_DO")

# test 2 - to ensure that the string representation of the Bug model is correct
class BugModelTest(TestCase):
    def test_bug_string_representation(self):
        bug = Bug.objects.create(
            title="Test Bug",
            description="This is a test bug.",
            bug_type="ERROR",
            status="TO_DO"
        )
        self.assertEqual(str(bug), "Test Bug")

# test 3 - to ensure that the default values of the Bug model are set correctly
class BugModelTest(TestCase):
    def test_bug_default_values(self):
        bug = Bug.objects.create(title="Test Bug")
        self.assertEqual(bug.bug_type, "ERROR")
        self.assertEqual(bug.status, "TO_DO")

# test 4 - to ensure that the bug_type and status fields accept valid choices
class BugModelTest(TestCase):
    def test_bug_valid_choices(self):
        bug = Bug.objects.create(
            title="Test Bug",
            description="This is a test bug.",
            bug_type="FEATURE",
            status="DONE"
        )
        self.assertIn(bug.bug_type, [choice[0] for choice in Bug.BUG_TYPES])
        self.assertIn(bug.status, [choice[0] for choice in Bug.STATUS_CHOICES])


# Creating four automated bug views tests
# test 1 - using the 'register_bug' view, a view test to ensure that bug registration works as expected
class BugViewTest(TestCase):
    def test_register_bug_view(self):
        client = Client()
        response = client.post(reverse('register_bug'), {
            'title': 'Test Bug',
            'description': 'This is a test bug.',
            'bug_type': 'ERROR',
            'status': 'TO_DO',
        })
        self.assertEqual(response.status_code, 302)  # Checks if the registration redirects
        self.assertEqual(Bug.objects.count(), 1)  # Checks if a bug is created
        bug = Bug.objects.first()
        self.assertEqual(bug.title, 'Test Bug')
        self.assertEqual(bug.description, 'This is a test bug.')
        self.assertEqual(bug.bug_type, 'ERROR')
        self.assertEqual(bug.status, 'TO_DO')

# test 2 - using the 'list_bug' view, a view test to ensure that it lists bugs correctly
class BugViewTest(TestCase):
    def test_list_bug_view(self):
        Bug.objects.create(title='Bug 1', description='Description 1', bug_type='ERROR', status='TO_DO')
        Bug.objects.create(title='Bug 2', description='Description 2', bug_type='FEATURE', status='IN_PROGRESS')
        client = Client()
        response = client.get(reverse('list_bug'))
        self.assertEqual(response.status_code, 200)  # Checks if the view returns a successful response
        self.assertQuerysetEqual(response.context['bugs'], ['<Bug: Bug 1>', '<Bug: Bug 2>'], ordered=False)

# test 3 - using the 'view_bug' view, a view test to ensure that it displays bug details correctly
class BugViewTest(TestCase):
    def test_list_bug_view(self):
        Bug.objects.create(title='Bug 1', description='Description 1', bug_type='ERROR', status='TO_DO')
        Bug.objects.create(title='Bug 2', description='Description 2', bug_type='FEATURE', status='IN_PROGRESS')
        client = Client()
        response = client.get(reverse('list_bug'))
        self.assertEqual(response.status_code, 200)  # Checks if the view returns a successful response
        self.assertQuerysetEqual(response.context['bugs'], ['<Bug: Bug 1>', '<Bug: Bug 2>'], ordered=False)

# test 4 - using the 'index' view, a view test to ensure that it renders the correct content
class BugViewTest(TestCase):
    def test_index_view(self):
        client = Client()
        response = self.client.get(reverse('Bug:index'))
        self.assertEqual(response.status_code, 200)  # Checks if the view returns a successful response
        self.assertTemplateUsed(response, 'index.html')

