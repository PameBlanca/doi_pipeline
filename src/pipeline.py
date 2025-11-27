from pathlib import Path

from .config import RAW_TEXT_FILE, PAPERS_INFO_CSV, PAPERS_WITH_TEXT_CSV, PDF_STATUS_CSV
from .utils_io import ensure_dirs
from .extract_dois import build_papers_info_csv
from .semantic_scholar import build_papers_info_with_text
from .pdf_downloaders import download_pdfs_for_all

def run_full_pipeline(
    raw_text_path: Path = RAW_TEXT_FILE,
) -> None:
    ensure_dirs()

    print("1) Extrayendo DOIs…")
    papers_info_csv = build_papers_info_csv(raw_text_path, PAPERS_INFO_CSV)

    print("2) Obteniendo título y abstract desde Semantic Scholar…")
    papers_with_text_csv = build_papers_info_with_text(papers_info_csv, PAPERS_WITH_TEXT_CSV)

    print("3) Descargando PDFs (Semantic Scholar / arXiv / PMC / Unpaywall)…")
    pdf_status_csv = download_pdfs_for_all(papers_with_text_csv, PDF_STATUS_CSV)

    print("\n Pipeline completado:")
    print(f" - DOIs: {papers_info_csv}")
    print(f" - Título + abstract: {papers_with_text_csv}")
    print(f" - PDF status: {pdf_status_csv}")
