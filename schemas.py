# schemas.py

from pydantic import BaseModel
from typing import Optional, List

# Base schema for a cell (includes cell_id)
class CellBase(BaseModel):
    cell_id: str

# Schema for setting a value (e.g., A1 = "42")
class CellValue(CellBase):
    value: str

# Schema for setting a formula (e.g., B1 = "=A1+5")
class CellFormula(CellBase):
    formula_string: str

# Schema for responding with full cell info
class CellResponse(CellBase):
    value: Optional[str] = None
    formula_string: Optional[str] = None

# Schema to return dependencies of a cell
class DependencyResponse(BaseModel):
    cell_id: str
    formula_string: str
    dependencies_identified: List[str]
