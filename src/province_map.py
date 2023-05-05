from constants import *


def province_mapping(dictObject: dict):
    for item in list(dictObject):
        if item in ProvinceID.JIANGSU.value:
            dictObject[Province.JIANGSU.value] = dictObject.pop(item)
        elif item in ProvinceID.GUANGDONG.value:
            dictObject[Province.GUANGDONG.value] = dictObject.pop(item)
        elif item in ProvinceID.HENAN.value:
            dictObject[Province.HENAN.value] = dictObject.pop(item)
        elif item in ProvinceID.SHANDONG.value:
            dictObject[Province.SHANDONG.value] = dictObject.pop(item)
        elif item in ProvinceID.SICHUAN.value:
            dictObject[Province.SICHUAN.value] = dictObject.pop(item)
        elif item in ProvinceID.HUBEI.value:
            dictObject[Province.HUBEI.value] = dictObject.pop(item)
        elif item in ProvinceID.HUNAN.value:
            dictObject[Province.HUNAN.value] = dictObject.pop(item)
        elif item in ProvinceID.ANHUI.value:
            dictObject[Province.ANHUI.value] = dictObject.pop(item)
        elif item in ProvinceID.HEBEI.value:
            dictObject[Province.HEBEI.value] = dictObject.pop(item)
        elif item in ProvinceID.ZHEJIANG.value:
            dictObject[Province.ZHEJIANG.value] = dictObject.pop(item)
        elif item in ProvinceID.LIAONING.value:
            dictObject[Province.LIAONING.value] = dictObject.pop(item)
        elif item in ProvinceID.JIANGXI.value:
            dictObject[Province.JIANGXI.value] = dictObject.pop(item)
        elif item in ProvinceID.SHANNXI.value:
            dictObject[Province.SHANNXI.value] = dictObject.pop(item)
        elif item in ProvinceID.BEIJING.value:
            dictObject[Province.BEIJING.value] = dictObject.pop(item)
        elif item in ProvinceID.FUJIAN.value:
            dictObject[Province.FUJIAN.value] = dictObject.pop(item)
        elif item in ProvinceID.YUNNAN.value:
            dictObject[Province.YUNNAN.value] = dictObject.pop(item)
        elif item in ProvinceID.GUANGXI.value:
            dictObject[Province.GUANGXI.value] = dictObject.pop(item)
        elif item in ProvinceID.SHANXI.value:
            dictObject[Province.SHANXI.value] = dictObject.pop(item)
        elif item in ProvinceID.HEILONGJIANG.value:
            dictObject[Province.HEILONGJIANG.value] = dictObject.pop(item)
        elif item in ProvinceID.CHONGQING.value:
            dictObject[Province.CHONGQING.value] = dictObject.pop(item)
        elif item in ProvinceID.GUIZHOU.value:
            dictObject[Province.GUIZHOU.value] = dictObject.pop(item)
        elif item in ProvinceID.JILIN.value:
            dictObject[Province.JILIN.value] = dictObject.pop(item)
        elif item in ProvinceID.SHANGHAI.value:
            dictObject[Province.SHANGHAI.value] = dictObject.pop(item)
        elif item in ProvinceID.TIANJIN.value:
            dictObject[Province.TIANJIN.value] = dictObject.pop(item)
        elif item in ProvinceID.XINJIANG.value:
            dictObject[Province.XINJIANG.value] = dictObject.pop(item)
        elif item in ProvinceID.NEIMENGGU.value:
            dictObject[Province.NEIMENGGU.value] = dictObject.pop(item)
        elif item in ProvinceID.GANSU.value:
            dictObject[Province.GANSU.value] = dictObject.pop(item)
        elif item in ProvinceID.HAINAN.value:
            dictObject[Province.HAINAN.value] = dictObject.pop(item)
        elif item in ProvinceID.NINGXIA.value:
            dictObject[Province.NINGXIA.value] = dictObject.pop(item)
        elif item in ProvinceID.XIANGGANG.value:
            dictObject[Province.XIANGGANG.value] = dictObject.pop(item)
        elif item in ProvinceID.QINGHAI.value:
            dictObject[Province.QINGHAI.value] = dictObject.pop(item)
        elif item in ProvinceID.XIZANG.value:
            dictObject[Province.XIZANG.value] = dictObject.pop(item)
        elif item in ProvinceID.AOMEN.value:
            dictObject[Province.AOMEN.value] = dictObject.pop(item)
    return dictObject

