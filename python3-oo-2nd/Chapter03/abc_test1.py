# -*- coding: utf-8 -*-

import abc

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    
    @abc.abstractproperty
    def ext(self):
        pass
    
    @classmethod
    def __subclasshook(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        
        return NotImplemented

class Wav(MediaLoader):
    pass

class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        pass

if __name__ == '__main__':
    # x = Wav()はTypeErrorとなる
    o = Ogg()
    