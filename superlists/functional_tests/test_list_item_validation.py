from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # daniel va a la página de inicio y accidentalmente hizo un submit
        # una lista vacia. le dio un enter a la caja de texto
        self.fail('escribe me')