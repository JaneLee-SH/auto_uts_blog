import requests

class AIWriter:
    def __init__(self, api_key):
        self.api_key = api_key

    def write(self, material):
        prompt = f"""
素材：{material}
你是UTS官方技术博主，写企业级实操文章。
要求：
1. 一个问题一篇文章
2. 结构：标题 + 场景 + 问题 + 解决方案 + 代码 + 总结
3. 生成爆款标题
4. 自动归类专栏
输出格式：
【专栏】
【标题】
【内容】Markdown
"""
        try:
            resp = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": "专业技术博主"},
                        {"role": "user", "content": prompt}
                    ]
                }
            )
            t = resp.json()["choices"][0]["message"]["content"]
            col = t.split("【专栏】")[1].split("\n")[0].strip()
            title = t.split("【标题】")[1].split("\n")[0].strip()
            content = t.split("【内容】")[1].strip()
        except:
            col = "UTS数据传输"
            title = "UTS传输超时 1分钟解决"
            content = "# UTS问题解决\n\n问题：连接超时\n解决：检查端口、防火墙"

        cover_url = "https://picsum.photos/800/400"
        return {"column": col, "title": title, "content": content, "cover": cover_url}
