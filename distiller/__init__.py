#
# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .utils import *
from .thresholding import GroupThresholdMixin, threshold_mask
from .config import fileConfig, dictConfig
from .model_summaries import *
from .scheduler import *
from .sensitivity import *
from .directives import *
from .policy import *
from .thinning import *

#del utils
del dictConfig
del thinning
#del model_summaries
#del scheduler
#del sensitivity
#del directives
#del thresholding
#del policy

# Distiller version
__version__ = "0.1.0"

def model_find_param_name(model, tensor_to_find):
    """Look up the name of a model tensor.

    Arguments:
        model: the model to search
        tensor_to_find: the tensors who's name we want to look up

    Returns:
        The parameter name (string) or None, if the paramter was not found.
    """
    for name, tensor  in model.state_dict().items():
        if tensor is tensor_to_find:
            return name
    return None

def model_find_param(model, param_to_find_name):
    """Look a model parameter by its name

    Arguments:
        model: the model to search
        param_to_find_name: the name of the parameter that we are searching for

    Returns:
        The parameter or None, if the paramter name was not found.
    """
    for name, param in model.named_parameters():
        if name == param_to_find_name:
            return param
    return None