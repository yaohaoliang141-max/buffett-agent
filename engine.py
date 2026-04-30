import os
import json
import requests
from loguru import logger
from prompts import BUFFETT_SYSTEM_PROMPT

class BuffettEngine:
    def __init__(self, api_key=None):
        # 读取或传入 DeepSeek API Key
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        self.base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        if not self.api_key:
            raise ValueError("未检测到 API Key，请在侧边栏输入。")
        # DeepSeek 完全兼容 OpenAI 接口，使用 /v1/chat/completions
        self.endpoint = f"{self.base_url}/v1/chat/completions"
        logger.info(f"BuffettEngine 初始化，endpoint={self.endpoint}")

    def _post(self, payload, stream=False):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(self.endpoint, headers=headers, json=payload, stream=stream, timeout=60)
            response.raise_for_status()
            return response
        except Exception as e:
            logger.error(f"DeepSeek 调用失败: {e}")
            raise

    def analyze(self, company_info, financial_data):
        """返回完整的文字点评（非流式）"""
        user_content = f"""
请根据以下公司信息和财务数据，以沃伦·巴菲特的口吻给出投资评价。请务必体现巴菲特的价值投资理念（护城河、安全边际、长期持有等），并使用幽默且简洁的语言。

【公司业务简述】
{company_info}

【核心财务指标】
{json.dumps(financial_data, ensure_ascii=False, indent=2)}
"""
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": BUFFETT_SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ],
            "temperature": 0.7,
            "stream": False,
        }
        resp = self._post(payload)
        # 返回文本内容
        result = resp.json()
        # OpenAI‑compatible response结构
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        return "（未得到有效回复）"

if __name__ == "__main__":
    # 简单测试
    engine = BuffettEngine(api_key="your_key_here")
    demo = engine.analyze("示例公司", {"市盈率": 15, "ROE": 0.12})
    print(demo)
