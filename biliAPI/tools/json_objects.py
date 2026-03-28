# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

import json

# ========== 模块级转换函数 ==========
def _convert(value):
    """递归转换：将 dict 转为 Dict，list 转为 List，其余保持原样。"""
    if isinstance(value, dict) and not isinstance(value, Dict):
        return Dict(value)
    elif isinstance(value, list) and not isinstance(value, List):
        return List(value)
    return value


# ========== 基类 ==========
class JSONContainer:
    """提供通用行为：字符串表示、递归转换、序列化接口。"""

    def __str__(self):
        return str(self.to_python())

    def __repr__(self):
        return f"{type(self).__name__}({repr(self._get_data())})"
    
    
    def _get_data(self):
        """返回内部存储的数据（子类必须实现）。"""
        raise NotImplementedError

    def to_python(self):
        """递归转换为普通 Python 对象（子类必须实现）。"""
        raise NotImplementedError


# ========== Dict 类 ==========
class Dict(dict, JSONContainer):
    """支持属性/键访问的字典，递归转换嵌套结构。"""

    def __init__(self, *args, **kwargs):
        raw_dict = dict(*args, **kwargs)
        converted_dict = {k: _convert(v) for k, v in raw_dict.items()}
        object.__setattr__(self, '_dict', converted_dict)

    def _get_data(self):
        return object.__getattribute__(self, '_dict')

    def to_python(self):
        d = self._get_data()
        return {
            k: (v.to_python() if isinstance(v, JSONContainer) else v)
            for k, v in d.items()
        }

    # 保留原有方法以保持兼容性
    def to_dict(self):
        return self.to_python()

    # ---------- 映射协议 ----------
    def __getattribute__(self, key):
        try:
            return object.__getattribute__(self, key)
        except AttributeError:
            try:
                return object.__getattribute__(self, '_dict')[key]
            except KeyError:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        if key == '_dict':
            raise AttributeError("'_dict' is a reserved attribute and cannot be set directly")
        try:
            object.__getattribute__(self, key)
            object.__setattr__(self, key, value)
        except AttributeError:
            converted = _convert(value)
            object.__getattribute__(self, '_dict')[key] = converted

    def __delattr__(self, key):
        if key == '_dict':
            raise AttributeError("'_dict' is a reserved attribute and cannot be deleted")
        try:
            object.__getattribute__(self, key)
            object.__delattr__(self, key)
        except AttributeError:
            try:
                del object.__getattribute__(self, '_dict')[key]
            except KeyError:
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def __getitem__(self, key):
        return object.__getattribute__(self, '_dict')[key]

    def __setitem__(self, key, value):
        converted = _convert(value)
        object.__getattribute__(self, '_dict')[key] = converted

    def __delitem__(self, key):
        del object.__getattribute__(self, '_dict')[key]

    def __contains__(self, key):
        return key in object.__getattribute__(self, '_dict')

    def __len__(self):
        return len(object.__getattribute__(self, '_dict'))

    def __iter__(self):
        return iter(object.__getattribute__(self, '_dict'))

    def items(self):
        return object.__getattribute__(self, '_dict').items()

    def keys(self):
        return object.__getattribute__(self, '_dict').keys()

    def values(self):
        return object.__getattribute__(self, '_dict').values()

    def get(self, key, default=None):
        return object.__getattribute__(self, '_dict').get(key, default)

    def update(self, *args, **kwargs):
        d = object.__getattribute__(self, '_dict')
        new_data = dict(*args, **kwargs)
        converted = {k: _convert(v) for k, v in new_data.items()}
        d.update(converted)


# ========== List 类 ==========
class List(list, JSONContainer):
    """类似列表的类，递归转换嵌套结构。"""

    def __init__(self, iterable=None):
        if iterable is None:
            raw_list = []
        else:
            raw_list = list(iterable)
        converted_list = [_convert(item) for item in raw_list]
        object.__setattr__(self, '_list', converted_list)

    def _get_data(self):
        return object.__getattribute__(self, '_list')

    def to_python(self):
        lst = self._get_data()
        return [
            item.to_python() if isinstance(item, JSONContainer) else item
            for item in lst
        ]

    # 保留原有方法以保持兼容性
    def to_list(self):
        return self.to_python()

    # ---------- 序列协议 ----------
    def __getitem__(self, index):
        return object.__getattribute__(self, '_list')[index]

    def __setitem__(self, index, value):
        converted = _convert(value)
        lst = object.__getattribute__(self, '_list')
        if isinstance(index, slice):
            if hasattr(value, '__iter__') and not isinstance(value, (str, bytes)):
                converted = [_convert(v) for v in value]
            else:
                converted = [converted]
        lst[index] = converted

    def __delitem__(self, index):
        del object.__getattribute__(self, '_list')[index]

    def __len__(self):
        return len(object.__getattribute__(self, '_list'))

    def __iter__(self):
        return iter(object.__getattribute__(self, '_list'))

    def __contains__(self, item):
        return item in object.__getattribute__(self, '_list')

    def append(self, value):
        converted = _convert(value)
        object.__getattribute__(self, '_list').append(converted)

    def extend(self, iterable):
        converted = [_convert(item) for item in iterable]
        object.__getattribute__(self, '_list').extend(converted)

    def insert(self, index, value):
        converted = _convert(value)
        object.__getattribute__(self, '_list').insert(index, converted)

    def pop(self, index=-1):
        return object.__getattribute__(self, '_list').pop(index)

    def remove(self, value):
        object.__getattribute__(self, '_list').remove(value)

    def clear(self):
        object.__getattribute__(self, '_list').clear()

    def copy(self):
        return List(object.__getattribute__(self, '_list'))

    def index(self, value, start=0, stop=None):
        lst = object.__getattribute__(self, '_list')
        if stop is None:
            return lst.index(value, start)
        return lst.index(value, start, stop)

    def count(self, value):
        return object.__getattribute__(self, '_list').count(value)

    def reverse(self):
        object.__getattribute__(self, '_list').reverse()

    def sort(self, key=None, reverse=False):
        object.__getattribute__(self, '_list').sort(key=key, reverse=reverse)


# ========== 模块级序列化函数 ==========
def loads(s, **args):
    obj = json.loads(s, **args)
    if isinstance(obj, list):
        return List(obj)
    if isinstance(obj, dict):
        return Dict(obj)
    return obj

def load(f, **args):
    obj = json.load(f, **args)
    if isinstance(obj, list):
        return List(obj)
    if isinstance(obj, dict):
        return Dict(obj)
    return obj

def dumps(obj, **args):
    if isinstance(obj, JSONContainer):
        return json.dumps(obj.to_python(), **args)
    return json.dumps(obj, **args)

def dump(obj, f, **args):
    if isinstance(obj, JSONContainer):
        return json.dump(obj.to_python(), f, **args)
    return json.dump(obj, f, **args)
    
def from_python(obj):
    if isinstance(obj, dict):
        return Dict(obj)
    if isinstance(obj, list):
        return List(obj)