from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.test import TestCase
from django.urls import reverse

from  task_manager.tests.parse_data import parse_data


User = get_user_model()
users_data = parse_data('task_manager/tests/fixtures/setup_data.json', "users")


class UsersTest(TestCase):
    fixtures = ["task_manager/tests/fixtures/users.json"]

    def setUp(self):
        self.new_user = users_data["new_user"]
        self.wrong_update_user = users_data["wrong_update_user"]
        self.success_update_user = users_data["success_update_user"]

    def test_users_list(self):
        response = self.client.get(reverse('users:index'))
        users_count = User.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, 'boss')
        self.assertContains(response, 'michail')
        self.assertContains(response, 'ivanovich')
        self.assertEqual(users_count, 2)

    def test_create_user(self):
        response = self.client.get(reverse('users:signup'))

        self.assertTemplateUsed(response, 'create_update_form.html')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('users:signup'),
            data=self.new_user,
            follow=True,
        )
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('User registered successfully'))

        last_user = User.objects.last()
        users_count = User.objects.count()
        self.assertEqual(last_user.first_name, "maxim")
        self.assertEqual(last_user.last_name, "sergeev")
        self.assertEqual(last_user.username, "manager")
        self.assertEqual(users_count, 3)

    def test_update_user(self):
        update_url = reverse("users:update", kwargs={"pk": 2})
        list_url = reverse("users:index")

        self.client.force_login(get_user_model().objects.get(pk=2))
        self.client.post(update_url,
                         data=self.wrong_update_user,
                         follow=True,
                         )

        response = self.client.get(list_url)

        self.assertContains(response, "boss")
        self.assertNotContains(response, "not_coworker")

        # self.client.force_login(get_user_model().objects.get(pk=2))
        self.client.post(update_url,
                         data=self.success_update_user,
                         follow=True,
                         )
        response = self.client.get(list_url)

        # self.assertRedirects(response, reverse('users:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('User is successfully update'))

        self.assertContains(response, "hr")
        self.assertNotContains(response, "boss")


    # def test_delete_user(self):
    #     delete_url = reverse("users:delete", kwargs={"pk": 2})
    #     list_url = reverse("users:index")
    #
    #     self.client.force_login(get_user_model().objects.get(pk=2))
    #     self.client.post(delete_url)
    #
    #     response = self.client.get(list_url)
    #
    #     self.assertNotContains(response, "user_02")
    #     self.assertContains(response, "user_01")
