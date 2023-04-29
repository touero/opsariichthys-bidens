from enum import Enum, unique, IntEnum


@unique
class API(Enum):
    ERROR = '/'  # 未知
    PROVINCE_COUNT = '/province_count'  # 各个省份包含大学
    DUAL_COUNT = '/dual_class_count'  # 各省份包含双一流数量
    TYPE_COUNT = '/type_count'  # 学校类别统计


@unique
class Docker(IntEnum):
    NOT = 0
    IN = 1


@unique
class SqlInfo(Enum):
    HOST = 'localhost'
    USER = 'username'
    PASSWORD = 'password'
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
