"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2019 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""

from .detector_2d import Detector_2D
from .detector_3d import Detector_3D
from .detector_dummy import Detector_Dummy

# explicit import here for pyinstaller because it will not search .pyx source files.
from pupil_detectors.visualizer_3d import Eye_Visualizer
