import unittest
import app

class TestApp(unittest.TestCase):
    def test_allowed_in_club_true(self):
        pug = app.Human('Just a pug on the internet', 'Pugger', 26)
        self.assertTrue(pug.allowed_in_the_club())

    def test_allowed_in_club_false(self):
        pug = app.Human('Just a pug on the internet', 'Pugger', 15)
        self.assertFalse(pug.allowed_in_the_club())  


if __name__== '__main__':
    unittest.main()