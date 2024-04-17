#!/usr/bin/python3
"""Lists states"""

import os
from model_state import Base, State
from sqlalchemy import relationship
from sqlalchemy.ext.deeclarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """class representing the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
            autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)
