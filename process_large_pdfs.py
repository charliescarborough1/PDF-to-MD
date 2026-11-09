from pathlib import Path
import pymupdf4llm

base_dir = Path(__file__).resolve().parent
input_dir = base_dir / "input_pdfs"
output_dir = base_dir / "output_md"
input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

pdf_files = list(input_dir.glob("*.pdf"))
print(f"Found {len(pdf_files)} PDF(s) to process.\n")

for pdf_path in pdf_files:
    print(f"Converting: {pdf_path.name}...")
    try:
        # Converts directly to structured markdown (headers, tables, lists)
        md_text = pymupdf4llm.to_markdown(str(pdf_path))
        
        out_file = output_dir / f"{pdf_path.stem}.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        print(f"✓ Saved: {out_file.name}\n")
    except Exception as e:
        print(f"✗ Failed {pdf_path.name}: {e}\n")

print("All files processed successfully!")