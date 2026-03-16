# Copyright 2026 Pengchen Wei
# ... (Apache Header Same as above) ...

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
        """
        基础检索功能
        支持按语种、标记颜色、关键词筛选
        """
        results = []
        for item in self.db:
            # 关键词匹配
            if keyword.lower() in item['content'].lower():
                # 语种筛选
                if lang and item['lang'] != lang:
                    continue
                # 标记颜色筛选
                if mark_color and item.get('property_mark') != mark_color:
                    continue
                results.append(item)
        return results

    def export_csv(self, results: list, filename: str):
        """
        导出为 CSV 格式
        """
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
