from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.users.models import User


class LabelsTest(TestCase):
    fixtures = [
        "task_manager/tests/fixtures/labels.json",
        "task_manager/tests/fixtures/users.json"
    ]

    def test_labeles_list(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('labels:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'label_01')
        self.assertEqual(len(response.context['labels']), 2)

    def test_create_label(self):
        self.client.force_login(User.objects.get(pk=1))
        self.status = Label.objects.create(
            name="label_03"
        )
        list_url = reverse("labels:index")
        response = self.client.get(list_url)

        self.assertContains(response, "label_03")
        self.assertContains(response, "label_01")

    def test_update_label(self):
        update_url = reverse("labels:update", kwargs={"pk": 1})
        list_url = reverse("labels:index")

        new_status = {
            "name": "label_04"
        }

        self.client.force_login(User.objects.get(pk=1))
        self.client.post(update_url, data=new_status)
        response = self.client.get(list_url)

        self.assertContains(response, "label_04")
        self.assertContains(response, "label_02")
        self.assertNotContains(response, "label_01")

    def test_delete_label(self):
        delete_url = reverse("labels:delete", kwargs={"pk": 2})
        list_url = reverse("labels:index")

        self.client.force_login(User.objects.get(pk=1))
        self.client.post(delete_url)

        response = self.client.get(list_url)

        self.assertNotContains(response, "label_02")
        self.assertContains(response, "label_01")
