import pandas as pd
import streamlit as st

from core.blueprint import generate_asset_blueprint, get_game_types
from core.asset_generator import generate_demo_assets
from core.prompt_composer import compose_prompts
from core.style_profile import build_style_profile, get_style_names


st.set_page_config(
    page_title="GameAsset Forge",
    page_icon="🎮",
    layout="wide"
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .hero {
        border: 1px solid #2B3142;
        background: #151922;
        border-radius: 18px;
        padding: 28px 32px;
        margin-bottom: 24px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #B8C0CC;
        line-height: 1.7;
        max-width: 900px;
    }

    .tag-row {
        margin-top: 18px;
    }

    .tag {
        display: inline-block;
        border: 1px solid #3A4256;
        border-radius: 999px;
        padding: 6px 12px;
        margin-right: 8px;
        color: #D8DEE9;
        background: #1E2430;
        font-size: 13px;
    }

    .panel-title {
        font-size: 26px;
        font-weight: 800;
        color: #F8FAFC;
        margin-top: 10px;
        margin-bottom: 8px;
    }

    .panel-desc {
        color: #AEB7C4;
        margin-bottom: 18px;
        line-height: 1.6;
    }

    .mini-card {
        border: 1px solid #2B3142;
        background: #151922;
        border-radius: 14px;
        padding: 16px 18px;
        min-height: 108px;
    }

    .mini-card-title {
        color: #F8FAFC;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .mini-card-text {
        color: #AEB7C4;
        font-size: 13px;
        line-height: 1.6;
    }

    div.stButton > button:first-child {
        background: #EF4444;
        color: white;
        border: 1px solid #F87171;
        border-radius: 10px;
        padding: 0.7rem 1.2rem;
        font-weight: 700;
    }

    div.stButton > button:first-child:hover {
        background: #F97316;
        color: white;
        border: 1px solid #FDBA74;
    }

    hr {
        border-color: #2B3142;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🎮 GameAsset Forge</div>
        <div class="hero-subtitle">
            面向学生团队和独立开发者的 2D 游戏素材生成工作台。
            当前 MVP 支持“项目配置 → 素材蓝图 → 清单编辑 → Prompt 编排”，
            为后续 Demo/API 生成和素材包导出提供基础。
        </div>
        <div class="tag-row">
            <span class="tag">Asset Blueprint</span>
            <span class="tag">Style Lock</span>
            <span class="tag">Prompt Composer</span>
            <span class="tag">2D Game Assets</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

card1, card2, card3 = st.columns(3)

with card1:
    st.markdown(
        """
        <div class="mini-card">
            <div class="mini-card-title">素材蓝图</div>
            <div class="mini-card-text">
                根据游戏类型推荐角色、敌人、道具、地图块、UI 和背景等基础素材。
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with card2:
    st.markdown(
        """
        <div class="mini-card">
            <div class="mini-card-title">清单编辑</div>
            <div class="mini-card-text">
                用户可以修改素材名称、类型、描述和是否生成，避免系统清单过于固定。
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with card3:
    st.markdown(
        """
        <div class="mini-card">
            <div class="mini-card-title">Prompt 编排</div>
            <div class="mini-card-text">
                按素材用途自动生成更适合 2D 游戏素材的英文 Prompt。
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown('<div class="panel-title">Step 1：项目配置</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="panel-desc">填写游戏基础信息，系统会据此生成素材蓝图和 Style Lock 风格档案。</div>',
    unsafe_allow_html=True
)

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

generation_mode = st.radio(
    "生成模式",
    ["Demo Mode", "API Mode"],
    horizontal=True,
    help="Demo Mode 使用内置示例素材稳定展示流程；API Mode 用于后续根据 Prompt 调用真实图像生成模型。"
)

if generation_mode == "Demo Mode":
    st.info(
        "当前为 Demo Mode：系统会根据素材名称和类型匹配内置示例素材。"
        "美术风格、尺寸、视角、背景和色彩主题会进入 Style Lock 与 Prompt，"
        "但不会强制改变内置 Demo 图片。若需要图片严格符合这些参数，请使用 API Mode。"
    )
else:
    st.warning(
        "API Mode 需要配置图像生成 API Key。当前版本先保留入口，后续可根据 Prompt 调用真实图像生成模型。"
    )

st.divider()

if st.button("生成素材蓝图与风格档案"):
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
    st.session_state.pop("composed_prompts", None)

if "project_config" in st.session_state:
    st.markdown('<div class="panel-title">Step 2：项目配置结果</div>', unsafe_allow_html=True)
    st.json(st.session_state["project_config"], expanded=False)

if "style_profile" in st.session_state:
    st.markdown('<div class="panel-title">Step 3：Style Lock 风格档案</div>', unsafe_allow_html=True)
    st.json(st.session_state["style_profile"], expanded=False)

if "asset_blueprint" in st.session_state:
    st.markdown('<div class="panel-title">Step 4：素材清单编辑</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="panel-desc">你可以直接修改素材名称、类型、描述和是否生成。后续系统会根据编辑后的清单生成 Prompt。</div>',
        unsafe_allow_html=True
    )

    df = pd.DataFrame(st.session_state["asset_blueprint"])

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        num_rows="dynamic",
        column_config={
            "asset_id": st.column_config.TextColumn("素材 ID", disabled=True),
            "asset_type": st.column_config.SelectboxColumn(
                "素材类型",
                options=["character", "enemy", "item", "tile", "ui", "background", "other"],
                required=True
            ),
            "display_name": st.column_config.TextColumn("素材名称", required=True),
            "description_zh": st.column_config.TextColumn("素材描述"),
            "selected": st.column_config.CheckboxColumn("是否生成"),
            "status": st.column_config.TextColumn("状态")
        }
    )

    st.session_state["asset_blueprint"] = edited_df.to_dict(orient="records")

    st.info(
        "当前为 Prompt Composer 阶段：系统会根据素材类型、素材描述和 Style Lock 风格档案生成英文 Prompt。"
    )

    if st.button("生成 Game-aware Prompt"):
        prompts = compose_prompts(
            st.session_state["asset_blueprint"],
            st.session_state["style_profile"]
        )
        st.session_state["composed_prompts"] = prompts

if "composed_prompts" in st.session_state:
    st.markdown('<div class="panel-title">Step 5：Prompt Composer 结果</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="panel-desc">这些 Prompt 将在后续 PR 中用于 Demo/API 图片生成。</div>',
        unsafe_allow_html=True
    )

    prompt_df = pd.DataFrame(st.session_state["composed_prompts"])
    st.dataframe(prompt_df, use_container_width=True, hide_index=True)

    with st.expander("查看第一条 Prompt 示例"):
        if not prompt_df.empty:
            st.code(prompt_df.iloc[0]["prompt"], language="text")
            st.caption("Negative Prompt")
            st.code(prompt_df.iloc[0]["negative_prompt"], language="text")

    st.info(
        "当前为 Demo Mode：系统会优先根据素材名称和类型匹配内置示例素材；"
        "如果没有完全匹配的图片，会使用同类型素材完成流程演示。"
        "如需生成与描述高度一致的真实图片，可在后续 API Mode 中调用图像生成模型。"
    )

    if st.button("生成 Demo 素材"):
        demo_assets = generate_demo_assets(
            st.session_state.get("asset_blueprint", []),
            st.session_state.get("composed_prompts", [])
        )
        st.session_state["demo_assets"] = demo_assets

if "demo_assets" in st.session_state:
    st.markdown('<div class="panel-title">Step 6：Demo 素材库</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="panel-desc">以下素材由 Demo Mode 根据当前素材清单匹配内置素材池生成，用于稳定展示完整工作流。</div>',
        unsafe_allow_html=True
    )

    demo_assets = st.session_state["demo_assets"]

    type_labels = {
        "all": "全部",
        "character": "角色",
        "enemy": "敌人",
        "item": "道具",
        "tile": "地图块",
        "ui": "UI",
        "background": "背景",
        "other": "其他"
    }

    available_types = ["all", "character", "enemy", "item", "tile", "ui", "background"]
    tabs = st.tabs([type_labels.get(t, t) for t in available_types])

    for tab, asset_type in zip(tabs, available_types):
        with tab:
            if asset_type == "all":
                filtered_assets = demo_assets
            else:
                filtered_assets = [
                    item for item in demo_assets
                    if item.get("asset_type") == asset_type
                ]

            if not filtered_assets:
                st.caption("当前分类暂无素材。")
                continue

            cols = st.columns(3)

            for index, asset in enumerate(filtered_assets):
                with cols[index % 3]:
                    image_path = asset.get("image_path", "")
                    if image_path:
                        st.image(image_path, use_container_width=True)

                    st.markdown(f"**{asset.get('display_name', '未命名素材')}**")
                    st.caption(f"类型：{type_labels.get(asset.get('asset_type'), asset.get('asset_type'))}")
                    st.caption(f"生成模式：{asset.get('generation_mode')}")
                    st.caption(f"匹配方式：{asset.get('match_strategy')}")
                    st.caption(f"Demo 图片：{asset.get('demo_display_name')}")

                    with st.expander("查看 Prompt"):
                        st.code(asset.get("prompt", ""), language="text")
