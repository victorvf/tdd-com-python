from django.test import TestCase


class HomePageTest(TestCase):
    """
    Primeiros testes:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")

        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.strip().endswith("</html>"))
    """

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")
