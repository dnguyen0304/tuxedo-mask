# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer

from . import Base


class Users(Base):

    __tablename__ = 'users'

    users_id = Column(Integer, primary_key=True)
    users_sid = Column()
    applications_id = Column(ForeignKey('applications.applications_id'))
    username = Column()
    password = Column()

    def __init__(self, applications_id, username, password):
        self.applications_id = applications_id
        self.username = username
        self.password = password

    def __repr__(self):
        repr_ = '{}(applications_id={}, username="{}", password="*")'
        return repr_.format(self.__class__.__name__,
                            self.applications_id,
                            self.username)

