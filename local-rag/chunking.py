from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Chunk:
    id: str
    source: str
    text: str

def chunk_markdown(path: Path, max_chars: int = 512) -> list[Chunk]:
    all_chunks = []
    path_glob_ignore_hidden = [
        f for f in Path("local-rag/doc").glob('**/*.md')
        if not any(part.startswith('.') for part in f.resolve().parts)
    ]
    for file in path_glob_ignore_hidden:
        mo.output.append(file)
        id_idx = 0
        raw_text = file.read_text("utf-8")
        list_para = raw_text.split("\n\n")
        # mo.output.append(list_para)
        # all_paras = all_paras + list_para
        paras_clean = [para.strip() for para in list_para]
        paras_clean = [para for para in paras_clean if len(para) > 0]
        current_para_combo = ""
        for para in paras_clean:
            if len(current_para_combo + para) < MAX_CHAR:
                current_para_combo += para
            else:
                # grouped_all_paras.append(current_para_combo)
                id = f"{file}-{id_idx:05}"
                # grouped_all_ids.append(id)
                chunk = Chunk(id=id, source=file, text=current_para_combo)
                all_chunks.append(chunk)
                current_para_combo = para
                id_idx += 1
        return all_chunks
