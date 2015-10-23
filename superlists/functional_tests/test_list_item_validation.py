from base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # daniel va a la página de inicio y accidentalmente hizo un submit
        # una lista vacia. le dio un enter a la caja de texto
        self.browser.get(self.server_url)
        self.browser.get_item_input_box().send_keys('\n')

        # la pagina de inicio se refresca, y hay un mensaje de error diciendo
        # la lista no puede estar en blanco
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'No puedes tener una lista de elementos vacia')

        # intenta nuevamente con un texto para el elemento, el cual ahora funciona
        self.browser.find_element_by_id('id_new_item').send_keys('comprar leche\n')
        self.check_for_row_in_list_table('1: comprar leche')

        # perversamente, ella decide agregar una segunda lista de elementos vacios
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # recibe una advertencia similar en la pagina de la lista
        self.check_for_row_in_list_table('1: comprar leche')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'No puedes tener una lista de elementos vacia')

        # y puede corregirlo agregando texto ahí
        self.browser.find_element_by_id('id_new_item').send_keys('hacer tea\n')
        self.check_for_row_in_list_table('1: comprar leche')
        self.check_for_row_in_list_table('2: hacer tea')
