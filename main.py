from config import PLATFORM_CONFIG, AI_API_KEY, COVER_MAP
from ai_writer import AIWriter
from publisher import Publisher
import os
import time

def load_queue():
    queue_file = "material/queue.txt"
    if not os.path.exists(queue_file):
        with open(queue_file, "w", encoding="utf-8") as f:
            f.write("UTS连接超时如何排查\n")
    with open(queue_file, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    return lines

def pop_first():
    lines = load_queue()
    if not lines:
        return None
    first = lines[0]
    with open("material/queue.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines[1:]) + "\n")
    return first

def main():
    print("="*60)
    print(" UTS 全自动博客系统｜最终完全版 ")
    print(" 每日早8点发布｜素材队列｜失败重试｜发布历史 ")
    print("="*60)

    os.makedirs("material", exist_ok=True)

    material = pop_first()
    if not material:
        print("📭 素材队列为空，今日不发布")
        return

    print(f"📥 当前素材: {material}")

    writer = AIWriter(AI_API_KEY)
    article = writer.generate_article(material)
    article["cover"] = COVER_MAP.get(article["column"], COVER_MAP["UTS数据传输"])

    pub = Publisher(PLATFORM_CONFIG)
    pub.publish_with_retry(article)

    print("\n🎉 今日发布完成，明天8点自动继续")

if __name__ == "__main__":
    main()
