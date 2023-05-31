from constants import *


def province_mapping(dictObject: dict, args=0):
    global province
    if args == 0:
        province = ProvinceID
    elif args == 1:
        province = Province
    for item in list(dictObject):
        if item in province.JIANGSU.value:
            dictObject[Province.JIANGSU.value] = dictObject.pop(item)
        elif item in province.GUANGDONG.value:
            dictObject[Province.GUANGDONG.value] = dictObject.pop(item)
        elif item in province.HENAN.value:
            dictObject[Province.HENAN.value] = dictObject.pop(item)
        elif item in province.SHANDONG.value:
            dictObject[Province.SHANDONG.value] = dictObject.pop(item)
        elif item in province.SICHUAN.value:
            dictObject[Province.SICHUAN.value] = dictObject.pop(item)
        elif item in province.HUBEI.value:
            dictObject[Province.HUBEI.value] = dictObject.pop(item)
        elif item in province.HUNAN.value:
            dictObject[Province.HUNAN.value] = dictObject.pop(item)
        elif item in province.ANHUI.value:
            dictObject[Province.ANHUI.value] = dictObject.pop(item)
        elif item in province.HEBEI.value:
            dictObject[Province.HEBEI.value] = dictObject.pop(item)
        elif item in province.ZHEJIANG.value:
            dictObject[Province.ZHEJIANG.value] = dictObject.pop(item)
        elif item in province.LIAONING.value:
            dictObject[Province.LIAONING.value] = dictObject.pop(item)
        elif item in province.JIANGXI.value:
            dictObject[Province.JIANGXI.value] = dictObject.pop(item)
        elif item in province.SHANNXI.value:
            dictObject[Province.SHANNXI.value] = dictObject.pop(item)
        elif item in province.BEIJING.value:
            dictObject[Province.BEIJING.value] = dictObject.pop(item)
        elif item in province.FUJIAN.value:
            dictObject[Province.FUJIAN.value] = dictObject.pop(item)
        elif item in province.YUNNAN.value:
            dictObject[Province.YUNNAN.value] = dictObject.pop(item)
        elif item in province.GUANGXI.value:
            dictObject[Province.GUANGXI.value] = dictObject.pop(item)
        elif item in province.SHANXI.value:
            dictObject[Province.SHANXI.value] = dictObject.pop(item)
        elif item in province.HEILONGJIANG.value:
            dictObject[Province.HEILONGJIANG.value] = dictObject.pop(item)
        elif item in province.CHONGQING.value:
            dictObject[Province.CHONGQING.value] = dictObject.pop(item)
        elif item in province.GUIZHOU.value:
            dictObject[Province.GUIZHOU.value] = dictObject.pop(item)
        elif item in province.JILIN.value:
            dictObject[Province.JILIN.value] = dictObject.pop(item)
        elif item in province.SHANGHAI.value:
            dictObject[Province.SHANGHAI.value] = dictObject.pop(item)
        elif item in province.TIANJIN.value:
            dictObject[Province.TIANJIN.value] = dictObject.pop(item)
        elif item in province.XINJIANG.value:
            dictObject[Province.XINJIANG.value] = dictObject.pop(item)
        elif item in province.NEIMENGGU.value:
            dictObject[Province.NEIMENGGU.value] = dictObject.pop(item)
        elif item in province.GANSU.value:
            dictObject[Province.GANSU.value] = dictObject.pop(item)
        elif item in province.HAINAN.value:
            dictObject[Province.HAINAN.value] = dictObject.pop(item)
        elif item in province.NINGXIA.value:
            dictObject[Province.NINGXIA.value] = dictObject.pop(item)
        elif item in province.XIANGGANG.value:
            dictObject[Province.XIANGGANG.value] = dictObject.pop(item)
        elif item in province.QINGHAI.value:
            dictObject[Province.QINGHAI.value] = dictObject.pop(item)
        elif item in province.XIZANG.value:
            dictObject[Province.XIZANG.value] = dictObject.pop(item)
        elif item in province.AOMEN.value:
            dictObject[Province.AOMEN.value] = dictObject.pop(item)
    return dictObject


