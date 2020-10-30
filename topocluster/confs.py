from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Dict, List, Literal, Optional

from ethicml.data import CelebAttrs
from ethicml.data.tabular_data.adult import AdultSplits
from omegaconf import MISSING
import torch

__all__ = ["BaseArgs", "ClusterArgs"]


@dataclass
class DataConf:
    _device: torch.device
    _s_dim: int
    _y_dim: int


class QuantLevel(Enum):
    THREE = auto()
    FIVE = auto()
    EIGHT = auto()


class ImageDataConf(DataConf):
    """General data set settings."""

    data_pcnt: float = 1.0  # data pcnt should be a real value > 0, and up to 1
    data_split_seed: int = 888
    root: str = ""
    save_dir: str = "experiments"

    # Colored MNIST settings
    scale: float = 0.02
    greyscale: bool = False
    background: bool = False
    black: bool = True
    binarize: bool = True
    rotate_data: bool = False
    shift_data: bool = False
    color_correlation: float = 1.0
    padding: int = 2  # by how many pixels to pad the cmnist images by
    quant_level: QuantLevel = QuantLevel.EIGHT  # number of bits that encode color
    # the subsample flags work like this: you give it a class id and a fraction in the form of a
    # float. the class id is given by class_id = y * s_count + s, so for binary s and y, the
    # correspondance is like this:
    # 0: y=0/s=0, 1: y=0/s=1, 2: y=1/s=0, 3: y=1/s=1
    input_noise: bool = True  # add uniform noise to the input

    visualize_clusters: bool = True
    # General settings
    use_wandb: bool = False

    # Global variables
    _s_dim: int
    _y_dim: int

    #  General training settings
    epochs: int = 250
    gpu: int = 0  # which GPU to use (if available)
    batch_size: int = 256
    test_batch_size: Optional[int] = None
    num_workers: int = 4
    seed: int = 4


@dataclass
class ExperimentConf:
    # data: DataConf
    clusterer: Any = MISSING


@dataclass
class EncoderConf:
    _target_: str = MISSING
    path: str = ""
    pt_epochs: int = 100  # number of pre-training epochs
    lr: float = 1e-3
    weight_decay: float = 0
    # Encoder settings
    save_encodings: bool = False
    ft: bool = False
    ft_lr: float = 1e-6
    ft_weight_decay: float = 0
    freeze_layers: int = 0


@dataclass
class AeConf(EncoderConf):
    # Encoder settings
    encoder: Literal["ae", "vae", "rotnet"] = "ae"
    enc_levels: int = 4
    enc_dim: int = 64
    init_channels: int = 32
    recon_loss: Literal["l1", "l2", "bce", "huber", "ce", "mixed"] = "l2"


# @dataclass
# class TrainConfig:
#     encode_batch_size: int = 1000

#     # Evaluation settings
#     eval_epochs: int = 40
#     eval_lr: float = 1e-3
#     # Training settings
#     resume: Optional[str] = None
#     evaluate: bool = False
#     val_freq: int = 5
#     log_freq: int = 50
#     feat_attr: bool = False
#     with_supervision: bool = True
#     # Optimization settings
#     early_stopping: int = 30


@dataclass
class RankedStatsConfig:
    """Flags for clustering."""

    # PseudoLabeler
    pseudo_labeler: Literal["ranking", "cosine"] = "ranking"
    sup_ce_weight: float = 1.0
    sup_bce_weight: float = 1.0
    k_num: int = 5
    lower_threshold: float = 0.5
    upper_threshold: float = 0.5

    # Classifier
    # clf_hidden_dims: List[int] = [256]
    clf_lr: float = 1e-3
    clf_weight_decay: float = 0
    use_multi_head: bool = False

    # Method
    method: Literal[
        "pl_enc", "pl_output", "pl_enc_no_norm", "kmeans", "topocluster"
    ] = "topocluster"

    #  Labeler
    labeler_lr: float = 1e-3
    labeler_weight_decay: float = 0
    # labeler_hidden_dims: List[int] = [100, 100]
    labeler_epochs: int = 100
    labeler_wandb: bool = False