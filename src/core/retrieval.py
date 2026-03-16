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
Module 4: Basic Content Retrieval & Classification
Supports basic search and export (CSV/TXT).
Does NOT include "Value Distribution" statistical functions.
"""

class ContentRetriever:
    """
    基础检索与分类管理
    """
    
    def __init__(self, database: list):
        self.db = database

    def search(self, keyword: str, lang: str = None, mark_color: str = None) -> list:
        results = []
        for item in self.db:
            if keyword.lower() in item['content'].lower():
                if lang and item['lang'] != lang:
                    continue
                if mark_color and item.get('property_mark') != mark_color:
                    continue
                results.append(item)
        return results

    def export_csv(self, results: list, filename: str):
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Content Summary', 'Language', 'Property Mark'])
            for item in results:
                writer.writerow([
                    item['id'], 
                    item['content'][:50] + '...', 
                    item['lang'], 
                    item.get('property_mark', 'N/A')
                ])
        print(f"Exported to {filename} successfully.")

# 开发者可扩展：增加更多导出格式，优化检索算法。
# 禁止：不得添加涉及“分润结算”的数据统计功能。
