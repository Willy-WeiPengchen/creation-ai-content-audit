# config.py
# 路径配置与核心参数设置

import os
from pathlib import Path

class Config:
    """基础配置类"""
    # 项目基础信息
    PROJECT_NAME = "IP-Guard-Lite"  # 知产卫士基础版
    VERSION = "0.1.0"
    DESCRIPTION = "高知创作原创性确权与保护工具"
    
    # 路径配置 (使用Path对象，兼容Windows/Linux/Mac)
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"
    LOG_DIR = BASE_DIR / "logs"
    OUTPUT_DIR = BASE_DIR / "output"
    
    # 确保必要的目录存在
    @classmethod
    def init_app(cls):
        """初始化创建目录"""
        for folder in [cls.DATA_DIR, cls.LOG_DIR, cls.OUTPUT_DIR]:
            folder.mkdir(parents=True, exist_ok=True)

    # 安全配置 (建议生产环境使用环境变量)
    # 这是一个演示用的密钥，实际部署请修改为随机字符串
    SECRET_KEY = os.environ.get('SECRET_KEY', 'weilaoshi_ip_guard_secret_key_2024')

    # 数据库配置 (轻量级SQLite，方便开源版分发和单机使用)
    # 如果未来对接SaaS平台，可切换为MySQL/PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f'sqlite:///{cls.DATA_DIR}/ip_guard.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- 核心算法配置 ---
    
    # 用于文本指纹的哈希算法 (SHA-256 安全性高)
    HASH_ALGORITHM = 'sha256' 
    
    # 文本切片大小 (字符数)，用于细粒度比对和确权
    # 500字适合一般段落，可根据创作类型调整
    CHUNK_SIZE = 500 
    
    # --- 扩展接口配置 (为未来SaaS化预留) ---
    
    # 存证配置 (预留接口，未来对接区块链或公证处API)
    # 目前设为None，等待您授权的核心功能接入
    BLOCKCHAIN_API_URL = os.environ.get('BLOCKCHAIN_API_URL', None)
    BLOCKCHAIN_API_KEY = os.environ.get('BLOCKCHAIN_API_KEY', None)

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    LOG_LEVEL = 'INFO'
    # 生产环境建议强制从环境变量读取敏感信息
    # SECRET_KEY = os.environ.get('SECRET_KEY') 

# 配置映射字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# 快速获取当前配置
def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
