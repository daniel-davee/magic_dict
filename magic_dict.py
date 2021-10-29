from typing import Any
class Magic_dict(dict):
    
    def __init__(self,obj:Any=None):
        obj = obj if isinstance(obj, dict) else {'obj' : obj}
        super().__init__(obj)
    
    def __call__(self) -> Any:
        return self.obj
    
    def __getattr__(self, key):
        if key in self:return self[key]
        raise AttributeError(key)

    def __setattr__(self, key, value):
        if key == 'obj': raise ValueError('obj cannot be key')
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
            return
        raise AttributeError(key)

    def __repr__(self):
        return '<Magic_dict ' + dict.__repr__(self) + '>'
