from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from app.schemas import DocumentsResponse
from app.services.assistant_service import list_documents
from app.services.document_service import upload_document, remove_document

router = APIRouter(prefix="/documents", tags=["Document Management"])


@router.post("/upload")
def upload(file: UploadFile = File(...), category: str = Form(...)):
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
    docs = list_documents()
    return DocumentsResponse(documents=docs, total=len(docs))


@router.delete("/{doc_id}")
def delete(doc_id: str):
    try:
        result = remove_document(doc_id)
        return {"success": True, **result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Delete failed: {e}")