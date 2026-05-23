import pandas as pd
import streamlit as st

from core.blueprint import generate_asset_blueprint, get_game_types
from core.style_profile import build_style_profile, get_style_names


st.set_page_config(
    page_title="GameAsset Forge",
    page_icon="🎮",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 44px;
        font-weight: 800;
        margin-bottom: 8px;
        color: #ffffff;
    }
    .subtitle {
        font-size: 18px;
        color: #C9D1D9;
        line-height: 1.7;
        margin-bottom: 24px;
    }
    .feature-card {
        background: #1F2430;
        padding: 18px 20px;
        border-radius: 16px;
        border: 1px solid #2F3545;
        min-height: 120px;
    }
    .feature-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #ffffff;
    }
    .feature-desc {
        color: #B8C0CC;
        font-size: 14px;
        line-height: 1.6;
    }
    .section-label {
        font-size: 26px;
        font-weight: 800;
        margin-top: 24px;
        margin-bottom: 12px;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #FF4B4B, #FF7A59);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.25rem;
        font-weight: 700;
        font-size: 16px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #FF6B6B, #FF8A65);
        color: white;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🎮 GameAsset Forge</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="subtitle">
    面向学生团队和独立开发者的 2D 游戏素材生成工作台。<br>
    从“AI 绘图”升级为“AI 游戏素材工作流”：先理解游戏需求，再生成素材蓝图、锁定风格，并为后续 Prompt 编排和素材导出打基础。
    </div>
    """,
    unsafe_allow_html=True
)

card1, card2, card3 = st.columns(3)

with card1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Asset Blueprint</div>
            <div class="feature-desc">根据游戏类型自动推荐角色、敌人、道具、地图块和 UI 等基础素材，帮助用户快速明确 Demo 所需资源。</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with card2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Style Lock</div>
            <div class="feature-desc">统一控制画风、尺寸、视角、背景和色彩主题，降低 AI 生成素材风格不一致的问题。</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with card3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Game-aware Prompt</div>
            <div class="feature-desc">后续将根据素材用途自动生成更符合 2D 游戏开发场景的专业 Prompt，而不是简单拼接用户输入。</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown('<div class="section-label">Step 1：项目配置</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    project_name = st.text_input("游戏名称", value="森林冒险")
    game_types = get_game_types()
    game_type = st.selectbox("游戏类型", game_types, index=0 if game_types else None)
    theme = st.text_input("游戏主题", value="森林、魔法、冒险")

with col2:
    style_names = get_style_names()
    style_name = st.selectbox("美术风格", style_names, index=0 if style_names else None)
    size = st.selectbox("素材尺寸", ["32x32", "64x64", "128x128", "256x256"], index=1)
    view = st.selectbox("游戏视角", ["俯视角", "侧视角", "等距视角", "正面"], index=0)

background = st.radio("背景要求", ["透明背景", "简单背景"], horizontal=True)
color_theme = st.selectbox("色彩主题", ["森林绿", "冰雪蓝", "暗黑紫", "沙漠黄", "科幻霓虹"], index=0)

st.divider()

generate_clicked = st.button("生成素材蓝图与风格档案")

if generate_clicked:
    asset_blueprint = generate_asset_blueprint(game_type)
    style_profile = build_style_profile(
        style_name=style_name,
        size=size,
        view=view,
        background=background,
        color_theme=color_theme
    )

    st.session_state["project_config"] = {
        "project_name": project_name,
        "game_type": game_type,
        "theme": theme
    }
    st.session_state["asset_blueprint"] = asset_blueprint
    st.session_state["style_profile"] = style_profile

if "project_config" in st.session_state:
    st.markdown('<div class="section-label">Step 2：项目配置结果</div>', unsafe_allow_html=True)
    st.json(st.session_state["project_config"], expanded=True)

if "style_profile" in st.session_state:
    st.markdown('<div class="section-label">Step 3：Style Lock 风格档案</div>', unsafe_allow_html=True)
    st.json(st.session_state["style_profile"], expanded=True)

if "asset_blueprint" in st.session_state:
    st.markdown('<div class="section-label">Step 4：Asset Blueprint 素材蓝图</div>', unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state["asset_blueprint"])

    type_map = {
        "character": "角色",
        "enemy": "敌人",
        "item": "道具",
        "tile": "地图块",
        "ui": "UI",
        "background": "背景",
        "other": "其他"
    }

    if "asset_type" in df.columns:
        df["asset_type_zh"] = df["asset_type"].map(type_map).fillna(df["asset_type"])

    display_columns = [
        "asset_id",
        "asset_type_zh",
        "display_name",
        "description_zh",
        "selected",
        "status"
    ]

    available_columns = [col for col in display_columns if col in df.columns]
    st.dataframe(df[available_columns], use_container_width=True, hide_index=True)

    st.success("素材蓝图已生成。后续 PR 将支持素材清单编辑、Prompt 自动生成、Demo/API 生成和素材包导出。")
