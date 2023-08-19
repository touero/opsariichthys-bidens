import json

from province_map import province_mapping
from sql_master import SqlMaster
from src.constants import MyJson

from src.util.tools import turn_to_dict_of_list, save_json, exist_json


class GetData:

    def __init__(self):
        super().__init__()
        # fixme is_upload是控制是否更新数据的参数，请尝试集成到default_config中
        self.is_upload = 0
        self.sql = SqlMaster()

    @property
    @exist_json(MyJson.PROVINCE_COUNT.value)
    def get_province(self) -> json:
        sql = "SELECT PROVINCE_NAME AS province,count(*) as times FROM info GROUP BY province ORDER BY times DESC;"
        province_data = sql.submit_sql_with_return(sql)
        province_data_count = province_mapping(dict(province_data), 1)
        listResult = turn_to_dict_of_list(province_data_count)
        save_json(str(MyJson.PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.DUAL_COUNT.value)
    def get_dual_class_name(self) -> json:
        sql = 'SELECT province_name, dual_class_name FROM info where dual_class_name = "双一流";'
        dual_data = self.sql.submit_sql_with_return(sql)
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
        sql = 'SELECT type_name AS type_name,count(*) AS times FROM info GROUP BY type_name ORDER BY times DESC;'
        type_name_data = self.sql.submit_sql_with_return(sql)
        type_nameDict = dict(type_name_data)
        listResult = turn_to_dict_of_list(type_nameDict)
        save_json(str(MyJson.TYPE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.SPECIAL_COUNT.value)
    def get_special_count(self) -> json:
        sql = 'SELECT special_name AS special_name,COUNT(*) AS times FROM major GROUP BY special_name ORDER BY times ' \
              'DESC LIMIT 10; '
        special_names = self.sql.submit_sql_with_return(sql)
        special_nameDict = dict(special_names)
        listResult = turn_to_dict_of_list(special_nameDict)
        save_json(str(MyJson.SPECIAL_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.SCORE_PROVINCE.value)
    def get_score_count(self) -> json:
        sql = 'SELECT province_id AS province_id_count,COUNT(*) AS times FROM score GROUP BY province_id  ORDER BY ' \
              'times DESC'
        score_province = self.sql.submit_sql_with_return(sql)
        score_provinceDict = province_mapping(dict(score_province))
        listResult = turn_to_dict_of_list(score_provinceDict)
        save_json(str(MyJson.SCORE_PROVINCE.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_COUNT.value)
    def get_big_data_count(self) -> json:
        sql = 'SELECT special_name  FROM major WHERE special_name LIKE "%数据%"'
        big_data = self.sql.submit_sql_with_return(sql)
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
        sql = 'SELECT info.province_id as province, count(*) AS times FROM info,major WHERE major.special_name like ' \
              '"%数据%" and info.school_id = major.school_id GROUP BY province ORDER BY times DESC; '
        big_data_province_count = self.sql.submit_sql_with_return(sql)
        big_data_provinceDict = province_mapping(dict(big_data_province_count))
        listResult = turn_to_dict_of_list(big_data_provinceDict)
        save_json(str(MyJson.BIG_DATA_PROVINCE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_TYPE_COUNT.value)
    def get_big_data_type_count(self) -> json:
        sql = 'SELECT type_name as type_name, count(*) as times FROM major WHERE special_name like "%数据%"  GROUP BY ' \
              'type_name ORDER BY times DESC; '
        big_data_type_count = self.sql.submit_sql_with_return(sql)
        big_data_typeDict = dict(big_data_type_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_TYPE_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL2_COUNT.value)
    def get_big_data_level2_count(self) -> json:
        sql = 'SELECT level2_name as level2_name, count(*) as times FROM major WHERE major.special_name like "%数据%" ' \
              'GROUP BY level2_name ORDER BY times DESC limit 5 '
        big_data_level2_count = self.sql.submit_sql_with_return(sql)
        big_data_typeDict = dict(big_data_level2_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_LEVEL2_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_LEVEL3_COUNT.value)
    def get_big_data_level3_count(self) -> json:
        sql = 'SELECT level3_name as level3_name, count(*) as times FROM major WHERE major.special_name like "%数据%" ' \
              'GROUP BY level3_name ORDER BY times DESC limit 10 '
        big_data_level3_count = self.sql.submit_sql_with_return(sql)
        big_data_typeDict = dict(big_data_level3_count)
        listResult = turn_to_dict_of_list(big_data_typeDict)
        save_json(str(MyJson.BIG_DATA_LEVEL3_COUNT.value), listResult)
        return listResult

    @property
    @exist_json(MyJson.BIG_DATA_IN_DUAL.value)
    def get_big_data_in_dual(self) -> json:
        dual_sql = 'select school_id from info where dual_class_name="双一流"'
        school_dual = self.sql.get_something_count(dual_sql)
        big_data_sql = 'select school_id from major where special_name="数据科学与大数据技术"'
        big_data_count_temp = self.sql.get_something_count(big_data_sql)
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
        null_sql = 'select school_id from info where dual_class_name="null"'
        school_dual = self.sql.get_something_count(null_sql)
        big_data_sql = 'select school_id from major where special_name="数据科学与大数据技术"'
        big_data_count_temp = self.sql.get_something_count(big_data_sql)
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
        null_sql = 'select school_id from info where dual_class_name="双一流"'
        school_dual = self.sql.get_something_count(null_sql)
        big_data_sql = 'select school_id from major where special_name="人工智能"'
        big_data_count_temp = self.sql.get_something_count(big_data_sql)
        count_dual = 0
        for temp in big_data_count_temp:
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
        null_sql = 'select school_id from info where dual_class_name="null"'
        school_dual = self.sql.get_something_count(null_sql)
        big_data_sql = 'select school_id from major where special_name="人工智能"'
        big_data_count_temp = self.sql.get_something_count(big_data_sql)
        count_dual = 0
        for temp in big_data_count_temp:
            if temp in school_dual:
                count_dual += 1
        other = len(school_dual) - count_dual
        result = [{'name': '拥有', 'count': count_dual},
                  {'name': '未拥有', 'count': other}
                  ]
        save_json(str(MyJson.ARTIFICIAL_INTELLIGENCE_IN_NULL.value), result)
        return result
