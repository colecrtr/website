from pathlib import Path

from .markdown import Markdown


class Content(dict):
    """In-memory content management"""

    @staticmethod
    def get_path_key(path: Path, directory: Path, extension: str):
        """
        Returns the OS-independent path key by taking the original path and removing the beginning
        content `directory` parts and the trailing file `extension`
        """

        # Path parts, excluding the content directory
        parts = path.parts[len(directory.parts) :]

        # Restructured, forward-slash delimited
        restructured = "/" + "/".join(parts)

        # Remove the file extension.
        path_key = restructured[: (-1 * len(extension))]

        return path_key

    def __init__(self, directory: str):
        extension = ".md"
        directory = Path(directory)

        if not directory.exists():
            raise FileNotFoundError(directory)
        if not directory.is_dir():
            raise ValueError(f"`{directory}` is not a directory")

        for content_path in directory.rglob(f"*{extension}"):
            key = Content.get_path_key(content_path, directory, extension)
            with open(str(content_path.resolve())) as content_file:
                self[key] = Markdown(content_file.read()).html
