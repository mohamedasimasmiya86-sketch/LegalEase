import html
from datetime import date

import requests
import streamlit as st

from app.utils.document_formatter import (
    format_docx,
    format_pdf,
    format_txt,
)


BACKEND_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


# ---------- Header ----------

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write(
    "Create professional legal document drafts using AI, "
    "edit them, and export them in multiple formats."
)

st.info(
    "AI-generated drafts are for informational purposes only. "
    "Please have important legal documents reviewed by a qualified "
    "legal professional before use."
)


# ---------- Input Section ----------

st.markdown("## Create Your Document")

col1, col2 = st.columns(2)

with col1:
    document_type = st.selectbox(
        "Document Type",
        [
            "Employment Contract",
            "Lease Agreement",
            "Non-Disclosure Agreement (NDA)",
            "Agreement",
            "Contract",
            "Employment Offer Letter"
        ]
    )

    parties = st.text_input(
        "Parties",
        placeholder="Example: ABC Technologies Pvt. Ltd. and John Doe"
    )

with col2:
    effective_date = st.date_input(
        "Effective Date",
        value=date.today()
    )

    terms = st.text_area(
        "Terms",
        placeholder=(
            "Example: Salary: ₹50,000 per month; "
            "Duration: 1 year; Notice Period: 30 days"
        ),
        height=120
    )


# ---------- Generate ----------

if st.button("✨ Generate Document", use_container_width=True):

    if not parties.strip():
        st.warning("Please enter the parties involved.")

    elif not terms.strip():
        st.warning("Please enter the document terms.")

    else:
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "effective_date": effective_date.isoformat()
        }

        try:
            with st.spinner("Generating your legal document..."):

                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json=payload,
                    timeout=120
                )

            if response.status_code == 200:

                result = response.json()

                if result.get("success"):

                    st.session_state.document_text = result["document"]

                    st.success("Document generated successfully! 🎉")

                else:
                    st.error("The document could not be generated.")

            else:
                error = response.json().get(
                    "detail",
                    "Unknown backend error."
                )

                st.error(f"Backend error: {error}")

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the LegalEase backend. "
                "Make sure the FastAPI server is running."
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")


# ---------- Document Preview / Editing ----------

if "document_text" in st.session_state:

    st.markdown("---")
    st.markdown("## 📄 Generated Document")

    st.session_state.document_text = st.text_area(
        "Edit your document",
        value=st.session_state.document_text,
        height=500
    )

    st.markdown("### Preview")

    safe_text = html.escape(st.session_state.document_text)
    safe_text = safe_text.replace("\n", "<br>")

    st.markdown(
        f"""
        <div style="
            padding: 30px;
            border: 1px solid #ddd;
            border-radius: 12px;
            background-color: #ffffff;
            color: #222;
            line-height: 1.7;
        ">
            {safe_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Downloads ----------

    st.markdown("### Download Document")

    download_col1, download_col2, download_col3 = st.columns(3)

    document_text = st.session_state.document_text

    with download_col1:
        st.download_button(
            "⬇️ Download TXT",
            data=format_txt(document_text),
            file_name="LegalEase_Document.txt",
            mime="text/plain",
            use_container_width=True
        )

    with download_col2:
        st.download_button(
            "⬇️ Download DOCX",
            data=format_docx(
                document_text,
                document_type
            ),
            file_name="LegalEase_Document.docx",
            mime=(
                "application/vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            ),
            use_container_width=True
        )

    with download_col3:
        st.download_button(
            "⬇️ Download PDF",
            data=format_pdf(
                document_text,
                document_type
            ),
            file_name="LegalEase_Document.pdf",
            mime="application/pdf",
            use_container_width=True
        )