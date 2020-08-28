import markdown as md
import pendulum


class Markdown:
    """Wrapper for the Python `markdown` library to retrofit it for my needs."""

    def __init__(self, markdown: str):
        self._md = md.Markdown(extensions=["fenced_code", "meta"])
        self._html = self._md.convert(markdown)

    def _get_meta(self, key, _type):
        """Returns the meta value for the given `key` casted or parsed to the expected `_type`."""

        value = self._md.Meta.get(key)[0]

        if _type == "string":
            value = str(value)
        elif _type == "datetime":
            value = pendulum.parse(value)

        return value

    @property
    def author(self):
        return self._get_meta("author", "string")

    @property
    def description(self):
        return self._get_meta("description", "string")

    @property
    def html(self):
        return self._html

    @property
    def published(self):
        return self._get_meta("published", "datetime")

    @property
    def title(self):
        return self._get_meta("title", "string")

    @property
    def type(self):
        return self._get_meta("type", "string")
