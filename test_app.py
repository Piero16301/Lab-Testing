import unittest

from app import CalculaGanador


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = CalculaGanador()

    def test_leerDatos(self):
        expected_data = [
            ['Ancash', 'Asuncion', 'Chacas', '81122156', 'Eddie Hinesley', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '20398144', 'Paula Daigle', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '33656332', 'Aundrea Grace', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '46615862', 'Robert Redmond', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '62329211', 'Aundrea Grace', '0']
        ]
        # read test.csv of local directory and convert it to FileStorage object
        with open('test.csv', 'rb') as f:
            read_data = self.app.leerDatos(f)
            self.assertEqual(read_data, expected_data)

    def test_contarVotos(self):
        expected_votos = {
            'Eddie Hinesley': 1,
            'Paula Daigle': 1,
            'Aundrea Grace': 1,
            'Robert Redmond': 1,
        }
        expected_total = 4
        data = [
            ['Ancash', 'Asuncion', 'Chacas', '81122156', 'Eddie Hinesley', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '20398144', 'Paula Daigle', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '33656332', 'Aundrea Grace', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '46615862', 'Robert Redmond', '1'],
            ['Ancash', 'Asuncion', 'Chacas', '62329211', 'Aundrea Grace', '0']
        ]
        votos, total = self.app.contarVotos(data)
        self.assertEqual(votos, expected_votos)
        self.assertEqual(total, expected_total)

    def test_calcularGanador(self):
        expected_ganador = [{'name': 'Aundrea Grace', 'votes': 5}]
        votos = {
            'Eddie Hinesley': 1,
            'Paula Daigle': 1,
            'Aundrea Grace': 5,
            'Robert Redmond': 1,
        }
        total = 8
        ganador = self.app.calcularGanador(votos, total)
        self.assertEqual(ganador, expected_ganador)
