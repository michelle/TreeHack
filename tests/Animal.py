class Animal:
    """YOUR UR BASES is I"""
    name = "animal"
    def __init__( self ):
              pass
        
    def talk( self ):
              return "hi i am an %s" % self.name

class Dog( Animal ):
    """DOG I IS"""
    name = "dog"
    
    def bark( self ):
             return "WOff"

class K9( Dog ):
    """I AM KANINE, I BITE ThiNGS YO"""
    name = "Kannine"

    def bark( self ):
               return "GrrRR WOFF!"

class Cat( Animal ):
    """ MEOWWW!! """
    pass

def talkAnimals( *animals, **kwargs ):
    """ Tell your animals to talk """
    for animal in animals:
              print animal.talk()
