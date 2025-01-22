from django.test import TestCase
from restaurant.models import MenuItem, Menu



class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        self.assertEqual(MenuItem.objects.count(), 1)
        self.assertEqual(MenuItem.objects.get().title, "IceCream")
        self.assertEqual(MenuItem.objects.get().price, 80)

    def test_get_item_price(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(MenuItem.objects.count(), 1)

    def test_create_menu_item(self) -> None:
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().title, "IceCream")
        self.assertEqual(Menu.objects.get().price, 80)
        self.assertEqual(Menu.objects.get().inventory, 100)

    def test_delete_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)