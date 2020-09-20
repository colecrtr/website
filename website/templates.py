from __future__ import annotations

from pathlib import Path
from typing import Dict

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template
from jinja2 import select_autoescape

from website.utils import get_path_key


def get_templates(directory: Path) -> Dict[str, Template]:
    if not directory.exists():
        raise FileNotFoundError(directory)
    elif not directory.is_dir():
        raise ValueError(f"{directory} is not a directory")

    extension = ".j2"
    jinja_env = Environment(
        loader=FileSystemLoader(str(directory)),
        autoescape=select_autoescape([extension]),
    )
    templates: Dict[str, Template] = {}

    for path in directory.rglob(f"*{extension}"):
        path_key = get_path_key(path=path, directory=directory, extension=extension)
        templates[path_key] = jinja_env.get_template(str(path.relative_to(directory)))

    return templates
