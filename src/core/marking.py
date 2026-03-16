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
Module 3: Basic Property Marking & Risk Hint
Uses Red/Yellow/Green system.
Does NOT include "Copyright Tracing" or "Infringement Warning" core capabilities.
"""

class PropertyMarker:
    """
    基础产权标记系统
    """
    
    GREEN = "PUBLIC_DOMAIN"
    YELLOW = "UNCLEAR_STATUS"
    RED = "PRIVATE_PROPERTY"

    def mark_content(self, content_record: dict, property_status: str) -> dict:
        if property_status not in [self.GREEN, self.YELLOW, self.RED]:
            raise ValueError("Invalid marking color/status.")
        content_record['property_mark'] = property_status
        content_record['risk_hint'] = self._generate_hint(property_status)
        return content_record

    def _generate_hint(self, status: str) -> str:
        hints = {
            self.GREEN: "Public domain content. Free to use.",
            self.YELLOW: "Unclear property status. Use with caution.",
            self.RED: "Private property. Unauthorized use prohibited."
        }
        return hints.get(status, "")

# 功能限制说明：
# 本模块仅提供标记存储与提示，不具备自动溯源侵权人等核心能力。
