from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

# Create your tests here.
class TaskAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': False,
        }
        self.task = Task.objects.create(**self.task_data)
        self.valid_payload = {
            'title': 'Updated Task',
            'description': 'This is an updated test task',
            'completed': True,
        }
        self.invalid_payload = {
            'title': '',
            'description': '',
            'completed': True,
        }

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_task(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_create_valid_task(self):
        response = self.client.post(reverse('task-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        response = self.client.post(reverse('task-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task(self):
        response = self.client.put(reverse('task-detail', kwargs={'pk': self.task.pk}), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, self.valid_payload['title'])

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
