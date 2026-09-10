import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from dataclasses import dataclass
    from pathlib import Path

    return Path, dataclass


@app.cell
def _(dataclass):
    @dataclass(frozen=True)
    class Chunk:
        id: str
        source: str
        text: str

    return (Chunk,)


@app.cell
def _(Path):
    Path(".").absolute()
    return


@app.cell
def _():
    from huggingface_hub import snapshot_download

    folder = snapshot_download(
        repo_id="vibrantlabsai/Sample_Docs_Markdown",
        repo_type="dataset",
        local_dir="./local-rag/doc",
    )
    print(folder)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `Path.iterdir()` is a _list_ of file/directories inside Path object.
    - `Path.glob()` is a _map_.
        - `map` is a _function_ applied to every item of an _iterable_
    """)
    return


@app.cell
def _(Chunk, Path, mo):
    # all_paras = []
    MAX_CHAR = 512
    # grouped_all_paras = []
    # grouped_all_ids = []
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
    # mo.output.append(len(grouped_all_paras))
    mo.output.append(all_chunks)
    return


@app.cell
def _():
    # all_paras_clean = [para.strip() for para in all_paras]
    # all_paras_clean = [para for para in all_paras if len(para)>0]
    # all_paras_clean
    return


@app.cell
def _():
    # MAX_CHAR = 512
    # grouped_all_paras = []
    # current_para_combo = ""
    # for para in all_paras_clean:
    #     if len(current_para_combo + para) < MAX_CHAR:
    #         current_para_combo += para
    #     else:
    #         grouped_all_paras.append(current_para_combo)
    #         current_para_combo = para
    # grouped_all_paras
    return


@app.cell
def _(grouped_all_paras):
    from uuid import uuid4

    uuids = tuple((uuid4(), para) for i, para in enumerate(grouped_all_paras))
    uuids
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
