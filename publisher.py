from playwright.sync_api import sync_playwright
import time
import os
import json

class Publisher:
    def __init__(self, cfg):
        self.cfg = cfg
        self.user_dir = "user_data"
        self.history_file = "publish_history.json"
        os.makedirs(self.user_dir, exist_ok=True)

    def load_history(self):
        if not os.path.exists(self.history_file):
            return []
        with open(self.history_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_history(self, article):
        history = self.load_history()
        history.append({
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "title": article["title"],
            "column": article["column"]
        })
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def publish_with_retry(self, article, max_retry=2):
        for i in range(max_retry+1):
            try:
                self.publish(article)
                self.save_history(article)
                print("✅ 发布成功并记录历史")
                return
            except Exception as e:
                print(f"⚠️ 第{i+1}次失败: {e}")
                time.sleep(10)
        print("❌ 达到最大重试次数")

    def publish(self, article):
        print(f"\n🚀 发布: {article['title']}")
        self.csdn(article)
        self.juejin(article)
        self.zhihu(article)

    def csdn(self, article):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(f"{self.user_dir}/csdn", headless=True)
                page = browser.new_page()
                page.goto("https://editor.csdn.net/md", timeout=60000)
                time.sleep(2)
                page.fill("[placeholder='请输入文章标题']", article["title"])
                time.sleep(1)
                page.keyboard.press("Tab")
                page.keyboard.insert_text(article["content"])
                time.sleep(2)
                page.click(".btn-publish")
                time.sleep(3)
                browser.close()
                print("✅ CSDN 发布成功")
        except:
            print("⚠️ CSDN 需手动登录一次")

    def juejin(self, article):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(f"{self.user_dir}/juejin", headless=True)
                page = browser.new_page()
                page.goto("https://juejin.cn/editor/drafts/new", timeout=60000)
                time.sleep(2)
                page.fill("[placeholder='请输入文章标题']", article["title"])
                time.sleep(1)
                page.keyboard.press("Tab")
                page.keyboard.insert_text(article["content"])
                time.sleep(2)
                page.click(".publish-btn")
                time.sleep(3)
                browser.close()
                print("✅ 掘金 发布成功")
        except:
            print("⚠️ 掘金 需手动登录一次")

    def zhihu(self, article):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(f"{self.user_dir}/zhihu", headless=True)
                page = browser.new_page()
                page.goto("https://zhuanlan.zhihu.com/publish", timeout=60000)
                time.sleep(2)
                page.fill("[placeholder='请输入标题']", article["title"])
                time.sleep(1)
                page.keyboard.press("Tab")
                page.keyboard.insert_text(article["content"])
                time.sleep(2)
                page.click(".PublishButton")
                time.sleep(3)
                browser.close()
                print("✅ 知乎 发布成功")
        except:
            print("⚠️ 知乎 需手动登录一次")
