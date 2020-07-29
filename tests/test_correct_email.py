from unittest import TestCase
from functions.correct_email import is_correct_email


class CorrectEmailTestCase(TestCase):
    def test1_is_True(self):
        self.assertTrue(is_correct_email("masteraalish@gmail.com"))

    def test2_is_True(self):
        self.assertTrue(is_correct_email("themonrealstudio@gmail.com"))

    def test3_has_double_dog(self):
        self.assertFalse(is_correct_email("themonrea@lstudio@gmail.com"))

    def test4_doesnt_have_name(self):
        self.assertFalse(is_correct_email("@gmail.com"))

    def test5_doesnt_have_dog(self):
        self.assertFalse(is_correct_email("aidana.yahoo.com"))
