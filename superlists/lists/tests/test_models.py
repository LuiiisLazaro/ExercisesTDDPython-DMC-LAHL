from lists.models import Item, List
from django.test import TestCase


# Create your tests here.
class ListAndItemsModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'La primera Lista de Elementos'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'El segundo Elemento'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text,
                         'La primera Lista de Elementos'
                         )
        self.assertEqual(first_saved_item.text,
                         'La primera Lista de Elementos'
                         )
        self.assertEqual(second_saved_item.text,
                         'El segundo Elemento'
                         )
        self.assertEqual(second_saved_item.text,
                         'El segundo Elemento'
                         )
