from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from base import Base
if TYPE_CHECKING:
    from employee import Employee


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee: 'Employee' = relationship('Employee', back_populates='addresses')
