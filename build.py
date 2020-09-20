from pathlib import Path

from website.build import build


if __name__ == "__main__":
    build(  # pragma: no cover
        templates_dir=Path("website/templates"),
        content_dir=Path("website/content"),
        build_dir=Path("./build"),
    )
