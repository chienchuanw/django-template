from django.test import TestCase
from django.urls import reverse


# Test functions must start with the word "test"
class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_reverse_url(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Home")

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_home_page_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "pages/home.html")
