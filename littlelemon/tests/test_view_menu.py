from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

        self.menu1 = Menu.objects.create(
            title = 'IceCream',
            price = 80,
            inventory = 100
        )
        self.menu2 = Menu.objects.create(
            title = 'Pizza',
            price = 200,
            inventory = 50
        )
        self.valid_payload = {
            'title': 'Test Menu',
            'price': 100,
            'inventory': 200
        }
        self.invalid_payload = {
            'title': '',
            'price': '',
            'inventory': ''
        }

    def login_as_testuser(self):
        self.client.login(username='testuser', password='testpassword')

    def test_view_by_authenticated_user(self):
        response = self.client.get(reverse('menus'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.login_as_testuser()
        response = self.client.get(reverse('menus'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_all_menus(self):
        self.login_as_testuser()
        response = self.client.get(reverse('menus'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_menu(self):
        self.login_as_testuser()
        response = self.client.post(
            reverse('menus'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   