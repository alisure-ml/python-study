"""
和类型相关，如判断类型
"""


class CoreType:
    # 判断类型:str
    @staticmethod
    def is_str(o):
        return isinstance(o, str)

    # 判断类型:list
    @staticmethod
    def is_list(o):
        return isinstance(o, list)

    # 判断类型:dict
    @staticmethod
    def is_dict(o):
        return isinstance(o, dict)

