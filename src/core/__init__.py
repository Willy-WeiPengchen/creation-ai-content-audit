# src/core/__init__.py
# 核心业务逻辑包初始化

"""
核心功能模块
============

包含文本确权系统的四大核心组件：

    - ingestion: 文本采集与预处理
    - marking: 指纹生成与标记（核心算法）
    - retrieval: 相似内容检索
    - verification: 原创性验证与确权
"""

# 模块级别的文档说明
__all__ = [
    'ingestion',
    'marking', 
    'retrieval',
    'verification'
]

# 导入各子模块，使其可以通过 from src.core import xxx 访问
from . import ingestion
from . import marking
from . import retrieval
from . import verification

# 版本标识
CORE_VERSION = "0.1.0"

# 包级别的工具函数（预留）
def init_core_system():
    """初始化核心系统组件"""
    print(f"[Core System] 初始化完成，版本: {CORE_VERSION}")
    # 未来可以在这里加载模型、初始化数据库连接等
    pass
