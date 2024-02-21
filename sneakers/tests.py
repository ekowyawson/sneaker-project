from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Sneaker


class ThingTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = Sneaker.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_thing.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_things_model(self):
        sneaker = Sneaker.objects.get(id=1)
        actual_owner = str(sneaker.owner)
        actual_name = str(sneaker.name)
        actual_description = str(sneaker.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_thing_list(self):
        url = reverse("thing_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0]["name"], "rake")

    def test_get_thing_by_id(self):
        url = reverse("thing_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sneaker = response.data
        self.assertEqual(sneaker["name"], "rake")

    def test_create_thing(self):
        url = reverse("thing_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        things = Sneaker.objects.all()
        self.assertEqual(len(things), 2)
        self.assertEqual(Sneaker.objects.get(id=2).name, "spoon")

    def test_update_thing(self):
        url = reverse("thing_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sneaker = Sneaker.objects.get(id=1)
        self.assertEqual(sneaker.name, data["name"])
        self.assertEqual(sneaker.owner.id, data["owner"])
        self.assertEqual(sneaker.description, data["description"])

    def test_delete_thing(self):
        url = reverse("thing_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        things = Sneaker.objects.all()
        self.assertEqual(len(things), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("thing_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
