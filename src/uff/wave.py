from dataclasses import dataclass
from uff.aperture import Aperture
from uff.origin import Origin
from uff.wave_type import WaveType


@dataclass
class Wave:
    """
    UFF class to describe the geometry of a transmitted wave or beam.

    Attributes:
        origin 	(WaveOrigin):       Geometric origin of the wave.
        type (WaveType):         	enumerated type (int) (converging = 0, diverging = 1, plane = 2, cylindrical = 3, photoacoustic = 4, default = 0)
        aperture (Aperture):     	Description of the aperture used to produce the wave
        excitation 	(int): 	        (Optional) index to the unique excitation in the parent group
    """
    origin: Origin
    wave_type: WaveType
    aperture: Aperture
    excitation: int = None
