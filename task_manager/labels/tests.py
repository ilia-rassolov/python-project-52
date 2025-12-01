from django.test import TestCase
from django.urls import reverse


# class LabelsTest(TestCase):
#     def test_labels_list(self):
#         response = self.client.get(reverse("labels:index"))
#         self.assertEqual(response.status_code, 200)
#
#         self.assertIn("labels", response.context)
#         labels = response.context["labels"]
#
#         self.assertTrue(len(labels) > 0)