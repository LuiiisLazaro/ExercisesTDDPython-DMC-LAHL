from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
	#browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    
    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        #Daniel ha escuchado acerca de una nueva aplicación genial en línea "to-do app"
        #Él va ha checar esta página.
        self.browser.get('http://localhost:8000')

	#Él ve el titulo de la página y el encabezado mencinando "To-Do lists"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #self.fail("Finalizar la Prueba!!! :D")

	#Él es invitado a ingresar un item directamente a "To-Do list"
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Ingresa un Elemento a To-Do'
        )

	#El escribe "comprar plumas de pavo" dentro de la caja de texto, El hobby de Daniel es hacer señuelos para pesca.
        inputbox.send_keys('comprar plumas de pavo')

	#Cuando el da enter, la página se actualiza y ahora la lista de la página contiene un item
	#llamado "1: comprar plumas de pavo real".
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: comprar plumas de pavo")
        self.check_for_row_in_list_table("1: usar las plumas de pavo")
        #import time
        #time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: comprar plumas de pavo', [row.text for row in rows])
        self.assertIn('2: usar las plimas de pavo', [row.text for row in rows])
	#todavia hay una caja de texto invitandole a agregar otro item. el 
	# ingresa "usar plumas y pavo para hacer señuelo de pesca"
        self.fail('Prueba Finalizada :D ')

	#la página se actualiza nuevamente y nos muestra dos elementos en la lista.

	#Daniel se pregunta si el sitio recordará su lista. Entonces se percata que el sitio 
	#ha generado una unica URL para el, --- hay alguna explicación para ese efecto.

	#El visita esa URl --- su lista "To-Do" todavia se encuentra ahí

	#satisfecho, el va a dormir.

if __name__=='__main__':
    unittest.main(warnings='ignore')
browser.quit()

