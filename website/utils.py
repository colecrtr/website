from pathlib import Path


def get_path_key(path: Path, directory: Path, extension: str):
    """
    Returns the OS-independent path key by taking the original path and removing the beginning
    content `directory` parts and the trailing file `extension`
    """

    # Path parts, excluding the `directory`
    parts = path.parts[len(directory.parts) :]

    # Restructured, forward-slash delimited
    path_key = "/".join(parts)

    # Remove the file extension
    if extension:
        path_key = path_key[: (-1 * len(extension))]

    return path_key
