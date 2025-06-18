# Import specific things from submodules to make them available at the package level
from .abc import ApiFetcherBase
from .dk import DMIClient  # Assuming DMIClient is made available in dk/__init__.py
from .se import SMHIClient # Assuming SMHIClient is made available in se/__init__.py

# Define what 'from datafetch import *' should bring in
__all__ = [
    'ApiFetcherBase',
    'DMIClient',
    'SMHIClient',
    # You might also choose to export the submodules themselves:
    # 'dk',
    # 'se',
]