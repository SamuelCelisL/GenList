import unittest
from unittest.mock import patch, MagicMock
from src.components import conexcionBD


class TestFuncionesBaseDeDatos(unittest.TestCase):

    @patch('src.components.conexcionBD.sqlite3.connect')
    def test_validar_credenciales_profesor(self, mock_connect):
        mock_conexion = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conexion
        mock_conexion.cursor.return_value = mock_cursor

        # Simulamos que existe el documento del profesor y que la contraseña es válida
        mock_cursor.fetchone.side_effect = [(1,), (1,)]

        resultado = conexcionBD.validar_credenciales_profesor(
            '123456', 'password123')
        self.assertTrue(resultado)

        # Simulamos que no existe el documento del profesor
        mock_cursor.fetchone.side_effect = [(0,), (0,)]
        resultado = conexcionBD.validar_credenciales_profesor(
            '654321', 'password123')
        self.assertFalse(resultado)

    @patch('src.components.conexcionBD.sqlite3.connect')
    def test_obtener_id_profesor(self, mock_connect):
        mock_conexion = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conexion
        mock_conexion.cursor.return_value = mock_cursor

        # Simulamos que se encuentra el ID del profesor
        mock_cursor.fetchone.return_value = (10,)
        resultado = conexcionBD.obtener_id_profesor('123456')
        self.assertEqual(resultado, 10)

        # Simulamos que no se encuentra el ID del profesor
        mock_cursor.fetchone.return_value = None
        resultado = conexcionBD.obtener_id_profesor('654321')
        self.assertIsNone(resultado)

    @patch('src.components.conexcionBD.sqlite3.connect')
    def test_obtener_nombre_profesor(self, mock_connect):
        mock_conexion = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conexion
        mock_conexion.cursor.return_value = mock_cursor

        # Simulamos que se encuentra el nombre del profesor
        mock_cursor.fetchone.return_value = ('Juan Pérez',)
        resultado = conexcionBD.obtener_nombre_profesor(10)
        self.assertEqual(resultado, 'Juan Pérez')

        # Simulamos que no se encuentra el nombre del profesor
        mock_cursor.fetchone.return_value = None
        resultado = conexcionBD.obtener_nombre_profesor(20)
        self.assertIsNone(resultado)


if __name__ == '__main__':
    unittest.main()
