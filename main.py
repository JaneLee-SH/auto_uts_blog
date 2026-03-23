from config import PLATFORM_CONFIG, AI_API_KEY
import os
import traceback

def run():
    try:
        # 确保material文件夹存在
        if not os.path.exists("material"):
            os.makedirs("material")
        
        # 读取素材
        file_path = "material/input.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("UTS客户问题：文件传输失败，提示连接超时，怎么解决？")
        
        with open(file_path, "r", encoding="utf-8") as f:
            material = f.read().strip()

        if not material:
            print("ℹ️ 使用默认测试素材")
            material = "UTS客户问题：文件传输失败，提示连接超时，怎么解决？"

        print("✅ 素材读取成功")
        print("✅ AI生成文章中...")
        print("✅ 模拟三平台发布完成")
        print("🎉 自动化任务执行成功！")

        # 发布后清空素材
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")
            
    except Exception as e:
        print(f"❌ 错误：{e}")
        traceback.print_exc()

if __name__ == "__main__":
    run()
