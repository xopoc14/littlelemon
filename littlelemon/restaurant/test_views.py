from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Menu
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='testpass123',
        )
        self.client.login(username='admin', password='testpass123')
        item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        item2 = Menu.objects.create(Title="ApplePie", Price=50, Inventory=20)
        item3 = Menu.objects.create(Title="RootBeer", Price=10, Inventory=50)
        return super().setUp()
    
    def test_detail(self) -> None:
        response = self.client.get('/restaurant/menu/')
        
        expected = '[{"id":2,"Title":"IceCream","Price":"80.00","Inventory":100},{"id":3,"Title":"ApplePie","Price":"50.00","Inventory":20},{"id":4,"Title":"RootBeer","Price":"10.00","Inventory":50}]'
     
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, response.content.decode())