# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from topocluster.clustering.kmeans import Backends
from typing import Optional


@dataclass
class KmeansConf:
    _target_: str = "topocluster.clustering.kmeans.Kmeans"
    n_iter: int = MISSING
    k: Optional[int] = None
    backend: Backends = Backends.TORCH
    verbose: bool = False
