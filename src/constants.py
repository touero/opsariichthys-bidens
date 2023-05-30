from enum import Enum, unique, IntEnum


@unique
class API(Enum):
    ERROR = '/'  # 未知
    PROVINCE_COUNT = '/province_count'  # 各个省份包含大学
    DUAL_COUNT = '/dual_class_count'  # 各省份包含双一流数量
    TYPE_COUNT = '/type_count'  # 学校类别统计
    SPECIAL_COUNT = '/spacial_name_count'  # 所有专业统计
    SCORE_PROVINCE = '/score_province'  # 招生统计
    BIG_DATA_COUNT = '/big_data_count'  # 不同大数据专业统计
    BIG_DATA_PROVINCE_COUNT = '/big_data_province_count'  # 含大数据专业的省份内大学统计
    BIG_DATA_TYPE_COUNT = '/big_data_type_count'  # 大数据本科专科统计


class MyJson(Enum):
    PROVINCE_COUNT = 'result_json/province_count.json'  # 各个省份包含大学
    DUAL_COUNT = 'result_json/dual_class_count.json'  # 各省份包含双一流数量
    TYPE_COUNT = 'result_json/type_count.json'  # 学校类别统计
    SPECIAL_COUNT = 'result_json/spacial_name_count.json'  # 所有专业统计
    SCORE_PROVINCE = 'result_json/score_province.json'  # 招生统计
    BIG_DATA_COUNT = 'result_json/big_data_count.json'  # 不同大数据专业统计
    BIG_DATA_PROVINCE_COUNT = 'result_json/big_data_province_count.json'  # 含大数据专业的省份内大学统计
    BIG_DATA_TYPE_COUNT = 'result_json/big_data_type_count.json'  # 大数据本科专科统计

@unique
class Province(Enum):
    JIANGSU = "江苏"
    GUANGDONG = "广东"
    HENAN = "河南"
    SHANDONG = "山东"
    SICHUAN = "四川"
    HUBEI = "湖北"
    HUNAN = "湖南"
    ANHUI = "安徽"
    HEBEI = "河北"
    ZHEJIANG = "浙江"
    LIAONING = "辽宁"
    JIANGXI = "江西"
    SHANNXI = "陕西"
    BEIJING = "北京"
    FUJIAN = "福建"
    YUNNAN = "云南"
    GUANGXI = "广西"
    SHANXI = "山西"
    HEILONGJIANG = "黑龙江"
    CHONGQING = "重庆"
    GUIZHOU = "贵州"
    JILIN = "吉林"
    SHANGHAI = "上海"
    TIANJIN = "天津"
    XINJIANG = "新疆"
    NEIMENGGU = "内蒙古"
    GANSU = "甘肃"
    HAINAN = "海南"
    NINGXIA = "宁夏"
    XIANGGANG = "香港"
    QINGHAI = "青海"
    XIZANG = "西藏"
    AOMEN = "澳门"


@unique
class ProvinceID(Enum):
    JIANGSU = "32"
    GUANGDONG = "44"
    HENAN = "41"
    SHANDONG = "37"
    SICHUAN = "51"
    HUBEI = "42"
    HUNAN = "43"
    ANHUI = "34"
    HEBEI = "13"
    ZHEJIANG = "33"
    LIAONING = "21"
    JIANGXI = "36"
    SHANNXI = "61"
    BEIJING = "11"
    FUJIAN = "35"
    YUNNAN = "53"
    GUANGXI = "45"
    SHANXI = "14"
    HEILONGJIANG = "23"
    CHONGQING = "50"
    GUIZHOU = "52"
    JILIN = "22"
    SHANGHAI = "31"
    TIANJIN = "12"
    XINJIANG = "65"
    NEIMENGGU = "15"
    GANSU = "62"
    HAINAN = "46"
    NINGXIA = "64"
    XIANGGANG = "81"
    QINGHAI = "63"
    XIZANG = "54"
    AOMEN = "82"


@unique
class Server(Enum):
    WINDOWS = "nt"
    LINUX = "posix"


@unique
class SqlInfo(Enum):
    HOST = '43.138.149.46'
    USER = 'root'
    PASSWORD = 'fanqiuyuan'
    PORT = 3306
    DATABASE = 'AllSchoolAPI'


@unique
class TaskType(IntEnum):
    CLEAR_DATA = 0  # 清洗数据，已弃用
    API = 1


@unique
class Name(Enum):
    SCHOOL_ID = 'school_id'  # 学校id代码
    DUAL_CLASS_NAME = 'dual_class_name'  # 是否为双一流
    BELONG = 'belong'  # 归属于
    ADDRESS = 'address'  # 学校地址
    CONTENT = 'content'  # 学校基本介绍
    PROVINCE_NAME = 'province_name'  # 学校所在省份名称
    SCHOOL_SITE = 'school_site'  # 学校招生页面
    NATURE_NAME = 'nature_name'  # 公办或者民营
    CITY_NAME = 'city_name'  # 所在城市
    LEVEL_NAME = 'level_name'  # 院校等级
    NAME = 'name'  # 学校名称
    SCHOOL_SCORE = 'school_score'  # 学校招生分数线
    MIN = 'min'  # 最低分
    PROVINCE_ID = 'province_id'  # 招生省份代码
    YEAR = 'year'  # 招生年份
    TYPE = 'type'  # 类型
    LIMIT_YEAR = 'limit_year'  # 学制
    TYPE_NAME = 'type_name'  # 专业等级
    LEVEL2_NAME = 'level2_name'  # 上级专业
    SPECIAL_NAME = 'special_name'  # 专业名称


@unique
class Path(Enum):
    READFILE = "part-r-00000"


@unique
class Host(Enum):
    LOCAL = "127.0.0.1"
    Server = "0.0.0.0"


@unique
class IsUpload(IntEnum):
    LOCAL = 0
    UPDATE = 1
