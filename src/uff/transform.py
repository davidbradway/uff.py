from dataclasses import dataclass
from uff.translation import Translation
from uff.rotation import Rotation


@dataclass
class Transform:
    """Specifies a 3D affine transformation of rotation plus translation,
    in that order, where the translation is done on the unrotated 
    coordinate system. The direction is given by local coordinate 
    system of the object that owns this object.

    Atributes:
        translation (Translation): 	change in position in meters
        rotation (Rotation): 	    change in rotation in radians
    """
    translation: Translation
    rotation: Rotation

