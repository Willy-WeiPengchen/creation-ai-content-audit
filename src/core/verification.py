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
Module 2: Creation Process Basic Verification
Provides basic plagiarism checks and compliance hints.
Does NOT implement the core "Triple-Fingerprint Anti-Infringement" algorithms.
"""

class BasicVerifier:
    """
    创作全流程基础核验模块
    """
    
    def __init__(self, existing_corpus: list):
        self.corpus = existing_corpus

    def check_topic_homogeneity(self, topic: str) -> float:
        count = 0
        for item in self.corpus:
            if topic.lower() in item['content'].lower():
                count += 1
        ratio = count / len(self.corpus) if self.corpus else 0.0
        return ratio

    def realtime_check(self, current_text: str) -> list:
        risks = []
        sentences = current_text.split('.')
        for sentence in sentences:
            if len(sentence) > 10:
                for item in self.corpus:
                    if sentence in item['content']:
                        risks.append({"snippet": sentence, "type": "exact_match"})
        return risks

    def post_creation_validate(self, final_text: str) -> dict:
        report = {
            "compliance": True,
            "risks": [],
            "sensitive_words": []
        }
        common_sensitive = ["forbidden_word_1", "forbidden_word_2"]
        for word in common_sensitive:
            if word in final_text:
                report['sensitive_words'].append(word)
                report['compliance'] = False
        return report

# 注意：本模块不包含“三重指纹防控”核心算法。
# 开发者可优化查重规则灵敏度，但不得试图复现未开源的核心防侵权逻辑。
