from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class CoreUserAdmin(TestCase):
    '''
        TEST CASES: CUSTOM CORE USER ADMIN.
    '''

    def setUp(self):
        self.client = Client()
        UserModel = get_user_model()
        self.admin_user = UserModel.objects.create_superuser(
            email="admin@google.com",
            password="admin123"
        )

        self.client.force_login(self.admin_user)
        self.user = UserModel.objects.create_user(
            email="anubhav@google.com",
            password="anubhav@123",
            name="Anubhav Sidhu"
        )


    def test_admin_users_listing(self):
        '''
            TEST CASE: TESTS USERS LISTING IS WORKING WITH CUSTOM USER MODEL.
        '''
        user_listing_url = reverse("admin:core_user_changelist")
        response = self.client.get(user_listing_url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_admin_user_change_page(self):
        '''
            TEST CASE: CUSTOM USER MODEL CHANGE PAGE WORKS PROPERLY.
        '''
        user_change_url = reverse("admin:core_user_change", args=[self.user.id])
        response = self.client.get(user_change_url)

        self.assertEqual(response.status_code, 200)

    def test_admin_user_add_page(self):
        '''
            TEST CASE: CUSTOM USER MODEL ADDS USER PROPERLY.
        '''
        user_add_url = reverse("admin:core_user_add")
        response = self.client.get(user_add_url)

        self.assertEqual(response.status_code, 200)
