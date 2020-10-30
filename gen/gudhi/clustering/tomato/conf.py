# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from typing import Any

from omegaconf import MISSING


@dataclass
class TomatoConf:
    _target_: str = "gudhi.clustering.tomato.Tomato"
    graph_type: Any = "knn"
    density_type: Any = "logDTM"
    n_clusters: Any = None
    merge_threshold: Any = None
    params: Any = MISSING