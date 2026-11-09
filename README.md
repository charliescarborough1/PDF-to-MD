# Batch PDF to Markdown Converter

`process_large_pdfs.py` converts PDFs to Markdown using PyMuPDF4LLM. It writes one UTF-8 Markdown file per PDF and can preserve structure such as headings, lists, and tables.

## Setup

Open a terminal in the folder that contains `process_large_pdfs.py`. Create a Python virtual environment and install the dependency.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pymupdf4llm
```

If you already have a virtual environment with PyMuPDF4LLM installed, activate it and continue below.

## Convert PDFs

1. Put your PDF files in `input_pdfs/`. Create the folder if needed.
2. From the folder containing the script, run:

   ```sh
   python process_large_pdfs.py
   ```

3. Open the results in `output_md/`. For example, `input_pdfs/report.pdf` becomes `output_md/report.md`.

Both folders live beside the script, regardless of your terminal's current working directory. The script creates them if they are missing. It looks for `*.pdf` directly inside `input_pdfs/`. Rerunning the script overwrites any Markdown file with the same name.

## Check the results

The terminal shows how many PDFs were found and whether each file was saved or failed. If a file fails, the script prints the error and continues with the next PDF. Check for lines beginning with `✗ Failed`, since the final message says “All files processed successfully!” even if individual conversions failed.
