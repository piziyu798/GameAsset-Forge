# GameAsset-Forge 架构设计说明

## 一、整体架构

GameAsset-Forge 当前采用轻量级本地 Web Demo 架构：

    Streamlit 前端页面
            ↓
    项目配置 / 素材需求描述
            ↓
    Asset Blueprint
            ↓
    Style Lock
            ↓
    Prompt Composer
            ↓
    Demo Asset Generator / API Image Generator
            ↓
    Gallery / Quality Checker / Exporter

该架构适合 MVP 快速验证，后续可以扩展为前后端分离或接入更多图像生成服务。

---

## 二、模块划分

### 1. app.py

负责 Streamlit 页面展示和用户交互，包括：

- 项目配置表单；
- 素材需求描述输入；
- Demo/API Mode 选择；
- API Key、API Base URL、模型名称和输出尺寸配置；
- 素材清单编辑；
- Prompt 展示；
- 素材库展示；
- 质量检查；
- 素材包导出下载。

### 2. core/blueprint.py

负责根据游戏类型生成默认素材蓝图。

输入：

    game_type

输出：

    asset_blueprint

### 3. core/style_profile.py

负责根据用户选择的风格、尺寸、视角、背景和色彩主题生成 Style Lock 风格档案。

### 4. core/prompt_composer.py

负责根据素材类型和 Style Lock 生成 Game-aware Prompt。

### 5. core/asset_generator.py

负责在 Demo Mode 下匹配内置素材池。

匹配策略：

1. 精准匹配；
2. 同类型替代；
3. 全局替代。

### 6. core/api_image_generator.py

负责在 API Mode 下调用图像生成服务。

核心能力：

- 配置 API Key；
- 配置 API Base URL；
- 配置模型名称；
- 配置输出尺寸；
- 根据 Base URL 自动选择硅基流动参数或 OpenAI 风格参数；
- 支持解析 images[].url、data[].url 和 data[].b64_json；
- 下载或保存生成图片；
- 输出与 Demo Mode 兼容的素材记录。

### 7. core/quality_checker.py

负责检查素材是否具备基本工程可用性，包括字段完整性、图片路径和 Prompt 记录。

### 8. core/exporter.py

负责将素材复制到结构化目录，并生成：

- manifest.json；
- README.md；
- asset_pack.zip。

### 9. tools/generate_demo_assets.py

负责使用 Pillow 程序化生成 36 张 Demo 素材。

---

## 三、数据文件设计

### 1. data/asset_blueprints.json

维护不同游戏类型的默认素材清单。

### 2. data/style_templates.json

维护不同美术风格对应的风格描述。

### 3. data/prompt_templates.json

维护不同素材类型对应的 Prompt 模板。

### 4. data/demo_asset_manifest.json

维护 Demo 素材的路径、类型、显示名称和关键词。

---

## 四、核心数据流

    用户输入项目配置
            ↓
    生成默认素材蓝图
            ↓
    合并素材需求描述中的补充素材
            ↓
    用户编辑素材清单
            ↓
    生成 Style Lock
            ↓
    生成 Game-aware Prompt
            ↓
    Demo Mode 或 API Mode 生成素材
            ↓
    展示素材库
            ↓
    质量检查
            ↓
    导出 ZIP

---

## 五、Demo Mode 与 API Mode

### Demo Mode

Demo Mode 使用内置示例素材池，保证在无 API Key、无网络或无额度的情况下也可以完整演示流程。

优点：

- 稳定；
- 可复现；
- 不依赖外部 API；
- 适合课堂展示和答辩。

限制：

- 图片不一定严格符合全部参数；
- 美术质量不是商用级。

### API Mode

API Mode 调用真实图像生成服务，根据 Prompt Composer 输出的 Prompt 生成图片。

当前默认配置：

- API Base URL： https://api.siliconflow.cn/v1
- 默认模型： Tongyi-MAI/Z-Image-Turbo
- 输出目录： outputs/api_generated/

API Mode 支持两类参数格式：

硅基流动模式：

    image_size
    batch_size
    num_inference_steps
    guidance_scale

OpenAI 兼容模式：

    size
    n
    response_format

两种模式生成的素材都会进入同一套 Gallery、Quality Checker 和 Exporter 流程。

---

## 六、导出结构

导出结果为：

    asset_pack/
    ├── characters/
    ├── enemies/
    ├── items/
    ├── tiles/
    ├── ui/
    ├── backgrounds/
    ├── manifest.json
    └── README.md

其中 manifest.json 记录素材元数据、Prompt、匹配方式和生成模式。
