from pathlib import Path
from unittest import TestCase

from website.utils import get_path_key


class TestGetPathKey(TestCase):
    """Tests for the `get_path_key` function"""

    def test_excludes_directory(self):
        directory = Path("hello/world")
        self.assertEqual(
            get_path_key(path=directory / "test", directory=directory, extension=""),
            "test",
        )

    def test_removes_extension(self):
        self.assertEqual(
            get_path_key(path=Path("a/b/c.md"), directory=Path("a/b"), extension=".md"),
            "c",
        )
