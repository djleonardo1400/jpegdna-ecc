#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author : Romain Graux
@date : 2022 May 13, 15:47:09
@last modified : 2022 June 14, 11:12:16
"""

import os
from glob import glob
from tqdm import tqdm
from functools import partial

import hydra
from omegaconf import OmegaConf
from helpers import omegaconf2namespace, Namespace

import numpy as np
import pandas as pd
import tensorflow as tf
from pyntcloud import PyntCloud
from multiprocessing import Pool

import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt

from fasta_io import latent_representation_to_fasta
from utils import pc_dir_to_ds, extract_path, extract_ext, extract_name, number_of_nucleotides


def align_files(*directories, return_names=False):
    """
    Allign all files based on the name of each file and zip them.
    """
    assert all(len(directory) > 0 for directory in directories), "Need at least 1 element in each directory"

    paths = [extract_path(directory[0]) for directory in directories]
    extentions = [extract_ext(directory[0]) for directory in directories] # Assume same extension for all files in a directory
    names = [set([extract_name(fname) for fname in directory]) for directory in directories]
    common_names = set.intersection(*names)
    common_names = sorted(common_names)
    files = [[f'{path}/{name}.{ext}' for name in common_names] for path, ext in zip(paths, extentions)]
    if return_names:
        return files + [common_names]
    return files

def load_file(fname):
    """
    Load a file and return the good format.
    """
    ext = extract_ext(fname)
    if ext == 'npy':
        return np.load(fname)
    elif ext == 'pkl':
        return pickle.load(open(fname, 'rb'))
    elif ext == 'ply':
        return PyntCloud.from_file(fname).points
    elif ext in ('dna', 'fasta', 'fastq'):
        with open(fname, 'r') as f:
            return f.read()
    else:
        return fname

def lazy_loader(files, args):
    """
    Load files in a lazy fashion.
    """
    for slice_files in files:
        yield [load_file(fname) for fname in slice_files]

def loader(files, args):
    """
    Load files in cache
    """
    return [load_file(fname) for fname in files]

def load_io_files(args, exception=[], only=[], return_names=False):
    """
    Load all files contained in the io subflag.
    """
    io = args.get('io', args)
    cdt_file = lambda name: name not in exception and (not len(only) or name in only)
    raw_files = [glob(f"{directory}/*") for name, directory in io.items() if cdt_file(name)]
    files = align_files(*raw_files, return_names=return_names)
    loader = lazy_loader(zip(*files) if len(files)>1 else np.reshape(files, (-1, 1)), args)
    return loader

# All tasks


def to_fastq(args):
    global file, fastq, _args
    _args = args
    files = load_io_files(args, only=['z'], return_names=True)
    for file, name in files:
        fasta = latent_representation_to_fasta(file, 200)
        with open(f"fasta/in/{name}.fasta", "w+") as fd:
            fd.write(fasta)





@hydra.main(config_path="config/benchmarks", config_name='config.yaml', version_base="1.2")
def main(cfg: OmegaConf) -> None:
    global args
    args = omegaconf2namespace(cfg)

    try:
        task = globals()[args.task]
    except KeyError:
        raise ValueError(f"Task {args.task} not supported")
    task(args)

if __name__ == '__main__':
    main()
