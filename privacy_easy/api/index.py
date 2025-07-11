from fastapi import FastAPI
from pydantic import BaseModel

# 创建应用
app = FastAPI(title="简单隐私过滤器测试")

# 请求模型
class TestRequest(BaseModel):
    message: str

# 响应模型
class TestResponse(BaseModel):
    original: str
    filtered: str
    success: bool

@app.get("/")
def root():
    return {
        "status": "运行正常",
        "message": "简单隐私过滤器测试版本",
        "version": "0.1.0"
    }

@app.post("/test")
def test_filter(request: TestRequest):
    """最简单的过滤测试"""
    original_text = request.message
    
    # 简单替换：爸爸、妈妈 -> 家人
    filtered_text = original_text.replace("爸爸", "家人").replace("妈妈", "家人")
    
    return TestResponse(
        original=original_text,
        filtered=filtered_text,
        success=True
    )

# Vercel 需要的处理器
handler = app