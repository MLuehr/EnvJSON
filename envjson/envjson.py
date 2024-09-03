__version__ = "0.1.0"

import io
import os
import re

import json

class EnvJSON:
    __version__ = __version__

    def __init__(
        self,
        json_file=None,
        strict=True,
        **kwargs
    ):
        """Create EnvJSON class instance and read content from environment and files if they exists

        :param str json_file: file path for config or env.yaml by default
        :param bool strict: use strict mode and throw exception when have unset variable, by default true
        :param dict kwargs: additional environment variables keys and values
        :return: new instance of EnvJSON
        """

        # read environment
        self.__cfg = dict(os.environ)

        # set strict mode to false if "ENVYAML_STRICT_DISABLE" presents in env else use "strict" from function
        self.__strict = strict

        self.__json_file = json_file
        data = self.__read_json()
        data = self.__process_json(data)

    def __read_json(self)->dict:
        with open(self.__json_file) as json_file:
            file_contents = json_file.read()
            return json.loads(file_contents)

    def __process_json(self, data: dict) -> dict:
        for key, value in data.items():
            print(f"{key}: {value}")
            
        return data
