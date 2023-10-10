import os

from enum import Enum, unique, IntEnum
from dataclasses import dataclass
from tools import log_t


@unique
class API(Enum):
    PROVINCE_COUNT = 'province_count'  # 各个省份包含大学
    DUAL_COUNT = 'dual_class_count'  # 各省份包含双一流数量
    TYPE_COUNT = 'type_count'  # 学校类别统计
    SPECIAL_COUNT = 'spacial_name_count'  # 所有专业统计
    SCORE_PROVINCE = 'score_province'  # 招生统计
    BIG_DATA_COUNT = 'big_data_count'  # 不同大数据专业统计
    BIG_DATA_PROVINCE_COUNT = 'big_data_province_count'  # 含大数据专业的省份内大学统计
    BIG_DATA_TYPE_COUNT = 'big_data_type_count'  # 大数据本科专科统计
    BIG_DATA_LEVEL2_COUNT = 'big_data_level2_count'  # 大数据二级类目统计
    BIG_DATA_LEVEL3_COUNT = 'big_data_level3_count'  # 大数据一级类目统计
    BIG_DATA_IN_DUAL = 'big_data_in_dual'  # 大数据在双一流占比
    BIG_DATA_IN_NULL = 'big_data_in_null'  # 大数据在普通院校占比
    ARTIFICIAL_INTELLIGENCE_IN_DUAL = 'artificial_intelligence_in_dual'  # 人工智能在双一流占比
    ARTIFICIAL_INTELLIGENCE_IN_NULL = 'artificial_intelligence_in_null'  # 人工智能在普通院校占比


class MyJson(Enum):
    PROVINCE_COUNT = 'result_json/province_count.json'  # 各个省份包含大学
    DUAL_COUNT = 'result_json/dual_class_count.json'  # 各省份包含双一流数量
    TYPE_COUNT = 'result_json/type_count.json'  # 学校类别统计
    SPECIAL_COUNT = 'result_json/spacial_name_count.json'  # 所有专业统计
    SCORE_PROVINCE = 'result_json/score_province.json'  # 招生统计
    BIG_DATA_COUNT = 'result_json/big_data_count.json'  # 不同大数据专业统计
    BIG_DATA_PROVINCE_COUNT = 'result_json/big_data_province_count.json'  # 含大数据专业的省份内大学统计
    BIG_DATA_TYPE_COUNT = 'result_json/big_data_type_count.json'  # 大数据本科专科统计
    BIG_DATA_LEVEL2_COUNT = 'result_json/big_data_level2_count.json'  # 大数据二级类目统计
    BIG_DATA_LEVEL3_COUNT = 'result_json/big_data_level3_count.json'  # 大数据一级类目统计
    BIG_DATA_IN_DUAL = 'result_json/big_data_in_dual.json'  # 大数据在双一流占比
    BIG_DATA_IN_NULL = 'result_json/big_data_in_null.json'  # 大数据在普通院校占比
    ARTIFICIAL_INTELLIGENCE_IN_DUAL = 'result_json/artificial_intelligence_in_dual.json'  # 人工智能在双一流占比
    ARTIFICIAL_INTELLIGENCE_IN_NULL = 'result_json/artificial_intelligence_in_null.json'  # 人工智能在普通院校占比


