from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database, auth
from typing import List

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db), current_user=Depends(auth.get_current_user)):
    new_note = models.Note(
        title=note.title,
        content=note.content,
        userId=current_user._id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/", response_model=List[schemas.NoteResponse])
def get_notes(db: Session = Depends(database.get_db), current_user=Depends(auth.get_current_user)):
    return db.query(models.Note).filter(models.Note.userId == current_user._id).all()


@router.put("/{note_id}", response_model=schemas.NoteResponse)
def update_note(note_id: str, updated: schemas.NoteUpdate, db: Session = Depends(database.get_db), current_user=Depends(auth.get_current_user)):
    note = db.query(models.Note).filter(models.Note._id == note_id, models.Note.userId == current_user._id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in updated.dict(exclude_unset=True).items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}")
def delete_note(note_id: str, db: Session = Depends(database.get_db), current_user=Depends(auth.get_current_user)):
    note = db.query(models.Note).filter(models.Note._id == note_id, models.Note.userId == current_user._id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
