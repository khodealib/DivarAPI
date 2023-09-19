from sqlalchemy import Column, String, BigInteger, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.base import TimestampMixin


class Advertisement(Base, TimestampMixin):
    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(length=127))
    description = Column(String, nullable=True)
    price = Column(BigInteger, default=0)
    user = relationship("User", back_populates="advertisements")

    images = relationship("AdvertisementImage", back_populates="advertisement")
    attributes = relationship("Attribute",
                              secondary="advertisement_attributes",
                              back_populates="advertisements")
    # TODO location
    # TODO category


class AdvertisementImage(Base, TimestampMixin):
    __tablename__ = "advertisement_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    file_path = Column(String)
    advertisement_id = Column(Integer, ForeignKey("advertisements.id"))
    advertisement = relationship("Advertisement", back_populates="images")


class Attribute(Base, TimestampMixin):
    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    advertisements = relationship("Advertisement",
                                  secondary="advertisement_attributes",
                                  back_populates="attributes")


class AdvertisementAttribute(Base, TimestampMixin):
    __tablename__ = "advertisement_attributes"

    advertisement_id = Column(
        Integer, ForeignKey("advertisements.id"),
        primary_key=True
    )
    attribute_id = Column(
        Integer, ForeignKey("attributes.id"),
        primary_key=True
    )
    value = Column(String, nullable=False)
