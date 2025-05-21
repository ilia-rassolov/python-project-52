from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.users.models import User


class StatusTest(TestCase):
    fixtures = [
        "task_manager/tests/fixtures/users.json",
        "task_manager/tests/fixtures/statuses.json"
    ]

    def test_statuses_list(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('statuses:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'status_01')
        self.assertEqual(len(response.context['statuses']), 2)

    def test_status_status(self):
        self.client.force_login(User.objects.get(pk=1))
        self.status = Status.objects.create(
            name="status_03"
        )
        list_url = reverse("statuses:index")
        response = self.client.get(list_url)

        self.assertContains(response, "status_03")
        self.assertContains(response, "status_01")

    def test_update_status(self):
        update_url = reverse("statuses:update", kwargs={"pk": 1})
        list_url = reverse("statuses:index")

        new_status = {
            "name": "status_04"
        }

        self.client.force_login(User.objects.get(pk=1))
        self.client.post(update_url, data=new_status)
        response = self.client.get(list_url)

        self.assertContains(response, "status_04")
        self.assertContains(response, "status_02")
        self.assertNotContains(response, "status_01")

    def test_delete_status(self):
        delete_url = reverse("statuses:delete", kwargs={"pk": 2})
        list_url = reverse("statuses:index")

        self.client.force_login(User.objects.get(pk=1))
        self.client.post(delete_url)

        response = self.client.get(list_url)

        self.assertNotContains(response, "status_02")
        self.assertContains(response, "status_01")
