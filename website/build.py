from pathlib import Path

from website.content import Content
from website.templates import get_templates


def build(templates_dir: Path, content_dir: Path, build_dir: Path) -> None:
    templates = get_templates(directory=templates_dir)
    all_content = Content.get(directory=content_dir, templates=templates)

    for _path, content in all_content.items():
        path = build_dir / f"{_path}.html"
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w") as file:
            file.write(
                content.template.render(all_content=all_content, content=content)
            )
