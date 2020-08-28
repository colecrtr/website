from pathlib import Path
from unittest import TestCase

import faker

from tests import BASE_TESTS_DIR
from website.content import Content


fake = faker.Faker()


class TestContent(TestCase):
    """Tests for the `Content` class."""

    def setUp(self):
        self.content = Content(str(BASE_TESTS_DIR / "test_content"))

    def test_get_path_key_static_method_with_shallow_path(self):
        path = Path("a/b/c/d.md")
        directory = Path("a/b/c")
        extension = ".md"
        expected = "/d"

        self.assertEqual(Content.get_path_key(path, directory, extension), expected)

    def test_get_path_key_static_method_with_deep_path(self):
        path = Path("a/b/c/d/e/f/g/h/i/j/k/l/m.md")
        directory = Path("a/b")
        extension = ".md"
        expected = "/c/d/e/f/g/h/i/j/k/l/m"

        self.assertEqual(Content.get_path_key(path, directory, extension), expected)

    def test_non_existent_content_directory(self):
        non_existent_path = str(BASE_TESTS_DIR / fake.word() / fake.word())
        with self.assertRaisesRegex(FileNotFoundError, non_existent_path):
            Content(non_existent_path)

    def test_file_path(self):
        file_path = str(BASE_TESTS_DIR / "test_content" / "test.md")
        with self.assertRaisesRegex(ValueError, r"is not a directory"):
            Content(file_path)
