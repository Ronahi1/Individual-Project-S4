from app.ingestion.document_loader import load_document

text = load_document("app/data/eu_regulation_261_2004.pdf")
print(text[:500])
