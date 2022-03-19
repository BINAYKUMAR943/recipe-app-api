from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):


    def setUp(self):
        """This method is generally used to do some setup before running the testcases. This method run first and before all the test cases"""
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(email="binay943@gmail.com",password="password123")
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(email="binay123@gmail.com",password="password123",name='Binay_user')
        """reverse is the method to get the url from the name.SO when you change url you just need to change
        once and not everywhere. So url are generally written on urls.py and can be called using reverse method"""




    def test_users_listed(self):
        """Test user is listed or not"""
        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)
        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)

    def test_user_page_change(self):
        """Test that the user change page works"""

        """ url would be /admin/core/user/1"""
        url=reverse('admin:core_user_change',args=[self.user.id])
        res=self.client.get(url)
        self.assertEqual(res.status_code,200)


    def test_create_user_page(self):
        "This Function test that create user is working fine"

        url=reverse('admin:core_user_add')
        res=self.client.get(url)
        self.assertEqual(res.status_code,200)
        
