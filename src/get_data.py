import json
from typing import Optional, Union
from constants import MyJson, API, Province
from sql_master import SqlMaster

from tools import Tools, exist_json


class GetData:
    sql: SqlMaster

    def __init__(self):
        self.sql: Optional[SqlMaster] = SqlMaster()
        self.func_names: dict = {API.PROVINCE_COUNT.value: 'get_province',
                                 API.DUAL_COUNT.value: 'get_dual_class_name',
                                 API.TYPE_COUNT.value: 'get_type_name',
                                 API.SPECIAL_COUNT.value: 'get_special_count',
                                 API.SCORE_PROVINCE.value: 'get_score_count',
                                 API.BIG_DATA_COUNT.value: 'get_big_data_count',
                                 API.BIG_DATA_PROVINCE_COUNT.value: 'get_big_data_province_count',
                                 API.BIG_DATA_TYPE_COUNT.value: 'get_big_data_type_count',
                                 API.BIG_DATA_LEVEL2_COUNT.value: 'get_big_data_level2_count',
                                 API.BIG_DATA_LEVEL3_COUNT.value: 'get_big_data_level3_count',
                                 API.BIG_DATA_IN_DUAL.value: 'get_big_data_in_dual',
                                 API.BIG_DATA_IN_NULL.value: 'get_big_data_in_null',
                                 API.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value: 'get_artificial_intelligence_in_dual',
                                 API.ARTIFICIAL_INTELLIGENCE_IN_NULL.value: 'get_artificial_intelligence_in_null'}

    def api_select(self, item: str) -> Union[dict, None]:
        func_name = self.func_names.get(item, None)
        if func_name is None:
            return None
        return getattr(self, func_name, None)

    @property
    @exist_json(MyJson.PROVINCE_COUNT.value)
    def get_province(self) -> json:
        province_data = self.sql.execute_sql('sql/province_count.sql')
        province_data_count = Province.province_mapping(dict(province_data), 1)
        list_result = Tools.turn_to_dict_of_list(province_data_count)
        Tools.save_json(str(MyJson.PROVINCE_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.DUAL_COUNT.value)
    def get_dual_class_name(self) -> json:
        dual_data = self.sql.execute_sql('sql/dual_class_count.sql')
        province_dict = Tools.both_count(dual_data)
        list_result = Tools.turn_to_dict_of_list(province_dict)
        Tools.save_json(str(MyJson.DUAL_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.TYPE_COUNT.value)
    def get_type_name(self) -> json:
        type_name_data = self.sql.execute_sql('sql/type_count.sql')
        type_name_dict = dict(type_name_data)
        list_result = Tools.turn_to_dict_of_list(type_name_dict)
        Tools.save_json(str(MyJson.TYPE_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.SPECIAL_COUNT.value)
    def get_special_count(self) -> json:
        special_names = self.sql.execute_sql('sql/spacial_name_count.sql')
        special_name_dict = dict(special_names)
        list_result = Tools.turn_to_dict_of_list(special_name_dict)
        Tools.save_json(str(MyJson.SPECIAL_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.SCORE_PROVINCE.value)
    def get_score_count(self) -> json:
        score_province = self.sql.execute_sql('sql/score_province.sql')
        score_province_dict = Province.province_mapping(dict(score_province))
        list_result = Tools.turn_to_dict_of_list(score_province_dict)
        Tools.save_json(str(MyJson.SCORE_PROVINCE.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.BIG_DATA_COUNT.value)
    def get_big_data_count(self) -> json:
        big_data = self.sql.execute_sql('sql/big_data_count.sql')
        special_dict = Tools.both_count(big_data)
        list_result = Tools.turn_to_dict_of_list(special_dict)
        Tools.save_json(str(MyJson.BIG_DATA_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.BIG_DATA_PROVINCE_COUNT.value)
    def get_big_data_province_count(self) -> json:
        big_data_province_count = self.sql.execute_sql('sql/big_data_province_count.sql')
        big_data_province_dict = Province.province_mapping(dict(big_data_province_count))
        list_result = Tools.turn_to_dict_of_list(big_data_province_dict)
        Tools.save_json(str(MyJson.BIG_DATA_PROVINCE_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.BIG_DATA_TYPE_COUNT.value)
    def get_big_data_type_count(self) -> json:
        big_data_type_count = self.sql.execute_sql('sql/big_data_type_count.sql')
        big_data_type_dict = dict(big_data_type_count)
        list_result = Tools.turn_to_dict_of_list(big_data_type_dict)
        Tools.save_json(str(MyJson.BIG_DATA_TYPE_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL2_COUNT.value)
    def get_big_data_level2_count(self) -> json:
        big_data_level2_count = self.sql.execute_sql('sql/big_data_level2_count.sql')
        big_data_type_dict = dict(big_data_level2_count)
        list_result = Tools.turn_to_dict_of_list(big_data_type_dict)
        Tools.save_json(str(MyJson.BIG_DATA_LEVEL2_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL3_COUNT.value)
    def get_big_data_level3_count(self) -> json:
        big_data_level3_count = self.sql.execute_sql('sql/big_data_level3_count.sql')
        big_data_type_dict = dict(big_data_level3_count)
        list_result = Tools.turn_to_dict_of_list(big_data_type_dict)
        Tools.save_json(str(MyJson.BIG_DATA_LEVEL3_COUNT.value), list_result)
        return list_result

    @property
    @exist_json(MyJson.BIG_DATA_IN_DUAL.value)
    def get_big_data_in_dual(self) -> json:
        school_dual = self.sql.get_something_count('sql/dual.sql')
        big_data_count_temp = self.sql.get_something_count('sql/big_data.sql')
        result = Tools.hava_count(school_dual, big_data_count_temp)
        Tools.save_json(str(MyJson.BIG_DATA_IN_DUAL.value), result)
        return result

    @property
    @exist_json(MyJson.BIG_DATA_IN_NULL.value)
    def get_big_data_in_null(self) -> json:
        school_dual = self.sql.get_something_count('sql/null.sql')
        big_data_count_temp = self.sql.get_something_count('sql/big_data.sql')
        result = Tools.hava_count(school_dual, big_data_count_temp)
        Tools.save_json(str(MyJson.BIG_DATA_IN_NULL.value), result)
        return result

    @property
    @exist_json(MyJson.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value)
    def get_artificial_intelligence_in_dual(self) -> json:
        school_dual = self.sql.get_something_count('sql/dual.sql')
        count_temp = self.sql.get_something_count('sql/artificial_intelligence.sql')
        result = Tools.hava_count(school_dual, count_temp)
        Tools.save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value), result)
        return result

    @property
    @exist_json(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value)
    def get_artificial_intelligence_in_null(self) -> json:
        school_dual = self.sql.get_something_count('sql/null.sql')
        count_temp = self.sql.get_something_count('sql/artificial_intelligence.sql')
        result = Tools.hava_count(school_dual, count_temp)
        Tools.save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value), result)
        return result
