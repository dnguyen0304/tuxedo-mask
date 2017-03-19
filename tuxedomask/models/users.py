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

    # Should application or applications_id be added as a required parameter?
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        repr_ = '{}(applications_id={}, username="{}", password="*")'
        return repr_.format(self.__class__.__name__,
                            self.applications_id,
                            self.username)

