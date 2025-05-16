from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class UsersTest(TestCase):
    fixtures = ["task_manager/tests/fixtures/users.json"]

    def test_users_list(self):
        response = self.client.get(reverse('users:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'user_01')
        self.assertEqual(len(response.context['users']), 2)

    def test_create_user(self):
        self.user = User.objects.create(
            username="username_03",
            first_name="user_03"
        )
        list_url = reverse("users:index")
        response = self.client.get(list_url)

        self.assertContains(response, "user_03")
        self.assertContains(response, "user_01")

    def test_update_user(self):
        update_url = reverse("users:update", kwargs={"pk": 1})
        list_url = reverse("users:index")

        new_user = {
            "password1": "password_04",
            "password2": "password_04",
            "first_name": "user_04",
            "last_name": "u_04",
            "username": "username_04"
        }

        self.client.force_login(get_user_model().objects.get(pk=1))
        self.client.post(update_url, data=new_user)
        response = self.client.get(list_url)

        self.assertContains(response, "user_04")
        self.assertContains(response, "user_02")
        self.assertNotContains(response, "user_01")

    def test_delete_user(self):
        delete_url = reverse("users:delete", kwargs={"pk": 2})
        list_url = reverse("users:index")

        self.client.force_login(get_user_model().objects.get(pk=2))
        self.client.post(delete_url)

        response = self.client.get(list_url)

        self.assertNotContains(response, "user_02")
        self.assertContains(response, "user_01")
