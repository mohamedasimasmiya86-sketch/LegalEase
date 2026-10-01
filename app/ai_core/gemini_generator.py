import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class GeminiDocumentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        )

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str
    ) -> str:

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing. "
                "Please add it to the .env file."
            )

        client = genai.Client(api_key=self.api_key)

        prompt = f"""
You are an AI legal document drafting assistant.

Generate a clear, professional draft legal document based on
the information provided below.

Document Type:
{document_type}

Parties:
{parties}

Effective Date:
{effective_date}

Terms:
{terms}

Requirements:
- Use a professional legal-document structure.
- Include an appropriate title.
- Clearly identify the parties.
- Include the effective date.
- Organize important terms into numbered sections.
- Use clear and formal language.
- Do not invent specific personal details that were not provided.
- End with appropriate signature sections.
- Return ONLY the document text.
- Do not use markdown code fences.

Important:
This is an AI-generated draft for informational purposes and
should be reviewed by a qualified legal professional before use.
"""

        response = client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        if not response.text:
            raise ValueError("The AI returned an empty response.")

        return response.text.strip()