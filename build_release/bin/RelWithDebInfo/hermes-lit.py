#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
import sys

# Make sure we can find the lit package.
sys.path.insert(0, os.path.join("C:/Users/Scott/hermes/external/llvh", 'utils', 'lit'))

if __name__=='__main__':
    from lit.main import main
    main({})
