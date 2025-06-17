import unittest
from src.model_loader import load_obj, Model

class TestModelLoader(unittest.TestCase):
    def test_load_cube(self):
        model = load_obj('tests/data/cube.obj')
        self.assertIsInstance(model, Model)
        self.assertEqual(len(model.vertices), 8)
        # Cube has 12 triangles after triangulation
        self.assertEqual(len(model.faces), 12)

if __name__ == '__main__':
    unittest.main()
