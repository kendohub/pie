import unittest
import user_type as ust

class TestUserType(unittest.TestCase):
  def test_button_available(self):
    actual = ust.button_available("社員")
    self.assertTrue(actual)

    actual = ust.button_available("契約社員")
    self.assertTrue(actual)

    actual = ust.button_available("派遣社員")
    self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
