import streamlit as st

st.set_page_config(
    page_title="GameAsset Forge",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 GameAsset Forge")
st.subheader("面向学生团队和独立开发者的 2D 游戏素材生成工作台")

st.markdown("""
GameAsset Forge 不是一个简单的 AI 绘图页面，而是围绕 2D 游戏原型开发流程设计的素材生成工作台。

核心流程：

1. 输入游戏需求与简单参数
2. 生成可编辑的素材清单
3. 使用 Style Lock 保持风格一致
4. 通过 Game-aware Prompt Composer 生成专业提示词
5. 使用 Demo/API 双模式生成素材
6. 按类型管理素材库
7. 进行质量检查
8. 导出游戏工程友好的素材包
""")

st.info("当前版本为项目初始化页面，后续 PR 将逐步实现素材蓝图、Prompt 编排、素材生成、质量检查和导出功能。")
