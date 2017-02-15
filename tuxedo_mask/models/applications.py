# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from . import Base


class Applications(Base):

    __tablename__ = 'applications'

    applications_id = Column(Integer, primary_key=True)
    applications_sid = Column()
    name = Column()

    users = relationship('Users')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

