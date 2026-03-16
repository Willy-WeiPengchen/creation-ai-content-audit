# src/interface/__init__.py
# 对外接口包初始化

"""
对外接口模块
============

提供对外的API接口、扩展功能、第三方集成等。

    - extension: 扩展接口，包含SaaS API、区块链存证等预留接口
"""

__all__ = ['extension']

from . import extension

# 接口版本号
API_VERSION = "v1.0"

def get_api_status():
    """获取API状态（预留）"""
    return {
        'status': 'running',
        'version': API_VERSION,
        'message': 'IP-Guard-Lite 接口服务就绪'
    }
