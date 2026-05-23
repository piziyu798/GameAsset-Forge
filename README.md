# 🎮 GameAsset-Forge｜2D 游戏素材生成工作台

GameAsset-Forge 是一个面向学生团队、独立开发者和 Game Jam 参赛者的 2D 游戏素材生成工作台。

它不是一个简单的 AI 绘图页面，而是围绕 2D 游戏原型开发流程，提供从“素材需求描述、素材蓝图、风格锁定、Prompt 编排、Demo/API 生成、素材库展示、质量检查到工程化导出”的完整工作流。

---

## 一、项目定位

在早期游戏 Demo 开发中，学生团队和独立开发者经常遇到以下问题：

- 缺少可用的角色、敌人、道具、地图块、UI 和背景素材；
- 普通 AI 绘图工具更偏向单张图片生成，不适合游戏素材包组织；
- AI 生成结果容易出现风格不一致、视角不统一、命名混乱等问题；
- 缺少素材分类、Prompt 记录、质量检查和工程化导出流程；
- 早期 Demo 需要快速验证玩法，但美术资源准备成本较高。

因此，本项目希望从“AI 绘图”升级为“AI 游戏素材工作流”，帮助用户更快获得结构清晰、风格统一、可导出的 2D 游戏素材包。

---

## 二、目标用户

本项目主要面向：

- 学生游戏开发团队；
- 独立游戏开发者；
- Game Jam 参赛者；
- 需要快速制作游戏 Demo 的产品、策划或开发人员；
- 不具备专业美术能力，但需要快速获得可用 2D 素材的用户。

---

## 三、核心功能

### 1. 项目配置

用户可以配置游戏名称、游戏类型、游戏主题、美术风格、素材尺寸、游戏视角、背景要求和色彩主题。

这些参数会作为后续素材蓝图、Style Lock 和 Prompt Composer 的基础约束。

### 2. 素材需求描述

用户可以直接填写希望生成的素材，例如：

    骑士主角、忍者角色、女巫角色、绿色史莱姆、金币、红色药水、草地地图块、森林背景

系统会将用户补充的素材需求与默认素材蓝图合并，形成一份可编辑的素材清单。

### 3. Asset Blueprint 素材蓝图

系统根据游戏类型生成基础素材清单。

例如 RPG 游戏可能包含：

- 主角；
- 敌人；
- 金币；
- 药水；
- 地图块；
- 血条；
- 背景。

用户可以在默认清单基础上继续新增、删除或修改素材。

### 4. Style Lock 风格锁定

为了解决 AI 生成素材风格不一致的问题，本项目设计了 Style Lock 机制。

系统会根据用户选择的：

- 美术风格；
- 素材尺寸；
- 游戏视角；
- 背景要求；
- 色彩主题；

生成统一的风格档案，并将其注入后续 Prompt 生成流程中。

### 5. Game-aware Prompt Composer

系统不会简单地把用户输入直接交给图像生成模型，而是会根据素材类型生成更适合游戏资产生产的 Prompt。

例如：

- 角色素材强调 character sprite、full body、transparent background；
- 敌人素材强调 enemy sprite、recognizable silhouette；
- 道具素材强调 item icon、centered、readable silhouette；
- 地图块强调 tileable、seamless、top-down；
- UI 元素强调 clean UI element、readable shape；
- 背景素材强调 game background、scene composition、layered environment。

### 6. Demo/API 双模式

当前版本支持 Demo Mode 和 API Mode。

#### Demo Mode

Demo Mode 使用内置 36 张程序化示例素材，稳定演示完整产品流程。

它的作用是：

- 不依赖 API Key；
- 不依赖外部网络；
- 保证课堂展示和项目答辩时可稳定运行；
- 展示从素材需求到素材包导出的完整流程。

#### API Mode

API Mode 支持用户配置图像生成 API，根据 Prompt Composer 输出的 Prompt 生成真实 2D 游戏素材。

当前默认配置为：

- API Base URL： https://api.siliconflow.cn/v1
- 默认模型： Tongyi-MAI/Z-Image-Turbo
- 支持输出尺寸：1024x1024、512x512、256x256

API Mode 生成的图片会保存到 outputs/api_generated/，并复用同一套素材库展示、质量检查和 ZIP 导出流程。

系统会根据 API Base URL 自动选择请求参数：

- 硅基流动模式：使用 image_size、batch_size、num_inference_steps、guidance_scale；
- OpenAI 兼容模式：使用 size、n、response_format。

### 7. 素材库展示

生成后的素材会进入素材库，并按照以下类型分类展示：

- 全部；
- 角色；
- 敌人；
- 道具；
- 地图块；
- UI；
- 背景。

每张素材卡片会展示：

- 素材名称；
- 素材类型；
- 生成模式；
- 匹配方式；
- 图片来源；
- 对应 Prompt。

### 8. 质量检查

系统会检查生成素材是否具备基本工程可用性，包括：

- 是否存在素材 ID；
- 是否存在素材类型；
- 是否存在素材名称；
- 是否存在图片路径；
- 图片文件是否存在；
- 是否记录 Prompt；
- 是否存在 Demo 替代匹配情况。

质量检查会输出：

- 素材总数；
- 通过数量；
- 未通过数量；
- 提醒项数量；
- 每个素材的检查详情。

### 9. 工程化导出

系统可以导出结构化素材包：

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

- characters/：角色素材；
- enemies/：敌人素材；
- items/：道具素材；
- tiles/：地图块素材；
- ui/：UI 素材；
- backgrounds/：背景素材；
- manifest.json：素材元数据、Prompt、匹配方式和生成模式；
- README.md：导出素材包说明。

