# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from . import Base


class Applications(Base):

    __tablename__ = 'applications'

    applications_id = Column(primary_key=True)
    applications_uuid = Column()
    name = Column()

    users = relationship('ApplicationsUsers')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

