# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:

    created_at = Column()
    created_by = Column()
    updated_at = Column()
    updated_by = Column()

