import json
from typing import Optional
from constants import MyJson, API
from sql_master import SqlMaster

from util.tools import turn_to_dict_of_list, save_json, exist_json, province_mapping, both_count, hava_count


class GetData:
    def __init__(self):
        self.sql: Optional[SqlMaster] = None

    def sql_init(self, sql: Optional[SqlMaster]) -> None:
        self.sql = sql

    def api_select(self, item: str) -> dict:
        result = {}
        if item == API.PROVINCE_COUNT.value:
            result = self.get_province
        elif item == API.DUAL_COUNT.value:
            result = self.get_dual_class_name
        elif item == API.TYPE_COUNT.value:
            result = self.get_type_name
        elif item == API.SPECIAL_COUNT.value:
            result = self.get_special_count
        elif item == API.SCORE_PROVINCE.value:
            result = self.get_score_count
        elif item == API.BIG_DATA_COUNT.value:
            result = self.get_big_data_count
        elif item == API.BIG_DATA_PROVINCE_COUNT.value:
            result = self.get_big_data_province_count
        elif item == API.BIG_DATA_TYPE_COUNT.value:
            result = self.get_big_data_type_count
        elif item == API.BIG_DATA_LEVEL2_COUNT.value:
            result = self.get_big_data_level2_count
        elif item == API.BIG_DATA_LEVEL3_COUNT.value:
            result = self.get_big_data_level3_count
        elif item == API.BIG_DATA_IN_DUAL.value:
            result = self.get_big_data_in_dual
        elif item == API.BIG_DATA_IN_NULL.value:
            result = self.get_big_data_in_null
        elif item == API.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value:
            result = self.get_artificial_intelligence_in_dual
        elif item == API.ARTIFICIAL_INTELLIGENCE_IN_NULL.value:
            result = self.get_artificial_intelligence_in_null
        return result

    @property
    @exist_json(MyJson.PROVINCE_COUNT.value)
    def get_province(self) -> json:
        province_data = self.sql.execute_sql('sql/province_count.sql')
        province_data_count = province_mapping(dict(province_data), 1)
        listResult = turn_to_dict_of_list(province_data_count)
        save_json(str(MyJson.PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.DUAL_COUNT.value)
    def get_dual_class_name(self) -> json:
        dual_data = self.sql.execute_sql('sql/dual_class_count.sql')
        provinceDict = both_count(dual_data)
        listResult = turn_to_dict_of_list(provinceDict)
        save_json(str(MyJson.DUAL_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.TYPE_COUNT.value)
    def get_type_name(self) -> json:
        type_name_data = self.sql.execute_sql('sql/type_count.sql')
        type_nameDict = dict(type_name_data)
        listResult = turn_to_dict_of_list(type_nameDict)
        save_json(str(MyJson.TYPE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.SPECIAL_COUNT.value)
    def get_special_count(self) -> json:
        special_names = self.sql.execute_sql('sql/spacial_name_count.sql')
        special_nameDict = dict(special_names)
        listResult = turn_to_dict_of_list(special_nameDict)
        save_json(str(MyJson.SPECIAL_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.SCORE_PROVINCE.value)
    def get_score_count(self) -> json:
        score_province = self.sql.execute_sql('sql/score_province.sql')
        score_provinceDict = province_mapping(dict(score_province))
        listResult = turn_to_dict_of_list(score_provinceDict)
        save_json(str(MyJson.SCORE_PROVINCE.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_COUNT.value)
    def get_big_data_count(self) -> json:
        big_data = self.sql.execute_sql('sql/big_data_count.sql')
        specialDict = both_count(big_data)
        listResult = turn_to_dict_of_list(specialDict)
        save_json(str(MyJson.BIG_DATA_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_PROVINCE_COUNT.value)
    def get_big_data_province_count(self) -> json:
        big_data_province_count = self.sql.execute_sql('sql/big_data_province_count.sql')
        big_data_provinceDict = province_mapping(dict(big_data_province_count))
        listResult = turn_to_dict_of_list(big_data_provinceDict)
        save_json(str(MyJson.BIG_DATA_PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_TYPE_COUNT.value)
    def get_big_data_type_count(self) -> json:
        big_data_type_count = self.sql.execute_sql('sql/big_data_type_count.sql')
        big_data_typeDict = dict(big_data_type_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_TYPE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL2_COUNT.value)
    def get_big_data_level2_count(self) -> json:
        big_data_level2_count = self.sql.execute_sql('sql/big_data_level2_count.sql')
        big_data_typeDict = dict(big_data_level2_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_LEVEL2_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL3_COUNT.value)
    def get_big_data_level3_count(self) -> json:
        big_data_level3_count = self.sql.execute_sql('sql/big_data_level3_count.sql')
        big_data_typeDict = dict(big_data_level3_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_LEVEL3_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_IN_DUAL.value)
    def get_big_data_in_dual(self) -> json:
        school_dual = self.sql.get_something_count('sql/dual.sql')
        big_data_count_temp = self.sql.get_something_count('sql/big_data.sql')
        result = hava_count(school_dual, big_data_count_temp)
        save_json(str(MyJson.BIG_DATA_IN_DUAL.value), result)
        return result

    @property
    @exist_json(MyJson.BIG_DATA_IN_NULL.value)
    def get_big_data_in_null(self) -> json:
        school_dual = self.sql.get_something_count('sql/null.sql')
        big_data_count_temp = self.sql.get_something_count('sql/big_data.sql')
        result = hava_count(school_dual, big_data_count_temp)
        save_json(str(MyJson.BIG_DATA_IN_NULL.value), result)
        return result

    @property
    @exist_json(MyJson.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value)
    def get_artificial_intelligence_in_dual(self) -> json:
        school_dual = self.sql.get_something_count('sql/dual.sql')
        count_temp = self.sql.get_something_count('sql/artificial_intelligence.sql')
        result = hava_count(school_dual, count_temp)
        save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value), result)
        return result

    @property
    @exist_json(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value)
    def get_artificial_intelligence_in_null(self) -> json:
        school_dual = self.sql.get_something_count('sql/null.sql')
        count_temp = self.sql.get_something_count('sql/artificial_intelligence.sql')
        result = hava_count(school_dual, count_temp)
        save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value), result)
        return result
