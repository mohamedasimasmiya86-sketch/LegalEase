from fastapi.testclient import TestClient

from app.main import app
from app.routes import generator
from app.utils.document_formatter import (
    format_txt,
    format_docx,
    format_pdf,
)


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_generate_document():
    original_method = generator.generate_document

    def fake_generate_document(
        document_type,
        parties,
        terms,
        effective_date
    ):
        return "TEST LEGAL DOCUMENT"

    generator.generate_document = fake_generate_document

    try:
        response = client.post(
            "/generate",
            json={
                "document_type": "Employment Contract",
                "parties": "ABC Technologies and John Doe",
                "terms": "Salary: ₹50,000",
                "effective_date": "2026-10-01",
            },
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["document"] == "TEST LEGAL DOCUMENT"

    finally:
        generator.generate_document = original_method


def test_txt_export():
    result = format_txt("Salary: ₹50,000")
    assert isinstance(result, bytes)
    assert "₹50,000".encode("utf-8") in result


def test_docx_export():
    result = format_docx(
        "Salary: ₹50,000",
        "Employment Contract"
    )
    assert isinstance(result, bytes)
    assert len(result) > 100


def test_pdf_export():
    result = format_pdf(
        "Salary: ₹50,000",
        "Employment Contract"
    )
    assert isinstance(result, bytes)
    assert len(result) > 100