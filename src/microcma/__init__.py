from __future__ import absolute_import as _ab
from __future__ import division as _di
from __future__ import print_function as _pr

del _ab, _di, _pr

import warnings as _warnings

from . import purecma

try:
    import numpy as _np

    del _np
except ImportError:
    _warnings.warn(
        'Only `cma.purecma` has been imported. Install `numpy` ("pip'
        ' install numpy") if you want to import the entire `cma`'
        " package."
    )
else:
    from . import (constraints_handler, evolution_strategy, fitness_functions,
                   fitness_transformations, interfaces, optimization_tools,
                   sampler, sigma_adaptation, transformations, utilities)

    # from . import test  # gives a warning with python -m cma.test (since Python 3.5.3?)
    test = 'type "import cma.test" to access the `test` module of `cma`'
    from . import s
    from .evolution_strategy import (CMAEvolutionStrategy, fmin, fmin2,
                                     fmin_con, fmin_con2, fmin_lq_surr,
                                     fmin_lq_surr2)
    from .fitness_functions import ff
    from .fitness_transformations import GlueArguments, ScaleCoordinates
    from .options_parameters import CMAOptions, cma_default_options_

    CMA = CMAEvolutionStrategy  # shortcut for typing without completion
    from .constraints_handler import (BoundPenalty, BoundTransform,
                                      ConstrainedFitnessAL)
    from .logger import CMADataLogger, disp, plot, plot_zip
    from .optimization_tools import NoiseHandler
