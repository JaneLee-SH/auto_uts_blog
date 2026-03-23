from config import PLATFORM_CONFIG, AI_API_KEY
from ai_writer import AITechWriter
from publisher import BlogPublisher

def run():
    # 1. 读取你丢的素材
    with open("material/input.txt", "r", encoding="utf-8") as f:
        material = f.read().strip()
    
    if not material:
        print("❌ 未找到素材，请在 material/input.txt 中放入内容")
        return

    # 2. AI生成专业技术文章
    writer = AITechWriter(AI_API_KEY)
    article = writer.generate_article(material)

    # 3. 三平台自动发布
    publisher = BlogPublisher(PLATFORM_CONFIG)
    publisher.publish(article)

    # 4. 清空素材，等待下一篇
    with open("material/input.txt", "w", encoding="utf-8") as f:
        f.write("")

if __name__ == "__main__":
    run()
