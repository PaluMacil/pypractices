from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from base import Base
if TYPE_CHECKING:
    from company import Company
    from address import Address


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    company_id = Column(Integer, ForeignKey('company.id'))
    company: 'Company' = relationship('Company', back_populates='employees')

    addresses: list['Address'] = relationship('Address', back_populates='employee', cascade='all, delete-orphan')
