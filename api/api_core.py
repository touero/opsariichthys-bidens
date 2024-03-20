from dataclasses import dataclass

from sqlalchemy import func, select, and_
from database.model import Info


@dataclass
class ApiCore:
    province = select(Info.province_name, func.count()).group_by(Info.province_name).order_by(
        func.count().desc()).limit(10)
    dual_class = select(Info.province_name, func.count()).where(Info.dual_class_name == "双一流").group_by(
        Info.province_name).order_by(func.count().desc())
    type_ = select(Info.type_name, func.count()).group_by(Info.type_name).order_by(func.count().desc())

