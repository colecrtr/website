from unittest import TestCase

import faker
import pytz

from website.markdown import Markdown


fake = faker.Faker()


class TestMarkdown(TestCase):
    """Tests for the `Markdown` class."""

    def setUp(self):
        self.expected_meta = {
            "author": fake.name(),
            "description": fake.sentence(),
            "published": fake.date_time(tzinfo=pytz.UTC),
            "title": fake.sentence(),
            "type": fake.random_element(elements=["post"]),
        }
        expected_meta_str = "\n".join(
            [f"{key}: {value}" for key, value in self.expected_meta.items()]
        )

        self.markdown = Markdown(
            "\n".join(
                ["---", expected_meta_str, "---", "# Header1", "## Header2", "", "Body"]
            )
        )

    def test__get_meta_method(self):
        """Expected to return the meta value for the given `key` in the given `_type`."""

        types = {
            "string": ["author", "title", "type"],
            "datetime": ["published"],
        }

        for _type, fields_of_type in types.items():
            random_field_of_type = fake.random_element(elements=fields_of_type)
            with self.subTest(_type=_type, random_field_of_type=random_field_of_type):
                self.assertEqual(
                    self.expected_meta[random_field_of_type],
                    self.markdown._get_meta(random_field_of_type, _type),
                )

    def test_author_property(self):
        """Expected to evaluate to the inputted `author` meta value."""

        self.assertEqual(self.expected_meta["author"], self.markdown.author)

    def test_description_property(self):
        """Expected to evaluate to the inputted `description` meta value."""

        self.assertEqual(self.expected_meta["description"], self.markdown.description)

    def test_html_property(self):
        """Expected to evaluate to the converted version of the inputted markdown string."""

        self.assertIn("<h1>Header1</h1>", self.markdown.html)
        self.assertIn("<h2>Header2</h2>", self.markdown.html)
        self.assertIn("<p>Body</p>", self.markdown.html)

    def test_published_property(self):
        """Expected to evaluate to the inputted `published` meta value."""

        self.assertEqual(self.expected_meta["published"], self.markdown.published)

    def test_title_property(self):
        """Expected to evaluate to the inputted `title` meta value."""

        self.assertEqual(self.expected_meta["title"], self.markdown.title)

    def test_type_property(self):
        """Expected to evaluate to the inputted `type` meta value."""

        self.assertEqual(self.expected_meta["type"], self.markdown.type)
