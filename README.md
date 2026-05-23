# 🎮 GameAsset-Forge｜2D 游戏素材生成工作台

面向学生团队与独立开发者的 2D 游戏素材生成工作台。

---

## 一、项目简介

GameAsset Forge 不是一个简单的 AI 绘图页面，而是一个面向 2D 游戏原型开发流程的素材生成工作台。

本项目希望解决学生团队、独立开发者和 Game Jam 参赛者在早期游戏 Demo 开发中遇到的素材生产问题，包括：

- 缺少美术资源；
- 素材风格不统一；
- 不知道一个游戏 Demo 需要哪些基础素材；
- 普通 AI 绘图工具只生成单张图片，难以形成完整素材包；
- 生成素材缺少命名、分类、质量检查和工程化导出流程。

因此，本项目的核心目标是：

> 从“AI 绘图”升级为“AI 游戏素材工作流”，帮助用户快速生成风格一致、结构清晰、可导出的 2D 游戏素材包。

---

## 二、目标用户

本项目主要面向：

- 学生游戏开发团队；
- 独立游戏开发者；
- Game Jam 参赛者；
- 需要快速制作游戏 Demo 的产品、策划或开发人员；
- 不具备专业美术能力，但需要快速获得可用 2D 素材的用户。

---

## 三、核心功能规划

### 1. 项目配置模块

用户可以输入或选择游戏名称、游戏类型、游戏主题、美术风格、素材尺寸、游戏视角和背景要求。

这些信息会作为后续素材生成、Prompt 编排和风格锁定的基础。

### 2. Asset Blueprint 素材蓝图

系统根据游戏类型和主题，自动推荐一组基础素材清单。

例如 RPG 游戏可能推荐：

- 主角；
- 敌人；
- 金币；
- 药水；
- 地图块；
- 血条；
- 开始按钮。

用户可以在推荐清单基础上继续新增、删除或修改素材。

### 3. Style Lock 风格锁定

为了解决 AI 生成素材风格不一致的问题，本项目设计 Style Lock 机制。

用户可以统一设置像素风、卡通风、暗黑风、俯视角、侧视角、透明背景、色彩主题和描边风格。

这些风格参数会被统一注入到每个素材的 Prompt 中。

### 4. Game-aware Prompt Composer

系统不会简单地把用户输入直接交给图像生成模型，而是会根据素材用途自动生成更专业的 Prompt。

例如：

- 角色素材强调 character sprite、full body、transparent background；
- 道具素材强调 item icon、centered、readable silhouette；
- 地图块强调 tileable、seamless、top-down；
- UI 元素强调 clean UI element、readable shape。

### 5. Demo/API 双模式

本项目计划支持两种生成模式：

- Demo Mode：无需 API Key，使用内置示例素材或占位图演示完整流程；
- API Mode：配置 API Key 后调用图像生成 API，根据系统生成的 Prompt 生成真实素材。

### 6. 素材库分类展示

生成后的素材会进入素材库，并按照角色、敌人、道具、地图块、UI、背景等类型分类展示。

用户可以查看素材名称、素材类型、生成 Prompt 和生成状态，便于后续管理与复用。

### 7. 质量检查

系统会检查素材命名、分类、Prompt 记录和导出结构，判断素材包是否具备基本工程可用性。

质量检查的目标不是评价图片艺术水平，而是判断素材是否能够被游戏项目继续使用。

### 8. 工程化导出

最终用户可以导出结构化素材包，示例结构如下：

    asset_pack/
    ├── characters/
    ├── enemies/
    ├── items/
    ├── tiles/
    ├── ui/
    ├── backgrounds/
    ├── manifest.json
    └── README.md

其中：

- 图片文件用于游戏项目；
- manifest.json 记录素材名称、类型、Prompt、尺寸等元数据；
- README.md 提供素材包导入和使用说明。

---

## 四、项目结构

项目当前目录结构如下：

    GameAsset-Forge/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── core/
    │   ├── blueprint.py
    │   ├── style_profile.py
    │   ├── prompt_composer.py
    │   ├── asset_generator.py
    │   ├── quality_checker.py
    │   └── exporter.py
    ├── data/
    │   ├── asset_blueprints.json
    │   ├── style_templates.json
    │   └── prompt_templates.json
    ├── assets/
    │   └── demo_samples/
    ├── outputs/
    └── docs/
        ├── product_design.md
        ├── architecture_design.md
        ├── module_plan.md
        └── demo_script.md

---

## 五、技术选型

当前计划使用以下技术完成第一版 MVP：

- Python：实现核心业务逻辑；
- Streamlit：快速搭建可交互的 Web Demo；
- Pillow：进行基础图片处理；
- JSON 配置文件：存储素材蓝图、风格模板和 Prompt 模板；
- Prompt Engineering：根据游戏素材类型生成更专业的提示词；
- 可选图像生成 API：后续用于接入真实 AI 生图能力；
- zipfile：用于导出游戏工程友好的素材包。

第一版优先保证产品流程完整、功能可演示、代码结构清晰，而不是追求复杂后端系统。

---

## 六、运行方式

安装依赖：

    python3 -m pip install -r requirements.txt

启动应用：

    python3 -m streamlit run app.py

运行后，浏览器会打开 GameAsset Forge 的本地页面。

---

## 七、文档目录

项目文档位于：

    docs/product_design.md
    docs/architecture_design.md
    docs/module_plan.md
    docs/demo_script.md

其中：

- product_design.md：说明产品定位、目标用户、用户痛点和功能范围；
- architecture_design.md：说明技术选型、模块划分和核心流程；
- module_plan.md：说明 PR 拆分计划和模块开发安排；
- demo_script.md：用于后续录制 Demo 视频时讲解产品功能。

---

## 八、开发记录要求

本项目按照议题要求进行持续开发，开发周期内会保持连续的 commit 和 Pull Request 记录。

计划 PR：

1. 初始化项目结构与基础文档；
2. 新增项目配置、素材蓝图和风格锁定；
3. 新增素材清单编辑与 Prompt Composer；
4. 新增 Demo/API 生成与素材库展示；
5. 新增质量检查、素材包导出和最终文档。

每个 PR 会尽量围绕一个独立模块展开，避免最后一次性提交全部代码。

---

## 九、当前进度

- [x] 创建 GitHub 仓库；
- [x] 初始化项目目录结构；
- [x] 添加基础 Streamlit 页面；
- [x] 添加 requirements.txt；
- [x] 添加 core、data、docs、assets、outputs 等基础目录；
- [x] 添加项目文档骨架；
- [ ] 实现项目配置模块；
- [ ] 实现素材蓝图模块；
- [ ] 实现风格锁定模块；
- [ ] 实现 Prompt Composer；
- [ ] 实现 Demo/API 生成模式；
- [ ] 实现素材库分类展示；
- [ ] 实现质量检查与导出功能。

---

## 十、作者

GitHub：@piziyu798