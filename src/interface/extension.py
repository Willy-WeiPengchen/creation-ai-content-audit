# Copyright 2026 Pengchen Wei
# ... (Apache Header Same as above) ...

"""
Module 6: Basic Code Extension Interface
Allows developers to extend base classes.
Prohibits bypassing patent protection logic.
"""

from abc import ABC, abstractmethod

# 定义抽象基类，供开发者继承扩展
class BaseIngestionExtension(ABC):
    """
    扩展接口示例：允许开发者自定义内容预处理逻辑
    """
    @abstractmethod
    def preprocess(self, content: str) -> str:
        pass

# 开发者可以在遵守 Apache 2.0 及专利声明的前提下，
# 实现自己的预处理逻辑（例如特定格式的清洗），
# 但不得修改底层架构以绕过专利保护范围。
