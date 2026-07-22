from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends
from app.schemas import DocumentsResponse
from app.services.assistant_service import list_documents
from app.services.document_service import upload_document, remove_document
from app.dependencies import get_current_user
from app.models import User

router = APIRouter(prefix="/documents", tags=["Document Management"])


@router.post("/upload")
def upload(
    file: UploadFile = File(...),
    category: str = Form(...),
    current_user: User = Depends(get_current_user)
):
    """Upload a new document, save it to disk and index it into the vector database. Requires authentication."""
    try:
        content_bytes = file.file.read()
        content = content_bytes.decode("utf-8")
        result = upload_document(filename=file.filename, content=content, category=category)
        return {"success": True, "document": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {e}")


@router.get("", response_model=DocumentsResponse)
def get_documents():
    """List all indexed documents. Public endpoint, mirrors GET /assistant/documents."""
    docs = list_documents()
    return DocumentsResponse(documents=docs, total=len(docs))


@router.delete("/{doc_id}")
def delete(doc_id: str, current_user: User = Depends(get_current_user)):
    """Delete a document from the knowledge base and vector database. Requires authentication."""
    try:
        result = remove_document(doc_id)
        return {"success": True, **result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Delete failed: {e}")