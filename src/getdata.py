import json

from province_map import province_mapping
from sql_master import SqlMaster
from src.constants import MyJson

from src.util.tools import turn_to_dict_of_list, save_json, exist_json


class GetData(SqlMaster):

    def __init__(self):
        super().__init__()
        # fixme is_upload是控制是否更新数据的参数，请尝试集成到default_config中
        self.is_upload = 0

    @property
    @exist_json(MyJson.PROVINCE_COUNT.value)
    def get_province(self) -> json:
        province_data = self.execute_sql('sql/province_count.sql')
        province_data_count = province_mapping(dict(province_data), 1)
        listResult = turn_to_dict_of_list(province_data_count)
        save_json(str(MyJson.PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.DUAL_COUNT.value)
    def get_dual_class_name(self) -> json:
        dual_data = self.execute_sql('sql/dual_class_count.sql')
        provinceDict = {}
        for item in dual_data:
            province_name = item[0]
            if province_name in provinceDict:
                provinceDict[item[0]] += 1
            elif province_name not in provinceDict:
                provinceDict[item[0]] = 1
        listResult = turn_to_dict_of_list(provinceDict)
        save_json(str(MyJson.DUAL_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.TYPE_COUNT.value)
    def get_type_name(self) -> json:
        type_name_data = self.execute_sql('sql/type_count.sql')
        type_nameDict = dict(type_name_data)
        listResult = turn_to_dict_of_list(type_nameDict)
        save_json(str(MyJson.TYPE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.SPECIAL_COUNT.value)
    def get_special_count(self) -> json:
        special_names = self.execute_sql('sql/spacial_name_count.sql')
        special_nameDict = dict(special_names)
        listResult = turn_to_dict_of_list(special_nameDict)
        save_json(str(MyJson.SPECIAL_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.SCORE_PROVINCE.value)
    def get_score_count(self) -> json:
        score_province = self.execute_sql('sql/score_province.sql')
        score_provinceDict = province_mapping(dict(score_province))
        listResult = turn_to_dict_of_list(score_provinceDict)
        save_json(str(MyJson.SCORE_PROVINCE.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_COUNT.value)
    def get_big_data_count(self) -> json:
        big_data = self.execute_sql('sql/big_data_count.sql')
        specialDict = {}
        for item in big_data:
            special_name = item[0]
            if special_name in specialDict:
                specialDict[item[0]] += 1
            elif special_name not in specialDict:
                specialDict[item[0]] = 1
        listResult = turn_to_dict_of_list(specialDict)
        save_json(str(MyJson.BIG_DATA_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_PROVINCE_COUNT.value)
    def get_big_data_province_count(self) -> json:
        big_data_province_count = self.execute_sql('sql/big_data_province_count.sql')
        big_data_provinceDict = province_mapping(dict(big_data_province_count))
        listResult = turn_to_dict_of_list(big_data_provinceDict)
        save_json(str(MyJson.BIG_DATA_PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_TYPE_COUNT.value)
    def get_big_data_type_count(self) -> json:
        big_data_type_count = self.execute_sql('sql/big_data_type_count.sql')
        big_data_typeDict = dict(big_data_type_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_TYPE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL2_COUNT.value)
    def get_big_data_level2_count(self) -> json:
        big_data_level2_count = self.execute_sql('sql/big_data_level2_count.sql')
        big_data_typeDict = dict(big_data_level2_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_LEVEL2_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL3_COUNT.value)
    def get_big_data_level3_count(self) -> json:
        big_data_level3_count = self.execute_sql('sql/big_data_level3_count.sql')
        big_data_typeDict = dict(big_data_level3_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_LEVEL3_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_IN_DUAL.value)
    def get_big_data_in_dual(self) -> json:
        school_dual = self.get_something_count('sql/dual.sql')
        big_data_count_temp = self.get_something_count('sql/big_data.sql')
        count_dual = 0
        for temp in big_data_count_temp:
            if temp in school_dual:
                count_dual += 1
        other = len(school_dual) - count_dual
        result = [{'name': '拥有', 'count': count_dual},
                  {'name': '未拥有', 'count': other}
                  ]
        save_json(str(MyJson.BIG_DATA_IN_DUAL.value), result)
        return result

    @property
    @exist_json(MyJson.BIG_DATA_IN_NULL.value)
    def get_big_data_in_null(self) -> json:
        school_dual = self.get_something_count('sql/null.sql')
        big_data_count_temp = self.get_something_count('sql/big_data.sql')
        count_dual = 0
        for temp in big_data_count_temp:
            if temp in school_dual:
                count_dual += 1
        other = len(school_dual) - count_dual
        result = [{'name': '拥有', 'count': count_dual},
                  {'name': '未拥有', 'count': other}
                  ]
        save_json(str(MyJson.BIG_DATA_IN_NULL.value), result)
        return result

    @property
    @exist_json(MyJson.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value)
    def get_artificial_intelligence_in_dual(self) -> json:
        school_dual = self.get_something_count('sql/dual.sql')
        count_temp = self.get_something_count('sql/artificial_intelligence.sql')
        count_dual = 0
        for temp in count_temp:
            if temp in school_dual:
                count_dual += 1
        other = len(school_dual) - count_dual
        result = [{'name': '拥有', 'count': count_dual},
                  {'name': '未拥有', 'count': other}
                  ]
        save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_DUAL.value), result)
        return result

    @property
    @exist_json(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value)
    def get_artificial_intelligence_in_null(self) -> json:
        school_dual = self.get_something_count('sql/null.sql')
        count_temp = self.get_something_count('sql/artificial_intelligence.sql')
        count_dual = 0
        for temp in count_temp:
            if temp in school_dual:
                count_dual += 1
        other = len(school_dual) - count_dual
        result = [{'name': '拥有', 'count': count_dual},
                  {'name': '未拥有', 'count': other}
                  ]
        save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value), result)
        return result
