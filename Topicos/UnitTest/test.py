import unittest
import requests

class TestAPIMethods(unittest.TestCase):

    def test_get(self):       
        req = requests.get('http://localhost:5000/flask/api/cursos/1')        
        self.assertTrue(req.ok)

    def test_delete(self):               
        req = requests.delete('http://localhost:5000/flask/api/cursos/2')              
        self.assertTrue(req.ERRO)

if __name__ == '__main__':
    unittest.main()