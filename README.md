# 世界观编年史生成系统 (WorldView Chronicle Generator)

> 🎭 自动化的故事世界观构建与编年史生成工具 —— 从设定到史诗，四步完成宏大世界观的深度构建。

[![Skill](https://img.shields.io/badge/Skill-WorldViewChronicle-blue)]()
[![Platform](https://img.shields.io/badge/Platform-AgentUniversal-green)]()
[![License](https://img.shields.io/badge/License-MIT-orange)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-brightergreen)]()

## 简介

**世界观编年史生成系统** 是一款通用型智能体技能（Agent Skill），能够根据用户指定的世界观类型与时间跨度，自动构建完整的故事世界观并生成万字级编年史文档。

本技能通过**四阶段流水线**架构，将世界观构建分解为可执行的递进流程，每个阶段产出独立的 Markdown 文件，最终整合为一部结构完整、细节丰富的编年史巨著。

**平台无关性：** 本技能不依赖任何特定平台、API 或外部服务。可在任何具备基本文件 I/O 能力的智能体环境中运行（如 WorkBuddy、CodeBuddy、自定义 Agent 等）。

## 核心特性

- **交互式引导** — 通过对话引导用户明确世界观类型、时间跨度和核心主题
- **模块化流水线** — 四个核心模块依次执行，每个模块产出独立文件
- **中间确认机制** — 每个模块完成后可预览和调整，确保方向正确
- **十六维度社会描绘** — 每个时期节点覆盖社会面貌的全部维度
- **万字级输出** — 默认生成约十万字（中文）/ 五万字英文，支持自定义字数
- **有机整合** — 三大素材文件融合为有机叙事，非简单拼接
- **平台无关** — 纯文本生成 + 文件 I/O，无外部依赖

## 四大核心模块

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  ① 世界观构建  →  ② 关键情节  →  ③ 社会面貌  →  ④ 编年史整合  │
│                                                     │
│   [world.md]       [plots.md]      [society.md]    [chronicle.md]  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 模块一：世界观构建

交互式收集用户输入，生成世界观核心设定与关键时间节点时间轴。

- 支持类型：奇幻、科幻、历史架空、末世、都市幻想、玄幻、武侠、蒸汽朋克、赛博朋克、神话重构等
- 生成至少 8-12 个关键时间节点
- 输出文件：`world.md`

### 模块二：关键情节生成

为时间轴每个节点生成详细叙事内容。

- 500-800 字完整事件经过
- 2-4 个核心角色（姓名、身份、动机、关键行动）
- 转折点分析与历史余波
- 输出文件：`plots.md`

### 模块三：社会面貌描绘

为各时期节点生成全景式社会描述，覆盖**十六个维度**：

| 维度 | 描述要点 |
|------|---------|
| 政治格局 | 政体、权力结构、统治势力、法律体系 |
| 人口族群结构 | 种族/族群分布、族群关系、聚居与迁徙 |
| 经济商贸 | 经济形态、产业、贸易网络、货币体系 |
| 科技发展 | 技术水平、技术创新、知识传承 |
| 文艺文化 | 文学/艺术形式、审美范式、文化认同 |
| 阶层关系 | 阶层划分、流动性、权力关系与矛盾 |
| 民众日常生活 | 衣食住行、劳作模式、休闲方式 |
| 婚恋家庭习俗 | 婚姻形式、家庭结构、性别权力 |
| 信仰民俗 | 信仰体系、宗教仪式、民间习俗 |
| 主流思想思潮 | 哲学/伦理体系、思想流派、核心价值观 |
| 大众集体心理 | 社会情绪、集体恐惧与梦想、身份认同 |
| 治安秩序 | 治安状况、执法体系、私力与公力救济 |
| 信息传播方式 | 信息载体、传播网络、信息控制 |
| 生存风险 | 天灾人祸、超自然威胁、防护机制 |
| 时代审美 | 美学范式、装饰文化、建筑美学 |
| 生态自然 | 环境生态、资源循环、人与自然关系 |

- 输出文件：`society.md`

### 模块四：编年史整合输出

以三大素材文件为锚点，整合为完整编年史文档。

- 默认约十万字（中文）/ 五万字（英文），支持自定义字数
- 史诗体/纪实体/传记体可选
- 章节按时间节点自然划分
- 输出文件：`chronicle.md`

## 使用方法

### 安装

将技能目录复制到任意 Agent 技能目录即可：

```bash
# 示例：用户级技能目录
cp -r worldview-chronicle-generator ~/.agent/skills/
cp -r worldview-chronicle-generator ~/.codebuddy/skills/
cp -r worldview-chronicle-generator ~/.workbuddy/skills/
```

**要求：** 运行环境需具备基本文件读写能力，无需外部 API、数据库或网络服务。

### 触发方式

以下任一关键词即可触发本技能：

- 中文：世界观构建、编年史生成、世界观设计、世界观文档、构建世界观、世界观框架
- English: worldview building, chronicle generation, world design, worldbuilding, story worldview, lore creation

### 工作流程

```
1. 对话触发技能
      ↓
2. 交互输入：世界观类型 / 时间跨度 / 核心主题
      ↓
3. 模块一执行 → world.md → 【确认/调整】
      ↓
4. 模块二执行 → plots.md → 【确认/调整】
      ↓
5. 模块三执行 → society.md → 【确认/调整】
      ↓
6. 模块四执行 → chronicle.md（默认约10万字）
```

### 风格控制指令

| 指令 | 效果 |
|------|------|
| `更史诗感` / `more epic` | 增加宏大叙事和英雄悲歌元素 |
| `更纪实感` / `more documentary` | 增强史料考证和田野调查风格 |
| `更文学性` / `more literary` | 增强心理描写和场景刻画 |
| `调整时期侧重` / `emphasize [era]` | 对特定时期增加或减少篇幅 |
| `字数XXXXX` / `length XXXXX` | 指定目标字数 |

## 项目文件结构

```
WorldViewGenerator/
├── README.md                              # 项目说明（本文件）
├── LICENSE                                # MIT 许可证
├── .gitignore                             # Git 忽略规则
│
├── worldview-chronicle-generator/         # 技能核心目录
│   ├── SKILL.md                           # 技能主文件（入口）
│   │
│   ├── scripts/                           # 辅助脚本
│   │   └── validate.py                    # 项目验证与字数统计工具
│   │
│   └── references/                        # 参考文档
│       └── 社会面貌维度指南.md              # 十六维度详细描述指南（中英双语）
│
└── examples/                              # 示例目录
    └── README.md                          # 示例说明
```

## 输出文件结构

使用技能后，项目目录中将生成以下文件：

```
project-directory/
├── world.md         # 模块一输出：主体框架与时间轴
├── plots.md         # 模块二输出：各节点叙事内容
├── society.md       # 模块三输出：十六维度社会全景
└── chronicle.md     # 模块四输出：整合后的完整编年史
```

## 使用示例

### 触发示例（中文）

**用户输入：**
> "帮我构建一个奇幻世界观，时间跨度三千年，核心主题是诸神黄昏后的文明重建"

**系统响应流程：**

1. 询问确认世界观设定偏好
2. 生成 `world.md`（含时间轴）
3. 展示框架摘要，确认方向
4. 生成 `plots.md`（8-12个关键事件）
5. 展示前两个情节预览，确认风格
6. 生成 `society.md`（各时期十六维度全景）
7. 展示一个时期预览，确认深度
8. 生成 `chronicle.md`（约十万字）

### 触发示例（English）

**User input:**
> "Build me a sci-fi worldview, 500-year timeline, core theme: post-singularity human-AI coexistence"

**System response flow:**

1. Confirm world type and setting preferences
2. Generate `world.md` (with timeline)
3. Show framework summary, confirm direction
4. Generate `plots.md` (8-12 key events)
5. Preview first two plots, confirm style
6. Generate `society.md` (16-dimension portraits for each era)
7. Preview one era, confirm depth
8. Generate `chronicle.md` (~50,000 words)

## 技术架构

| 组件 | 说明 |
|------|------|
| **运行平台** | 通用（任何 Agent 环境） |
| **技能格式** | SKILL.md + 资源文件（YAML 前置元数据） |
| **输出格式** | Markdown (.md) — 平台无关 |
| **依赖要求** | 无（仅需基本文件 I/O） |
| **辅助脚本** | Python 3.x（项目结构验证、字数统计） |
| **参考文档** | 十六维度社会面貌描绘指南（中英双语） |

## 为什么选择 Agent 通用技能？

| 特性 | WorkBuddy 专用技能 | Agent 通用技能 |
|------|-------------------|-------------|
| 平台依赖 | 绑定特定平台 | 跨任何 Agent 运行环境 |
| 安装方式 | 复制到平台特定目录 | 复制到任意技能目录 |
| 触发机制 | 平台内置匹配 | 关键词匹配 / 描述匹配 |
| 文件操作 | 依赖平台工具 | 标准文件 I/O |
| 可移植性 | 低 | 高 |
| 共享复用 | 限于平台生态 | 跨团队 / 跨项目 |

## 版本与许可

- **当前版本：** v1.0.0
- **许可证：** [MIT](LICENSE)
- **适用平台：** 任何具备文件 I/O 能力的智能体环境

## 贡献与反馈

本技能由 AI 智能体自动构建。如有改进建议或问题反馈，欢迎提交修改。

---

<p align="center">
  <em>🌌 从一粒种子到参天大树 —— 让每一个故事世界都拥有自己的历史。</em><br/>
  <em>From a single seed to a towering tree — every story world deserves its own history.</em>
</p>
