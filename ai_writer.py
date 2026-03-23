import requests
import time

class AIWriter:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_article(self, material):
        system_prompt = """
你是UTS官方技术博主，专注企业级实操。
文章结构：场景→问题→方案→代码→小结
语言专业、简洁、可直接复制使用。
"""
        user_prompt = f"""
素材：{material}

输出格式严格如下：
【专栏】
【爆款标题】
【正文】markdown
"""
        try:
            resp = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.6
                }
            )
            txt = resp.json()["choices"][0]["message"]["content"]
            column = txt.split("【专栏】")[1].split("\n")[0].strip()
            title = txt.split("【爆款标题】")[1].split("\n")[0].strip()
            content = txt.split("【正文】")[1].strip()
            return {"column": column, "title": title, "content": content}
        except Exception as e:
            print("AI生成异常，使用默认内容")
            return {
                "column": "UTS数据传输",
                "title": f"UTS日常问题解决 {time.strftime('%Y-%m-%d')}",
                "content": "本文记录UTS实际使用中的常见问题与解决方案。"
            }
