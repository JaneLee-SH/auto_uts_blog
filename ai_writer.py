import requests

class AITechWriter:
    def __init__(self, api_key):
        self.api_key = api_key
        # 你的专属写作风格：UTS技术博主 专业干货
        self.system_prompt = """
你是【UTS数据传输系统】官方技术博主，文风专业、精炼、实操。
只写技术干货，专注4大领域：
1. UTS数据传输 2. 数据同步 3. 信创 4. 国产数据库

文章规则：
- 每次只解决1个小问题，短小精悍
- 结构固定：标题 → 场景 → 问题 → 解决方案 → 代码 → 验证 → 总结
- 代码块格式化，可直接复制运行
- 专业、严谨、企业级实操风格
- 自动归类到4大专栏
- 输出纯Markdown，无多余内容
"""

    def generate_article(self, material):
        prompt = f"""
素材：{material}
生成技术博客，输出格式严格如下：
【专栏】UTS数据传输/数据同步/信创/国产数据库
【标题】实操型短句标题
【内容】Markdown正文
"""
        # 调用AI生成（已适配主流大模型）
        resp = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ]
            }
        )
        content = resp.json()["choices"][0]["message"]["content"]
        
        # 解析文章
        column = content.split("【专栏】")[1].split("\n")[0].strip()
        title = content.split("【标题】")[1].split("\n")[0].strip()
        article = content.split("【内容】")[1].strip()
        return {"column": column, "title": title, "content": article}
