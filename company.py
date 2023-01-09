from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from base import Base
if TYPE_CHECKING:
    from employee import Employee


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    employees: list['Employee'] = relationship('Employee', back_populates='company', cascade='all, delete-orphan')
