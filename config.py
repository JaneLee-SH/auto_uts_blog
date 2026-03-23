import os
# =============== 你的专属账号配置 ===============
PLATFORM_CONFIG = {
    "csdn": {
        "username": "qing_lr",
        "password": os.getenv("CSDN_PASSWORD"),
        "column": {
            "UTS数据传输": "UTS数据传输系统",
            "数据同步": "数据同步",
            "信创": "信创",
            "国产数据库": "国产数据库"
        }
    },
    "juejin": {
        "username": "19121300184",
        "password": os.getenv("JUEJIN_PASSWORD"),
        "column": {
            "UTS数据传输": "UTS数据传输",
            "数据同步": "数据同步",
            "信创": "信创",
            "国产数据库": "国产数据库"
        }
    },
    "zhihu": {
        "username": "18602163799",
        "password": os.getenv("JUEJIN_PASSWORD"),
        "column": {
            "UTS数据传输": "UTS数据传输",
            "数据同步": "数据同步",
            "信创": "信创",
            "国产数据库": "国产数据库"
        }
    }
}

# AI 密钥
AI_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# 标签
TAGS = {
    "UTS数据传输": ["UTS", "数据传输", "中间件", "技术实操"],
    "数据同步": ["数据同步", "实时同步", "UTS", "数据迁移"],
    "信创": ["信创", "国产化", "自主可控", "政策解读"],
    "国产数据库": ["国产数据库", "达梦", "人大金仓", "OceanBase"]
}

# 专栏专属封面
COVER_MAP = {
    "UTS数据传输": "https://picsum.photos/id/1/800/420",
    "数据同步": "https://picsum.photos/id/2/800/420",
    "信创": "https://picsum.photos/id/3/800/420",
    "国产数据库": "https://picsum.photos/id/4/800/420"
}
