from sqlalchemy import func, select, and_
from database.model import Info


def province():
    return select(Info.province_name, func.count()).group_by(Info.province_name).order_by(
        func.count().desc()).limit(10)


def dual_class():
    return select(Info.province_name, func.count()).where(Info.dual_class_name == "双一流").group_by(
        Info.province_name).order_by(func.count().desc())

def type_():
    return