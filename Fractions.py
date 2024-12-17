from Stalker import Stalker

class ClearSky(Stalker):
    _fraction = "Clear Sky"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "CS")
        super().__init__(name, rank)
        self._reputation["Neutral"] = 1000
        self._reputation["Clear Sky"] = 9999
        self._reputation["Bandit"] = -9999
        self._reputation["Military"] = -2500
        self._reputation["Dolg"] = 2000
        self._reputation["Swoboda"] = 2000
        self._reputation["Merc"] = 0
        self._reputation["Monolit"] = -9999
#end class ClearSky

class Neutral(Stalker):
    _fraction = "Neutral"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Neutral")
        super().__init__(name, rank)
        self._reputation["Neutral"] = 9999
        self._reputation["Clear Sky"] = 1000
        self._reputation["Bandit"] = -9999
        self._reputation["Military"] = -2500
        self._reputation["Dolg"] = 1000
        self._reputation["Swoboda"] = 2000
        self._reputation["Merc"] = -1000
        self._reputation["Monolit"] = -9999
#end class Neutral

class Bandit(Stalker):
    _fraction = "Bandit"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Bandit")
        super().__init__(name, rank)
        self._reputation["Neutral"] = -9999
        self._reputation["Clear Sky"] = -9999
        self._reputation["Bandit"] = 9999
        self._reputation["Military"] = -9999
        self._reputation["Dolg"] = -9999
        self._reputation["Swoboda"] = -9999
        self._reputation["Merc"] = 0
        self._reputation["Monolit"] = -9999
#end class Bandit

class Military(Stalker):
    _fraction = "Military"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Military")
        super().__init__(name, rank)
        self._reputation["Neutral"] = -9999
        self._reputation["Clear Sky"] = -2500
        self._reputation["Bandit"] = -9999
        self._reputation["Military"] = 9999
        self._reputation["Dolg"] = 0
        self._reputation["Swoboda"] = -5000
        self._reputation["Merc"] = -9999
        self._reputation["Monolit"] = -9999
#end class Military

class Dolg(Stalker):
    _fraction = "Dolg"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Dolg")
        super().__init__(name, rank)
        self._reputation["Neutral"] = 2000
        self._reputation["Clear Sky"] = 2000
        self._reputation["Bandit"] = -9999
        self._reputation["Military"] = 0
        self._reputation["Dolg"] = 9999
        self._reputation["Swoboda"] = -9999
        self._reputation["Merc"] = -4500
        self._reputation["Monolit"] = -9999
#end class Dolg

class Swoboda(Stalker):
    _fraction = "Swoboda"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Swoboda")
        super().__init__(name, rank)
        self._reputation["Neutral"] = 2000
        self._reputation["Clear Sky"] = 2000
        self._reputation["Bandit"] = -9999
        self._reputation["Military"] = -5000
        self._reputation["Dolg"] = -9999
        self._reputation["Swoboda"] = 9999
        self._reputation["Merc"] = -8000
        self._reputation["Monolit"] = -9999
#end class Swoboda

class Merc(Stalker):
    _fraction = "Merc"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Merc")
        super().__init__(name, rank)
        self._reputation["Neutral"] = -1000
        self._reputation["Clear Sky"] = 0
        self._reputation["Bandit"] = 0
        self._reputation["Military"] = -9999
        self._reputation["Dolg"] = -4500
        self._reputation["Swoboda"] = -9999
        self._reputation["Merc"] = 9999
        self._reputation["Monolit"] = -9999
#end class Merc

class Monolit(Stalker):
    _fraction = "Monolit"
    def __init__(self, rank, name):
        self._initTexturePath(rank, "Monolit")
        super().__init__(name, rank)
        self._reputation["Neutral"] = -9999
        self._reputation["Clear Sky"] = -9999
        self._reputation["Bandit"] = -9999
        self._reputation["Military"] = -9999
        self._reputation["Dolg"] = -9999
        self._reputation["Swoboda"] = -9999
        self._reputation["Merc"] = -9999
        self._reputation["Monolit"] = 9999
#end class Monolit
