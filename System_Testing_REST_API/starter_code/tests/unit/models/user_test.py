from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    def test_create_user(self):
        """
        Tests that the UserModel correctly hashes the password upon creation
        and can verify it with the check_password() method.
        """
        user = UserModel('test','abcd')

        self.assertEqual(user.username, 'test')
        self.assertNotEqual(user.password, 'abcd')
        self.assertTrue(user.check_password('abcd'))  # Assert that the correct password returns True
        self.assertFalse(user.check_password('1234'))  # Assert that the wrong password returns False


