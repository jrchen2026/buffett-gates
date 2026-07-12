# 巴菲特语料 Wiki：Schema

> 模式来源：Karpathy 的 LLM Wiki 三层架构（gist 442a6bf5）——原始语料不可变，LLM 维护互链 wiki 做全部记账活，人只做语料筛选。
> 本 wiki 的定位：给 buffett-gates 验金台配的**判例库**。rank.md 是法条（一锚三闸），这里是判例——巴菲特怎么判具体公司。三闸读数、反方砍价时来这里找刻度感。

## 三层

| 层 | 位置 | 规则 |
|---|---|---|
| Raw sources | `corpus/`（gitignore，本地） | 不可变。一期：股东信 48 封（`scripts/fetch_letters.py` 自建）；二期：CNBC 股东会记录 |
| The Wiki | `wiki/`（gitignore，本地，仅本文件入库） | LLM 维护，人不手改正文。含大量原文引用 → 版权原因不入公开库 |
| The Schema | 本文件（入库公开） | 结构、约定、工作流 |

## 目录结构

```
wiki/
  SCHEMA.md               本文件（唯一入库项）
  index.md                目录：每页一行（路径 + 一句话），LLM 每次 ingest 后更新
  log.md                  流水：每次 ingest/query/lint 一行（日期 + 动作 + 触及页面）
  rank-falsification.md   证伪台账：一锚三闸生成不出来的判例候选（见下）
  years/<year>.md         信页：一封信一页
  companies/<slug>.md     判例页（核心产出）：一家公司一页
  concepts/<slug>.md      概念页：对应 skill 的 11 张卡 + 语料中新冒出的概念
  evolution/<slug>.md     演变页：观点随年份的变化轨迹
  people/<slug>.md        人物页：芒格、格雷厄姆、经理人等
```

## 页面约定

- 全部 markdown，互链用相对路径链接（Obsidian 可直接开库浏览）
- 引文必须带年份锚点：`> 原文（1989 信）`——短引文即可，读数依据要能回溯到语料原文
- 每页头部一句话主线；不写的比写的重要——wiki 不是摘要堆，是判断的索引

### 判例页（companies/）模板

```markdown
# <公司>
**一句话主线**：巴菲特对它的判决主线（如"看错了护城河的类型"）

## 判决时间线
| 年份 | 场合 | 判断/动作 | 引文锚点 |

## 闸门映射
哪道闸起了作用、当时的读数逻辑（对着一锚三闸写）

## 结果
对 / 错 / 待定 + 巴菲特自己怎么复盘（他公开认错的原话年份）

## 关联
指向 concepts/ evolution/ people/ 的链接
```

### 信页（years/）模板

```markdown
# <year> 信
**三件事**：这封信最值得记的三点（各一行）

## 判例线索
提到的公司判断 → 指向/新建 companies/ 页

## 概念动向
新概念首次出现 / 旧概念表述变化 → 指向 concepts/ evolution/

## 降秩对表
这封信的内容，一锚三闸盖得住吗？盖不住的записать rank-falsification.md
```

## 工作流

**Ingest（每封信一次）**：读 `corpus/letters/md/<year>.md` → 写 `years/<year>.md` → 创建/更新触及的 companies/concepts/evolution/people 页 → 更新 index.md → log.md 落一行。一封信通常触及 5–15 页。

**Query**：先查 index.md 定位，再读具体页面。有价值的综合发现写回新页（复利）。

**Lint（定期）**：查孤页、断链、index 漏项。**注意与 Karpathy 原版的一处改造**：他说 lint 要查矛盾，但本语料里巴菲特的自我矛盾是特征不是 bug（航空股 1989 骂 → 2016 买 → 2020 割）——矛盾不"修复"，归档成 evolution/ 页。

**证伪测试（rank-falsification.md）**：一锚三闸是从股东信降秩出的最小生成器。每次 ingest 顺手问一句：这封信里有没有四个生成器生成不出来的判断？候选记入台账；积累多了 → rank.md 的秩要修。这是本 wiki 对 skill 最硬的反哺。

## 分期

- **一期（进行中）**：股东信 48 封 ingest。语料一条命令自建，先跑通 schema
- **二期**：CNBC 股东会问答记录（Buffett Archive，1994–）——判例主矿脉，信里从不谈的具体标的临场判断都在这里。瓶颈是 transcript 抓取
- **不进**：CNBC 日常访谈（信噪比低，缓议）、年报 10-K 正文（那是伯克希尔的财务细节，不是判断系统语料）

## 与 buffett-gates 的接口

- skill 保持薄，不依赖 wiki 存在——wiki 是可选外挂
- 三闸读数/反方砍价时**可**引判例：先查 `wiki/index.md`，无 wiki 则跳过
- 语料封闭（巴菲特 2025 年底卸任，股东信收官），ingest 是一次性工程，维护成本趋零
