from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_url_raiz_direciona_para_view_da_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
