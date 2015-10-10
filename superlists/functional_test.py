from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
	#browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
	
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Daniel ha escuchado acerca de una nueva aplicación genial en línea "to-do app"
        #Él va ha checar esta página.
        self.browser.get('http://localhost:8000')

	#Él ve el titulo de la página y el encabezado mencinando "To-Do lists"
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finalizar la Prueba!!! :D")

	#Él es invitado a ingresar un item directamente a "To-Do list"

	#El escribe "comprar plumas de pavo" dentro de la caja de texto, El hobby de Daniel es hacer señuelos para pesca.

	#Cuando el da enter, la página se actualiza y ahora la lista de la página contiene un item
	#llamado "1: comprar plumas de pavo real".

	#todavia hay una caja de texto invitandole a agregar otro item. el 
	# ingresa "usar plumas y pavo para hacer señuelo de pesca"

	#la página se actualiza nuevamente y nos muestra dos elementos en la lista.

	#Daniel se pregunta si el sitio recordará su lista. Entonces se percata que el sitio 
	#ha generado una unica URL para el, --- hay alguna explicación para ese efecto.

	#El visita esa URl --- su lista "To-Do" todavia se encuentra ahí

	#satisfecho, el va a dormir.

if __name__=='__main__':
    unittest.main(warnings='ignore')
browser.quit()

