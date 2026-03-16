# Copyright 2026 Pengchen Wei
# ... (Apache Header Same as above) ...

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
        self.corpus = existing_corpus # 已公开的内容库

    def check_topic_homogeneity(self, topic: str) -> float:
        """
        创作前：主题同质化核查
        :return: 基础重复度百分比 (0.0 - 1.0)
        """
        # 基础算法：简单的关键词匹配，不涉及精准溯源
        count = 0
        for item in self.corpus:
            if topic.lower() in item['content'].lower():
                count += 1
        
        ratio = count / len(self.corpus) if self.corpus else 0.0
        return ratio

    def realtime_check(self, current_text: str) -> list:
        """
        创作中：实时查重
        :return: 风险片段列表
        """
        risks = []
        # 基础算法：检查是否有完全重复的句子片段
        sentences = current_text.split('.')
        for sentence in sentences:
            if len(sentence) > 10: # 忽略短句
                for item in self.corpus:
                    if sentence in item['content']:
                        risks.append({"snippet": sentence, "type": "exact_match"})
        return risks

    def post_creation_validate(self, final_text: str) -> dict:
        """
        创作后：基础校验
        """
        report = {
            "compliance": True,
            "risks": [],
            "sensitive_words": [] # 仅基于公开通用词库
        }
        
        # 模拟敏感词检查（非核心复杂算法）
        common_sensitive = ["forbidden_word_1", "forbidden_word_2"] 
        for word in common_sensitive:
            if word in final_text:
                report['sensitive_words'].append(word)
                report['compliance'] = False
                
        return report

# 注意：本模块不包含“三重指纹防控”核心算法。
# 开发者可优化查重规则灵敏度，但不得试图复现未开源的核心防侵权逻辑。
