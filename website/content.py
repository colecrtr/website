from __future__ import annotations

from pathlib import Path
from typing import Dict

import markdown as md
import pendulum
from jinja2 import Template

from .utils import get_path_key


class Content:
    """A piece of content of this website, written in Markdown"""

    def __init__(self, file_path: Path, templates: Dict[str, Template]):
        self._file_path = file_path
        self._markdown = md.Markdown(extensions=["fenced_code", "meta"])

        with open(str(file_path.resolve())) as file:
            self._html = self._markdown.convert(file.read())

        self._template = templates[self.get_meta("template", "string")]

    def get_meta(self, key, _type):
        """Returns the meta value for the given `key` casted or parsed to the expected `_type`."""

        value = self._markdown.Meta.get(key)[0]

        if _type == "string":
            value = str(value)
        elif _type == "datetime":
            value = pendulum.parse(value)

        return value

    @property
    def author(self) -> str:
        return self.get_meta("author", "string")

    @property
    def description(self) -> str:
        return self.get_meta("description", "string")

    @property
    def html(self) -> str:
        return self._html

    @property
    def published(self) -> pendulum.DateTime:
        return self.get_meta("published", "datetime")

    @property
    def template(self) -> Template:
        return self._template

    @property
    def title(self) -> str:
        return self.get_meta("title", "string")

    @classmethod
    def get(cls, directory: Path, templates: Dict[str, Template]) -> Dict[str, Content]:
        if not directory.exists():
            raise FileNotFoundError(directory)
        elif not directory.is_dir():
            raise ValueError(f"{directory} is not a directory")

        extension = ".md"
        content: Dict[str, Content] = {}

        for path in directory.rglob(f"*{extension}"):
            path_key = get_path_key(path=path, directory=directory, extension=extension)
            content[path_key] = Content(file_path=path, templates=templates)

        return content
