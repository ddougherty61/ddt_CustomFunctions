import inspect
import logging
import datetime as dt
import math
from sqlalchemy.sql.sqltypes import TIMESTAMP,VARCHAR
import numpy as np
import pandas as pd

from iotfunctions.base import BaseTransformer
from iotfunctions import ui

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install.
# Example assumes the repository is private.
# Replace XXXXXX with your personal access token.
# After @ you must specify a branch.

#PACKAGE_URL = 'git+https://XXXXXX@github.com/<user_id><path_to_repository>@starter_package'
PACKAGE_URL = 'git+https://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@github.com/ddougherty61/ddt_CustomFunctions@starter_package'

class zDDT_Func1(BaseTransformer):

    def __init__(self, input_items, factor, output_items):

        self.input_items = input_items
        self.output_items = output_items
        self.factor = float(factor)
        super().__init__()

    def execute(self, df):
        df = df.copy()
        for i,input_item in enumerate(self.input_items):
            df[self.output_items[i]] = df[input_item] * self.factor
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items',
                datatype=float,
                description = "Data items adjust",
                output_item = 'output_items',
                is_output_datatype_derived = True)
                      )
        inputs.append(ui.UISingle(
                name = 'factor',
                datatype=float)
                      )
        outputs = []
        return (inputs,outputs)
