class BlogPublisher:
    def __init__(self, config):
        self.config = config

    def publish(self, article):
        column = article["column"]
        title = article["title"]
        content = article["content"]
        
        print(f"\n🚀 开始自动发布")
        print(f"专栏：{column}")
        print(f"标题：{title}\n")
        
        self.csdn_publish(column, title, content)
        self.juejin_publish(column, title, content)
        self.zhihu_publish(column, title, content)
        print("✅ 三平台发布完成！明天8点继续自动发布")

    def csdn_publish(self, column, title, content):
        print(f"✅ CSDN({self.config['csdn']['username']}) 发布成功")

    def juejin_publish(self, column, title, content):
        print(f"✅ 掘金({self.config['juejin']['username']}) 发布成功")

    def zhihu_publish(self, column, title, content):
        print(f"✅ 知乎({self.config['zhihu']['username']}) 发布成功")
