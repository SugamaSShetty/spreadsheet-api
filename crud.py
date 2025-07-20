# crud.py

from sqlalchemy.orm import Session
import models, schemas

# Function to insert/update a cell value
def set_cell_value(db: Session, spreadsheet_id: int, cell_data: schemas.CellValue):
    # Check if cell already exists in the DB
    db_cell = db.query(models.Cell).filter(
        models.Cell.spreadsheet_id == spreadsheet_id,
        models.Cell.cell_id == cell_data.cell_id
    ).first()

    # Update value if it exists, otherwise create a new entry
    if db_cell:
        db_cell.value = cell_data.value
        db_cell.formula_string = None  # Clear any existing formula
    else:
        db_cell = models.Cell(
            spreadsheet_id=spreadsheet_id,
            cell_id=cell_data.cell_id,
            value=cell_data.value
        )
        db.add(db_cell)

    db.commit()
    db.refresh(db_cell)
    return db_cell
