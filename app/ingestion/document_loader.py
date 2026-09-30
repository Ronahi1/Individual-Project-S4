import pypdf
from pathlib import Path


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix == ".pdf":
        return _load_pdf(path)
    elif path.suffix == ".txt":
        return _load_txt(path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")


def _load_pdf(path: Path) -> str:
    reader = pypdf.PdfReader(str(path))
    pages = [page.extract_text() for page in reader.pages]
    return "\n".join(pages)


def _load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8")