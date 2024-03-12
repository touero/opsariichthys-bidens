from sqlalchemy import Column, String, Text
from .base import Base


class Info(Base):
    __tablename__ = "info"

    school_id = Column(String, primary_key=True, nullable=False)
    name = Column(String, default=None, nullable=True)
    belong = Column(String, default=None, nullable=True)
    province_id = Column(String, default=None, nullable=True)
    province_name = Column(String, default=None, nullable=True)
    site = Column(String, default=None, nullable=True)
    city_name = Column(String, default=None, nullable=True)
    level_name = Column(String, default=None, nullable=True)
    type_name = Column(String, default=None, nullable=True)
    school_type_name = Column(String, default=None, nullable=True)
    school_nature_name = Column(String, default=None, nullable=True)
    dual_class_name = Column(String, default=None, nullable=True)
    nature_name = Column(String, default=None, nullable=True)
    school_site = Column(String, default=None, nullable=True)
    address = Column(String, default=None, nullable=True)
    content = Column(Text, default=None, nullable=True)
