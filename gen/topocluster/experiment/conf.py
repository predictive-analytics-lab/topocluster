# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any
from typing import Optional


@dataclass
class ExperimentConf:
    _target_: str = "topocluster.experiment.Experiment"
    datamodule: Any = MISSING  # DataModule
    encoder: Any = MISSING  # AutoEncoder
    clusterer: Any = MISSING  # Clusterer
    trainer: Any = MISSING  # Trainer
    pretrainer: Any = MISSING  # Trainer
    lr: float = 0.001
    log_offline: bool = False
    seed: Optional[int] = 42
