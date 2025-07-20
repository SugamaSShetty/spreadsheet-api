from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Dict

# Create FastAPI instance
app = FastAPI(
    title="Spreadsheet API",
    description="A simple spreadsheet-like API to read and update cell values.",
    version="1.0.0"
)

# In-memory spreadsheet data
spreadsheet: Dict[str, str] = {
    "A1": "Welcome",
    "B1": "to",
    "C1": "FastAPI"
}

# Request model for updating cell
class CellUpdate(BaseModel):
    value: str

# GET endpoint to read cell value
@app.get("/cells/{cell_id}", summary="Read a cell", tags=["Cells"])
def read_cell(cell_id: str = Path(..., description="The ID of the cell to retrieve (e.g., A1)")):
    value = spreadsheet.get(cell_id)
    if value is None:
        return {"cell_id": cell_id, "value": "Cell not found"}
    return {"cell_id": cell_id, "value": value}

# POST endpoint to update cell value
@app.post("/cells/{cell_id}", summary="Update a cell", tags=["Cells"])
def update_cell(cell_id: str, update: CellUpdate):
    spreadsheet[cell_id] = update.value
    return {
        "message": f"Cell {cell_id} updated successfully.",
        "cell_id": cell_id,
        "new_value": update.value
    }
