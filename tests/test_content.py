from unittest import TestCase

import pendulum

from tests import BASE_TESTS_DIR
from website.content import Content
from website.templates import get_templates


class TestContent(TestCase):
    """Tests for the `Content` class"""

    def setUp(self):
        self.content_dir = BASE_TESTS_DIR / "test_content"
        self.templates = get_templates(BASE_TESTS_DIR / "test_templates")
        self.content = Content(self.content_dir / "test.md", templates=self.templates)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            Content(self.content_dir / "blah.md", templates=self.templates)

    def test_existing_file(self):
        Content(self.content_dir / "test.md", templates=self.templates)

    def test_author(self):
        self.assertEqual(self.content.author, "Cole Carter")

    def test_description(self):
        self.assertEqual(self.content.description, "Test description")

    def test_html(self):
        self.assertIn(
            "<p>Example content should be placed here.</p>", self.content.html
        )

    def test_published(self):
        self.assertEqual(self.content.published, pendulum.datetime(2020, 1, 1))

    def test_template(self):
        self.assertEqual(self.content.template, self.templates["test"])

    def test_title(self):
        self.assertEqual(self.content.title, "Test Title")

    def test_get_with_nonexistent_directory(self):
        with self.assertRaises(FileNotFoundError):
            Content.get(BASE_TESTS_DIR / "not_real", templates=self.templates)

    def test_get_with_file_path(self):
        with self.assertRaises(ValueError):
            Content.get(self.content_dir / "test.md", templates=self.templates)

    def test_get_with_existing_directory(self):
        Content.get(self.content_dir, templates=self.templates)

    def test_get_maps_content_correctly(self):
        content = Content.get(self.content_dir, templates=self.templates)
        self.assertEqual(content["some_other_test/deeper/page"].title, "My page title")
        self.assertEqual(content["index"].title, "Test INDEX Title")
        self.assertEqual(content["test"].title, "Test Title")
