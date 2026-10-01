\# ⚖️ LegalEase



\## AI-Powered Legal Document Generator



LegalEase is an AI-powered legal document generation application that helps users create professional legal document drafts from simple inputs.



Users can select a document type, provide the parties involved, effective date, and important terms. LegalEase uses Google's Gemini API to generate a structured legal document that can be edited and exported as TXT, DOCX, or PDF.



> ⚠️ \*\*Disclaimer:\*\* LegalEase generates AI-assisted document drafts for informational purposes only. Important legal documents should be reviewed by a qualified legal professional before use.



\---



\## ✨ Features



\- 🤖 AI-powered legal document generation

\- 📄 Multiple document types

\- ✏️ Editable generated documents

\- 👀 Formatted document preview

\- 📥 Download as TXT

\- 📥 Download as DOCX

\- 📥 Download as PDF

\- 💰 Unicode support for symbols such as ₹

\- ⚡ FastAPI backend

\- 🎨 Streamlit frontend

\- 🔐 API key stored securely using `.env`

\- 🧪 Automated tests for backend and document exporters



\---



\## 📋 Supported Document Types



LegalEase currently supports document types such as:



\- Employment Contract

\- Lease Agreement

\- Non-Disclosure Agreement (NDA)

\- Agreement

\- Contract

\- Employment Offer Letter



\---



\## 🏗️ Project Architecture



```text

LegalEase/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── routes.py

│   │

│   ├── ai\_core/

│   │   ├── \_\_init\_\_.py

│   │   └── gemini\_generator.py

│   │

│   └── utils/

│       ├── \_\_init\_\_.py

│       └── document\_formatter.py

│

├── tests/

│   └── test\_app.py

│

├── assets/

│   └── arial.ttf

│

├── app.py

├── requirements.txt

├── .env

├── .gitignore

└── README.md

