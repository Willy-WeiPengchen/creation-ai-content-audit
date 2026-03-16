# src/__init__.py
# IP-Guard-Lite 源码包初始化

"""
IP-Guard-Lite: 高知创作原创性确权与保护工具
============================================

本系统提供文本指纹生成、原创性验证、版权确权等核心功能。

核心模块:
    - core: 核心业务逻辑
    - deploy: 部署配置
    - interface: 对外接口

使用示例:
    >>> from src.core import TextProcessor
    >>> from src.core.marking import FingerprintGenerator
"""

__version__ = "0.1.0"
__author__ = "Wei Laoshi Team"

# 初始化时打印版本信息（可选）
def get_version():
    """返回当前版本号"""
    return __version__

# 在包级别暴露常用模块，方便导入
# 例如：from src import core
from . import core
from . import interface
from . import deploy