@unique
class Province(Enum):
    JIANGSU = "江苏省"
    GUANGDONG = "广东省"
    HENAN = "河南省"
    SHANDONG = "山东省"
    SICHUAN = "四川省"
    HUBEI = "湖北省"
    HUNAN = "湖南省"
    ANHUI = "安徽省"
    HEBEI = "河北省"
    ZHEJIANG = "浙江省"
    LIAONING = "辽宁省"
    JIANGXI = "江西省"
    SHANNXI = "陕西省"
    BEIJING = "北京市"
    FUJIAN = "福建省"
    YUNNAN = "云南省"
    GUANGXI = "广西壮族自治区"
    SHANXI = "山西省"
    HEILONGJIANG = "黑龙江省"
    CHONGQING = "重庆市"
    GUIZHOU = "贵州省"
    JILIN = "吉林省"
    SHANGHAI = "上海市"
    TIANJIN = "天津市"
    XINJIANG = "新疆维吾尔自治区"
    NEIMENGGU = "内蒙古自治区"
    GANSU = "甘肃省"
    HAINAN = "海南省"
    NINGXIA = "宁夏回族自治区"
    XIANGGANG = "香港特别行政区"
    QINGHAI = "青海省"
    XIZANG = "西藏自治区"
    AOMEN = "澳门特别行政区"

    @staticmethod
    def province_mapping(dict_object: dict, args=0) -> dict:
        province = None
        if args == 0:
            province = ProvinceID
        elif args == 1:
            province = Province
        for item in list(dict_object):
            if item in province.JIANGSU.value:
                dict_object[Province.JIANGSU.value] = dict_object.pop(item)
            elif item in province.GUANGDONG.value:
                dict_object[Province.GUANGDONG.value] = dict_object.pop(item)
            elif item in province.HENAN.value:
                dict_object[Province.HENAN.value] = dict_object.pop(item)
            elif item in province.SHANDONG.value:
                dict_object[Province.SHANDONG.value] = dict_object.pop(item)
            elif item in province.SICHUAN.value:
                dict_object[Province.SICHUAN.value] = dict_object.pop(item)
            elif item in province.HUBEI.value:
                dict_object[Province.HUBEI.value] = dict_object.pop(item)
            elif item in province.HUNAN.value:
                dict_object[Province.HUNAN.value] = dict_object.pop(item)
            elif item in province.ANHUI.value:
                dict_object[Province.ANHUI.value] = dict_object.pop(item)
            elif item in province.HEBEI.value:
                dict_object[Province.HEBEI.value] = dict_object.pop(item)
            elif item in province.ZHEJIANG.value:
                dict_object[Province.ZHEJIANG.value] = dict_object.pop(item)
            elif item in province.LIAONING.value:
                dict_object[Province.LIAONING.value] = dict_object.pop(item)
            elif item in province.JIANGXI.value:
                dict_object[Province.JIANGXI.value] = dict_object.pop(item)
            elif item in province.SHANNXI.value:
                dict_object[Province.SHANNXI.value] = dict_object.pop(item)
            elif item in province.BEIJING.value:
                dict_object[Province.BEIJING.value] = dict_object.pop(item)
            elif item in province.FUJIAN.value:
                dict_object[Province.FUJIAN.value] = dict_object.pop(item)
            elif item in province.YUNNAN.value:
                dict_object[Province.YUNNAN.value] = dict_object.pop(item)
            elif item in province.GUANGXI.value:
                dict_object[Province.GUANGXI.value] = dict_object.pop(item)
            elif item in province.SHANXI.value:
                dict_object[Province.SHANXI.value] = dict_object.pop(item)
            elif item in province.HEILONGJIANG.value:
                dict_object[Province.HEILONGJIANG.value] = dict_object.pop(item)
            elif item in province.CHONGQING.value:
                dict_object[Province.CHONGQING.value] = dict_object.pop(item)
            elif item in province.GUIZHOU.value:
                dict_object[Province.GUIZHOU.value] = dict_object.pop(item)
            elif item in province.JILIN.value:
                dict_object[Province.JILIN.value] = dict_object.pop(item)
            elif item in province.SHANGHAI.value:
                dict_object[Province.SHANGHAI.value] = dict_object.pop(item)
            elif item in province.TIANJIN.value:
                dict_object[Province.TIANJIN.value] = dict_object.pop(item)
            elif item in province.XINJIANG.value:
                dict_object[Province.XINJIANG.value] = dict_object.pop(item)
            elif item in province.NEIMENGGU.value:
                dict_object[Province.NEIMENGGU.value] = dict_object.pop(item)
            elif item in province.GANSU.value:
                dict_object[Province.GANSU.value] = dict_object.pop(item)
            elif item in province.HAINAN.value:
                dict_object[Province.HAINAN.value] = dict_object.pop(item)
            elif item in province.NINGXIA.value:
                dict_object[Province.NINGXIA.value] = dict_object.pop(item)
            elif item in province.XIANGGANG.value:
                dict_object[Province.XIANGGANG.value] = dict_object.pop(item)
            elif item in province.QINGHAI.value:
                dict_object[Province.QINGHAI.value] = dict_object.pop(item)
            elif item in province.XIZANG.value:
                dict_object[Province.XIZANG.value] = dict_object.pop(item)
            elif item in province.AOMEN.value:
                dict_object[Province.AOMEN.value] = dict_object.pop(item)
        return dict_object


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
    Windows = "nt"
    Linux = "posix"

    @staticmethod
    def get_machine_host() -> str:
        temp = Server(os.name)
        log_t(f'machine_type: {temp}')
        if temp is Server.Windows:
            return Host.Local.value
        elif temp is Server.Linux:
            if os.path.exists('/.dockerenv'):
                return Host.Local.value
            return Host.Server.value

    @staticmethod
    def execute_command(cmd: str = None):
        if cmd is None:
            return
        os.system('chcp 65001')
        os.system(f'powershell -Command "{cmd}"')


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
    API_GET = 1
    API_POST = 2

    @staticmethod
    def api_task() -> list[int]:
        return [TaskType.API_GET.value, TaskType.API_POST.value]


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
class OutPath(Enum):
    READFILE = "part-r-00000"


@unique
class Host(Enum):
    Local = "127.0.0.1"
    Server = "0.0.0.0"


@unique
class IsUpload(IntEnum):
    Local = 0
    Update = 1


@dataclass
class DataBaseInfo:
    host: str = "127.0.0.1"
    user: str = 'root'
    password: str = '223366'
    database: str = 'AllSchoolAPI'
    port: int = 3306
