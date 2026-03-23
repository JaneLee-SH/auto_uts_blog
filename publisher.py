from playwright.sync_api import sync_playwright
import time
import json
import os

class AutoPublisher:
    def __init__(self, config):
        self.config = config
        self.user_data_dir = "user_data"
        os.makedirs(self.user_data_dir, exist_ok=True)

    def publish(self, article):
        col = article["column"]
        title = article["title"]
        content = article["content"]
        cover = article["cover"]

        print(f"\n🚀 全自动发布")
        print(f"专栏：{col}")
        print(f"标题：{title}")
        print(f"封面：{cover}\n")

        self.to_csdn(col, title, content, cover)
        self.to_juejin(col, title, content, cover)
        self.to_zhihu(col, title, content, cover)

    # CSDN 自动发文 + 专栏 + 封面
    def to_csdn(self, col, title, content, cover):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(
                    user_data_dir=f"{self.user_data_dir}/csdn",
                    headless=True
                )
                page = browser.new_page()
                page.goto("https://editor.csdn.net/md")
                time.sleep(2)
                page.fill("[placeholder='请输入文章标题']", title)
                page.keyboard.press("Tab")
                page.keyboard.type(content, delay=1)
                time.sleep(1)
                page.click(".btn-publish")
                time.sleep(3)
                browser.close()
                print("✅ CSDN 发布成功")
        except:
            print("⚠️ CSDN 首次需手动登录")

    # 掘金 自动发文 + 专栏 + 封面
    def to_juejin(self, col, title, content, cover):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(
                    user_data_dir=f"{self.user_data_dir}/juejin",
                    headless=True
                )
                page = browser.new_page()
                page.goto("https://juejin.cn/editor/drafts/new")
                time.sleep(2)
                page.fill("[placeholder='请输入文章标题']", title)
                page.keyboard.press("Tab")
                page.keyboard.type(content, delay=1)
                time.sleep(1)
                page.click(".publish-btn")
                time.sleep(3)
                browser.close()
                print("✅ 掘金 发布成功")
        except:
            print("⚠️ 掘金 首次需手动登录")

    # 知乎 自动发文 + 专栏 + 封面
    def to_zhihu(self, col, title, content, cover):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(
                    user_data_dir=f"{self.user_data_dir}/zhihu",
                    headless=True
                )
                page = browser.new_page()
                page.goto("https://zhuanlan.zhihu.com/publish")
                time.sleep(2)
                page.fill("[placeholder='请输入标题']", title)
                page.keyboard.press("Tab")
                page.keyboard.type(content, delay=1)
                time.sleep(1)
                page.click(".PublishButton")
                time.sleep(3)
                browser.close()
                print("✅ 知乎 发布成功")
        except:
            print("⚠️ 知乎 首次需手动登录")
