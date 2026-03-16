# src/deploy/__init__.py
# 部署配置包初始化

"""
部署配置模块
============

管理系统的配置参数、环境变量、安全密钥等。

使用示例:
    >>> from src.deploy.config import Config
    >>> config = Config()
    >>> print(config.PROJECT_NAME)
"""

__all__ = ['config']

from . import config

# 自动初始化配置目录（当导入此包时执行）
def ensure_directories():
    """确保必要的目录存在"""
    from .config import Config
    Config.init_app()

# 导入时自动执行（可选）
# ensure_directories()
