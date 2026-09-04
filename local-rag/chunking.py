from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Chunk:
    id: str
    source: str
    text: str

def chunk_markdown(path: Path, max_chars: int = 500) -> list[Chunk]:
