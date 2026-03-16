# Copyright 2026 Pengchen Wei
# ... (Apache Header Same as above) ...

"""
Module 3: Basic Property Marking & Risk Hint
Uses Red/Yellow/Green system.
Does NOT include "Copyright Tracing" or "Infringement Warning" core capabilities.
"""

class PropertyMarker:
    """
    基础产权标记系统
    """
    
    # 标记常量
    GREEN = "PUBLIC_DOMAIN"    # 绿色：公域内容
    YELLOW = "UNCLEAR_STATUS"  # 黄色：疑似私有
    RED = "PRIVATE_PROPERTY"   # 红色：私有产权

    def mark_content(self, content_record: dict, property_status: str) -> dict:
        """
        对内容进行标记
        :param property_status: GREEN, YELLOW, or RED
        """
        if property_status not in [self.GREEN, self.YELLOW, self.RED]:
            raise ValueError("Invalid marking color/status.")
            
        content_record['property_mark'] = property_status
        content_record['risk_hint'] = self._generate_hint(property_status)
        return content_record

    def _generate_hint(self, status: str) -> str:
        """
        生成基础文字提示
        """
        hints = {
            self.GREEN: "Public domain content. Free to use.",
            self.YELLOW: "Unclear property status. Use with caution.",
            self.RED: "Private property. Unauthorized use prohibited."
        }
        return hints.get(status, "")

# 功能限制说明：
# 本模块仅提供标记存储与提示，不具备自动溯源侵权人等核心能力。
