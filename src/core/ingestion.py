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
Module 1: Basic Multilingual Content Ingestion Interface
Focuses on basic content ingestion, classification, and format validation.
Does NOT include intelligent rights attribution or identity binding.
"""

import datetime  # ← 新增导入

class ContentIngestor:
    """
    基础多语种内容收录接口
    """
    
    SUPPORTED_LANGUAGES = ['zh', 'en', 'ja', 'ko']
    SUPPORTED_TYPES = ['text', 'image', 'short_video']

    def __init__(self):
        self.database = []

    def ingest_single(self, content: str, lang: str, content_type: str, source: str) -> dict:
        if not content or not content.strip():
            raise ValueError("Content cannot be empty.")
        
        if lang not in self.SUPPORTED_LANGUAGES:
            print(f"Warning: Language '{lang}' not in default support list. Extensible interface available.")
        
        record = {
            "id": len(self.database) + 1,
            "content": self._sanitize(content),
            "lang": lang,
            "type": content_type,
            "source": source,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z"  # ← 修正为动态时间戳
        }
        self.database.append(record)
        return record

    def ingest_batch(self, content_list: list) -> list:
        results = []
        for item in content_list:
            try:
                results.append(self.ingest_single(**item))
            except ValueError as e:
                print(f"Skipping invalid item: {e}")
        return results

    def _sanitize(self, text: str) -> str:
        return text.strip()

# 开发者可扩展接口示例：
# 开发者可继承此类以增加更多语种适配或自定义分类标签
# 但不得扩展至未开源的“智能确权”身份绑定功能。
