from dataclasses import dataclass

from sqlalchemy import func, select, and_

from .constants_api import API
from database.model import Info, Major, Score


@dataclass
class ApiCore:
    province = select(Info.province_name, func.count()).group_by(Info.province_name).order_by(
        func.count().desc()).limit(10)

    dual_class = select(Info.province_name, func.count()).where(Info.dual_class_name == "双一流").group_by(
        Info.province_name).order_by(func.count().desc())

    type_ = select(Info.type_name, func.count()).group_by(Info.type_name).order_by(func.count().desc())

    major = select(Major.special_name, func.count()).group_by(Major.special_name).order_by(
        func.count().desc()).limit(10)

    admissions = select(Score.province_id, func.count()).group_by(Score.province_id).order_by(
        func.count().desc())

    big_data = select(Major.special_name, func.count()).where(Major.special_name.like("%数据%")).group_by(
        Major.special_name).order_by(func.count().desc()).limit(10)

    big_data_province = select(Info.province_id.label('info_province'), func.count()).where(and_(
        Major.special_name.like("%数据%"), Info.school_id == Major.school_id)).group_by(
        'info_province').order_by(func.count().desc())

    big_data_type = select(Major.type_name.label('type_name'), func.count()).where(
        Major.special_name.like("%数据%")).group_by('type_name').order_by(func.count().desc())

    big_data_level2 = select(Major.level2_name.label('level2_name'), func.count()).where(
        Major.special_name.like("%数据%")).group_by('level2_name').order_by(func.count().desc()).limit(5)

    big_data_level3 = select(Major.level2_name.label('level3_name'), func.count()).where(
        Major.special_name.like("%数据%")).group_by('level3_name').order_by(func.count().desc()).limit(5)

    @staticmethod
    def school_in_type(dual_class_name: str) -> select:
        return select(Info.school_id, func.count()).where(Info.dual_class_name == f'{dual_class_name}').group_by(
            Info.school_id)

    @staticmethod
    def major_in_type(special_name: str) -> select:
        return select(Major.school_id, func.count()).where(Major.special_name == f'{special_name}').group_by(
            Major.school_id)

    def __call__(self, api: str):
        if api == API.PROVINCE.value:
            return self.province
        elif api == API.DUAL_CLASS.value:
            return self.dual_class
        elif api == API.TYPE.value:
            return self.type_
        elif api == API.MAJOR.value:
            return self.major
        elif api == API.ADMISSIONS.value:
            return self.admissions
        elif api == API.BIG_DATA.value:
            return self.big_data
        elif api == API.BIG_DATA_PROVINCE.value:
            return self.big_data_province
        elif api == API.BIG_DATA_TYPE.value:
            return self.big_data_type
        elif api == API.BIG_DATA_LEVEL2.value:
            return self.big_data_level2
        elif api == API.BIG_DATA_LEVEL3.value:
            return self.big_data_level3
        elif api == API.BIG_DATA_IN_DUAL.value:
            return self.school_in_type('双一流'), self.major_in_type('数据科学与大数据技术')
        elif api == API.BIG_DATA_IN_NULL.value:
            return self.school_in_type('null'), self.major_in_type('数据科学与大数据技术')
        elif api == API.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value:
            return self.school_in_type('双一流'), self.major_in_type('人工智能')
        elif api == API.ARTIFICIAL_INTELLIGENCE_IN_NULL.value:
            return self.school_in_type('双一流'), self.major_in_type('人工智能')
