# Copyright 2026 Pengchen Wei
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module 6: Basic Code Extension Interface
Allows developers to extend base classes.
Prohibits bypassing patent protection logic.
"""

from abc import ABC, abstractmethod

class BaseIngestionExtension(ABC):
    """
    扩展接口示例：允许开发者自定义内容预处理逻辑
    """
    @abstractmethod
    def preprocess(self, content: str) -> str:
        pass
