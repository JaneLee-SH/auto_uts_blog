from config import PLATFORM_CONFIG, AI_API_KEY
from ai_writer import AIWriter
from publisher import AutoPublisher
import os

def run():
    print("=" * 60)
    print(" UTS 自动化博客发布系统 - 终极完整版 ")
    print(" 每天8:00 自动发文 CSDN / 掘金 / 知乎 ")
    print("=" * 60)

    os.makedirs("material", exist_ok=True)
    path = "material/input.txt"

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("UTS客户问题：连接超时怎么解决？")

    with open(path, "r", encoding="utf-8") as f:
        mat = f.read().strip()

    if not mat:
        mat = "UTS客户问题：连接超时怎么解决？"

    # AI 生成
    writer = AIWriter(AI_API_KEY)
    article = writer.write(mat)

    # 发布
    pub = AutoPublisher(PLATFORM_CONFIG)
    pub.publish(article)

    # 清空素材
    with open(path, "w", encoding="utf-8") as f:
        f.write("")

    print("\n🎉 全部发布完成！")

if __name__ == "__main__":
    run()
