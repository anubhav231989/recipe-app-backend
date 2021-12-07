from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserModelTestCase(TestCase):
    '''
    TEST CASES: Custom User Model.
    '''

    def test_user_created_via_email(self):
        '''
            TEST CASE: USER WITH EMAIL IS CREATED SUCCESSFULLY.
        '''

        UserModel = get_user_model()
        email = "anubhav.sidhu@google.com"
        password = "anubhav123"

        user = UserModel.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        '''
            TEST CASE: NORMALIZED USER EMAIL IS SAVED.
        '''

        UserModel = get_user_model()
        email = "anubhav.sidhu@GOOGLE.COM"

        user = UserModel.objects.create_user(
            email=email,
            password="abcd123"
        )

        self.assertEqual(user.email, email.lower())

    def test_empty_email_user_not_created(self):
        '''
        TEST CASE: USER IS NOT CREATED WITH EMPTY EMAIL.
        '''

        with self.assertRaises(ValueError):
            UserModel = get_user_model()
            UserModel.objects.create_user(email=None, password='abcd123')

    def test_superuser_creation(self):
        '''
            TEST CASE: SUPERUSER IS CREATED SUCCESSFULLY.
        '''

        UserModel = get_user_model()
        email = 'anubhav.sidhu@google.com'
        user = UserModel.objects.create_superuser(email=email, password='abcd123')

        self.assertTrue(user.is_superuser)