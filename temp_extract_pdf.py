import re
from pathlib import Path
import pypdf

pdf_path = Path(r'c:\Users\Andy\dev\spellbook\School\Computer-Science\Notes\CS-530\Week-01\chapter-1.pdf')
out_md = pdf_path.with_suffix('.md')
reader = pypdf.PdfReader(str(pdf_path))
text = '\n\n'.join(page.extract_text() or '' for page in reader.pages)
text = text.replace('\r\n', '\n').replace('\r', '\n')
text = re.sub(r'\n{3,}', '\n\n', text).strip()
if not text:
    raise SystemExit('No text extracted from PDF')
out_md.write_text('# Chapter 1\n\n' + text + '\n', encoding='utf-8')
print(f'Wrote {out_md}')
