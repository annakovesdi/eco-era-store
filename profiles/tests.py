from django.test import TestCase


class TestProfileViews(TestCase):
    # profile page only on log in displaying past orders
    def test_get_profile_page(self):

    # only superuser can succesfully add products
    def test_add_product_page(self):

     # only superuser can succesfully edit products
    def test_edit_product_page(self):

     # only superuser can succesfully delete products
    def test_delete_product_page(self):