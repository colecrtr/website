from unittest import TestCase

from jinja2 import Template

from tests import BASE_TESTS_DIR
from website.templates import get_templates


class TestGetTemplates(TestCase):
    """Tests for the `get_templates` function"""

    def setUp(self):
        self.templates_dir = BASE_TESTS_DIR / "test_templates"

    def test_get_with_nonexistent_directory(self):
        with self.assertRaises(FileNotFoundError):
            get_templates(directory=BASE_TESTS_DIR / "not_real")

    def test_get_with_file_path(self):
        with self.assertRaises(ValueError):
            get_templates(directory=self.templates_dir / "test.j2")

    def test_get_with_existing_directory(self):
        get_templates(directory=self.templates_dir)

    def test_get_maps_templates_correctly(self):
        templates = get_templates(directory=self.templates_dir)
        self.assertIsInstance(templates["deeper/template"], Template)
        self.assertIsInstance(templates["page"], Template)
        self.assertIsInstance(templates["test"], Template)
