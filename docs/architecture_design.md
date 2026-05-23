# 技术架构设计文档

## 1. 技术选型

- 前端与交互：Streamlit
- 核心逻辑：Python
- 图片处理：Pillow
- 数据存储：JSON 配置文件
- 可选图像生成：API Provider Adapter
- 导出功能：zipfile
- 文档管理：Markdown

## 2. 项目模块划分

```text
core/
├── blueprint.py          # 素材蓝图生成
├── style_profile.py      # 风格档案与风格锁定
├── prompt_composer.py    # Game-aware Prompt 编排
├── asset_generator.py    # Demo/API 素材生成
├── quality_checker.py    # 质量检查
└── exporter.py           # 素材包导出

---

## 3. 写 `docs/module_plan.md`

```bash
cat > docs/module_plan.md <<'EOF'
# 模块规划文档

## PR 1：初始化项目结构与基础文档

目标：完成项目基础结构和说明文档。

包含内容：

- 创建项目目录结构；
- 添加基础 Streamlit 页面；
- 添加 README；
- 添加 docs 文档骨架；
- 添加 requirements.txt；
- 添加 core/data/assets/outputs 等基础目录。

## PR 2：项目配置、素材蓝图和风格锁定

目标：实现用户输入游戏需求，并根据游戏类型生成基础素材清单。

包含内容：

- 项目配置表单；
- 游戏类型选择；
- 主题与风格参数；
- Asset Blueprint 推荐逻辑；
- Style Profile 风格参数；
- JSON 模板数据。

## PR 3：素材清单编辑与 Prompt Composer

目标：让用户可以编辑素材清单，并自动生成专业 Prompt。

包含内容：

- 中文素材清单展示；
- 素材新增、删除、修改；
- 英文文件名生成；
- Game-aware Prompt Composer；
- Prompt 预览与复制。

## PR 4：Demo/API 生成与素材库展示

目标：实现素材生成结果展示和素材库分类管理。

包含内容：

- Demo Mode；
- API Mode 接口预留；
- 角色、敌人、道具、地图块、UI、背景分类展示；
- 素材卡片；
- Prompt 与素材状态展示。

## PR 5：质量检查、素材包导出和最终文档

目标：完成作品闭环，准备最终提交。

包含内容：

- 质量检查；
- manifest.json 生成；
- zip 素材包导出；
- README 完善；
- Demo 视频脚本；
- 最终提交说明。

## 开发规范

- 每个 PR 聚焦一个核心模块；
- 每个 PR 至少包含 1-2 个有效 commit；
- PR 标题和描述需要说明功能、实现思路和测试方式；
- 避免最后一天一次性提交所有代码。
