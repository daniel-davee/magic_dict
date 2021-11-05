from typing import Any
class Magic_dict(dict):
   
    _pure = False
    _obj = object()    
    
    def __init__(self,obj:Any=object()):
        self._obj = obj if obj else self._obj
        if isinstance(obj,dict): super().__init__(self._obj)
        else:super().__init__({})
    
    def __call__(self,*args, **kwargs) -> Any:
        return self._obj(*args,**kwargs) if callable(self._obj) else self._obj
    
    def __getattr__(self, key):
        return self[key]
    
    def __getitem__(self, key: str) -> Any:
        """[key is split into head and tail (everything else)
        if tail can be true in some sense call self[head] and 
        then try to call tail, if tail is empty and it already exist just return that,
        if it does exist yet don't worry, let's make magic_dict]

        Args:
            key (str): [key is in object path format, key1.key2.key3 or empty]]

        Returns:
            Any: [description]
        """
        keys = key.split('.')
        head, tail = keys[0], '.'.join(keys[1:])
        return self[head][tail] if tail else\
                    super().__getitem__(head) if head in self else\
                    self.__setitem__(head,Magic_dict())
        
    def __setitem__(self, key: str, value: Any) -> Any:
        if not self._obj: super()['_obj'] = value
        super().__setitem__(key, value)
        return value
 
    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
            return
        raise AttributeError(key)

    def __repr__(self):
        return '<Magic_dict ' + dict.__repr__(self) + '>'
