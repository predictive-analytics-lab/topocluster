# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field


@dataclass
class PlClustererConf:
    _target_: str = "topocluster.clustering.dac.PlClusterer"