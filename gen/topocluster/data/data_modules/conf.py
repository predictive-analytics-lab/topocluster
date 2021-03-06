# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field


@dataclass
class MNISTDataModuleConf:
    _target_: str = "topocluster.data.data_modules.MNISTDataModule"
    data_dir: str = "./"
    train_batch_size: int = 256
    test_batch_size: int = 1000
    num_workers: int = 0
    val_pcnt: float = 0.2
    label_threshold: int = 5


@dataclass
class CIFAR10DataModuleConf:
    _target_: str = "topocluster.data.data_modules.CIFAR10DataModule"
    data_dir: str = "./"
    train_batch_size: int = 256
    test_batch_size: int = 1000
    num_workers: int = 0
    val_pcnt: float = 0.2
    label_threshold: int = 5


@dataclass
class CIFAR100DataModuleConf:
    _target_: str = "topocluster.data.data_modules.CIFAR100DataModule"
    data_dir: str = "./"
    train_batch_size: int = 256
    test_batch_size: int = 1000
    num_workers: int = 0
    val_pcnt: float = 0.2
    label_threshold: int = 80


@dataclass
class SVHNDataModuleConf:
    _target_: str = "topocluster.data.data_modules.SVHNDataModule"
    data_dir: str = "./"
    train_batch_size: int = 256
    test_batch_size: int = 1000
    num_workers: int = 0
    val_pcnt: float = 0.2
    label_threshold: int = 5
