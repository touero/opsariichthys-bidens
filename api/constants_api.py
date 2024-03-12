from enum import unique, Enum


@unique
class API(Enum):
    PROVINCE_COUNT = '/province_count'  # 各个省份包含大学
    DUAL_COUNT = '/dual_class_count'  # 各省份包含双一流数量
    TYPE_COUNT = '/type_count'  # 学校类别统计
    SPECIAL_COUNT = '/spacial_name_count'  # 所有专业统计
    SCORE_PROVINCE = '/score_province'  # 招生统计
    BIG_DATA_COUNT = '/big_data_count'  # 不同大数据专业统计
    BIG_DATA_PROVINCE_COUNT = '/big_data_province_count'  # 含大数据专业的省份内大学统计
    BIG_DATA_TYPE_COUNT = '/big_data_type_count'  # 大数据本科专科统计
    BIG_DATA_LEVEL2_COUNT = '/big_data_level2_count'  # 大数据二级类目统计
    BIG_DATA_LEVEL3_COUNT = '/big_data_level3_count'  # 大数据一级类目统计
    BIG_DATA_IN_DUAL = '/big_data_in_dual'  # 大数据在双一流占比
    BIG_DATA_IN_NULL = '/big_data_in_null'  # 大数据在普通院校占比
    ARTIFICIAL_INTELLIGENCE_IN_DUAL = '/artificial_intelligence_in_dual'  # 人工智能在双一流占比
    ARTIFICIAL_INTELLIGENCE_IN_NULL = '/artificial_intelligence_in_null'  # 人工智能在普通院校占比
