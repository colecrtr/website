import shutil
from unittest import TestCase

from tests import BASE_TESTS_DIR
from website.build import build


class TestBuild(TestCase):
    """Tests for the `build` function"""

    def setUp(self):
        self.build_dir = BASE_TESTS_DIR / "test_build"
        build(
            templates_dir=BASE_TESTS_DIR / "test_templates",
            content_dir=BASE_TESTS_DIR / "test_content",
            build_dir=self.build_dir,
        )

    def tearDown(self):
        shutil.rmtree(self.build_dir)

    def test_builds_correctly(self):
        self.assertTrue((self.build_dir / "some_other_test/deeper/page.html").exists())
        self.assertTrue((self.build_dir / "index.html").exists())
        self.assertTrue((self.build_dir / "test.html").exists())
