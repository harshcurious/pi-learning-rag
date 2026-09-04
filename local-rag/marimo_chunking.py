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

    return


@app.cell
def _(Path):
    Path(".").absolute()
    return


@app.cell
def _():
    from huggingface_hub import snapshot_download
    folder = snapshot_download(repo_id="vibrantlabsai/Sample_Docs_Markdown",
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


app._unparsable_cell(
    r"""
    para = 
    for file in Path("local-rag/doc").glob("*.md"):
        mo.output.append(file.resolve())
        raw_text = file.read_text('utf-8')
        list_para = raw_text.split('\n\n')
        mo.output.append(list_para)
    """,
    name="_"
)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
