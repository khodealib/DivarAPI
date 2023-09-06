from sqlalchemy import Column, DateTime, func


class BaseDBModel():
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
