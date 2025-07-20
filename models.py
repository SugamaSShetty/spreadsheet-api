# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Spreadsheet table
class Spreadsheet(Base):
    __tablename__ = "spreadsheets"

    id = Column(Integer, primary_key=True, index=True)

# Cell table
class Cell(Base):
    __tablename__ = "cells"

    id = Column(Integer, primary_key=True, index=True)
    spreadsheet_id = Column(Integer, ForeignKey("spreadsheets.id"))
    cell_id = Column(String, index=True)  # e.g., "A1"
    value = Column(String, nullable=True)
    formula_string = Column(String, nullable=True)

    spreadsheet = relationship("Spreadsheet")

# CellDependency table
class CellDependency(Base):
    __tablename__ = "cell_dependencies"

    id = Column(Integer, primary_key=True, index=True)
    spreadsheet_id = Column(Integer)
    from_cell = Column(String)  # Dependent cell (e.g., "C1")
    to_cell = Column(String)    # Precedent cell (e.g., "A1")