最终用户可以下载 asset_pack.zip。

---

## 四、技术选型

当前 MVP 使用以下技术实现：

- Python：实现核心业务逻辑；
- Streamlit：快速搭建可交互 Web Demo；
- Pillow：程序化生成 Demo 素材；
- requests：调用图像生成 API；
- JSON：维护素材蓝图、风格模板、Prompt 模板和 Demo 素材清单；
- zipfile：导出结构化素材包；
- Prompt Engineering：根据游戏素材类型生成更专业的提示词。

第一版优先保证产品流程完整、功能可演示、代码结构清晰，而不是追求复杂后端系统。

---

## 五、项目结构

    GameAsset-Forge/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── core/
    │   ├── blueprint.py
    │   ├── style_profile.py
    │   ├── prompt_composer.py
    │   ├── asset_generator.py
    │   ├── api_image_generator.py
    │   ├── quality_checker.py
    │   └── exporter.py
    ├── data/
    │   ├── asset_blueprints.json
    │   ├── style_templates.json
    │   ├── prompt_templates.json
    │   └── demo_asset_manifest.json
    ├── assets/
    │   └── demo_samples/
    ├── outputs/
    ├── tools/
    │   └── generate_demo_assets.py
    └── docs/
        ├── product_design.md
        ├── architecture_design.md
        ├── module_plan.md
        └── demo_script.md

---

## 六、运行方式

### 1. 安装依赖

    python3 -m pip install -r requirements.txt

### 2. 生成 Demo 素材

    python3 tools/generate_demo_assets.py

执行后会在 assets/demo_samples/ 下生成 36 张内置 Demo 素材。

### 3. 启动应用

    python3 -m streamlit run app.py

运行后，浏览器会打开 GameAsset-Forge 的本地页面。

---

## 七、演示流程

推荐按照以下步骤演示：

1. 填写项目配置；
2. 填写素材需求描述；
3. 选择 Demo Mode 或 API Mode；
4. 如果选择 API Mode，填写 API Key、API Base URL、模型名称和输出尺寸；
5. 点击“生成素材蓝图与风格档案”；
6. 查看项目配置结果和 Style Lock 风格档案；
7. 编辑素材清单；
8. 点击“生成 Game-aware Prompt”；
9. 查看 Prompt 表格和 Prompt 示例；
10. 点击“生成 Demo 素材”或“生成 API 素材”；
11. 在素材库中按角色、敌人、道具、地图块、UI、背景查看素材；
12. 点击“进行质量检查”；
13. 查看质量检查结果；
14. 点击“导出素材包 ZIP”；
15. 下载并解压 asset_pack.zip；
16. 查看导出的图片、manifest.json 和 README.md。

---

## 八、Demo Mode 与 API Mode 的关系

本项目采用 Demo Mode 和 API Mode 双模式设计。

Demo Mode 用于保证项目可稳定演示，即使没有 API Key，也可以完整跑通素材生成、素材库展示、质量检查和导出流程。

API Mode 用于调用真实图像生成服务，根据 Prompt Composer 输出的 Prompt 生成真实素材，增强项目的 AI 生成能力。

两种模式都会进入同一套后处理流程：

    生成素材
        ↓
    素材库展示
        ↓
    质量检查
        ↓
    ZIP 导出

---

## 九、PR 开发记录

本项目按照模块进行持续开发，避免最后一次性提交。

已完成的 PR 规划如下：

1. PR1：初始化项目结构与基础文档；
2. PR2：新增项目配置、素材蓝图与风格锁定；
3. PR3：新增素材清单编辑与 Prompt Composer；
4. PR4：新增 Demo 素材生成与素材库展示；
5. PR5：新增质量检查与素材包导出；
6. PR6：新增 API Mode 图像生成接入；
7. PR7：完善最终项目文档与 Demo 演示说明。

---

## 十、当前版本能力

当前版本已经实现：

- 项目配置；
- 素材需求描述；
- 默认素材蓝图；
- 素材清单编辑；
- Style Lock 风格档案；
- Game-aware Prompt Composer；
- Demo Mode 素材匹配；
- 36 张内置 Demo 素材；
- API Mode 图像生成；
- 硅基流动 API 参数适配；
- OpenAI 风格参数兼容；
- API 生成素材按类型均衡抽取；
- 素材库分类展示；
- 质量检查；
- asset_pack.zip 导出；
- 导出 manifest.json；
- 导出 README.md。

---

## 十一、后续优化方向

后续可以继续扩展：

- 支持更多图像生成服务商；
- 支持更多游戏类型；
- 支持更多素材类型；
- 增加素材质量评分；
- 增加 Prompt 质量评分；
- 支持素材批量重命名；
- 支持导出 Unity/Godot 友好的目录结构；
- 支持用户上传参考图进行风格约束；
- 支持多轮修改与局部重生成。

---

## 十二、项目亮点

本项目的主要亮点包括：

1. 从“单张 AI 绘图”升级为“游戏素材生成工作流”；
2. 通过 Asset Blueprint 帮助用户规划素材清单；
3. 通过 Style Lock 保持生成风格一致；
4. 通过 Prompt Composer 针对不同游戏素材类型生成专业 Prompt；
5. 通过 Demo Mode 保证无 API Key 情况下也能稳定演示；
6. 通过 API Mode 接入真实图像生成服务；
7. 通过素材库分类展示提高素材管理效率；
8. 通过质量检查和 ZIP 导出增强工程可用性。

---

## 十三、作者

GitHub：@piziyu798
