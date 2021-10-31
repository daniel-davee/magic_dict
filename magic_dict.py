from typing import Any
class Magic_dict(dict):
   
    _pure = False    
    
    def __init__(self,obj:Any=None):
        self._obj = obj
        if isinstance(obj,dict): super().__init__(self._obj)
    
    def __call__(self,*args, **kwargs) -> Any:
        return self._obj(*args,**kwargs) if callable(self._obj) else self._obj
    
    def __getattr__(self, key):
        if key in self:return self[key]
        raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
            return
        raise AttributeError(key)

    def __repr__(self):
        return '<Magic_dict ' + dict.__repr__(self) + '>'
