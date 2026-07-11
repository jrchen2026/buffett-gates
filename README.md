# buffett-gates

**验金台。** 标的从哪来不管——你自己选的、筛选工具出的、券商研报推的——放上来，只验一件事：**成色配不配下注；下注之后，赌注对不对。**

不筛选（那是投研流水线的活）、不做全流程研究、只验上市公司。输入永远是"已被某人选中的标的"，输出永远是"配不配 + 凭什么 + 什么情况该跑"。

## 为什么不是又一份 checklist

1. **可溯源**：每道闸背后站着具体年份的股东信原文（1986 owner earnings / 1987 市场先生 / 2007 护城河三分法 / 1989 烟蒂降级），非名言级转述
2. **生成器而非清单**：一锚三闸是从伯克希尔股东信 1977–2024 全量原文降秩出的最小生成器，不是清单的重新排列组合；清单答有准备的题，生成器答没见过的题
3. **强制结论**：法眼二选一、三闸不许骑墙、格子决定动作、格子结论必须与建议一致——靠结构逼，不靠原则劝
4. **季检闭环**：快照留下四闸读数 + 退出信号表；持有阶段每季重读仪表，对事实/价格/认知三层报告位移与归因，画四象限轨迹——是体检，不是审判

## 工作时间线

```
投资阶段                                    持有阶段，每季度（季检）
  │                                          │
  ▼                                          ▼
┌──────┐  ┌──────┐  ┌────────────────┐   ┌─────────────────────┐
│ 域检  │─▶│ 法眼  │─▶│ 三闸读数        │   │ 季检                 │
│ 上市? │  │ 好生意 │  │ 锚·竞争·认知·情绪 │─▶│ 三层位移与归因        │
│ 报价? │  │ or    │  │ → 四象限定格    │   │ Δ事实/Δ价格/Δ认知    │
└──────┘  │ 好错价 │  │ → 快照+退出信号 │   │ → 四象限轨迹         │
  域外→出局 └──────┘  └────────────────┘   └─────────────────────┘
            两相皆无→停笔                      无变化 = 好消息
```

## 快速开始

```
# 投资阶段
对 <标的名/代码> 过闸 / 验成色 / 跑 buffett-gates

# 持有阶段（季检）
对 <标的> 跑季检（需已有一份含仪表读数的快照）
```

## 仓库结构

```
skills/buffett-gates/   唯一 skill：投资阶段（域检 → 法眼 → 三闸 → 四象限 → 快照）+ 持有阶段（季检）
  └── references/       一锚三闸降秩全文 + 10 张概念卡（每张含原文引文）
PROTOCOL.md             投资阶段与持有阶段之间的接口规范：仪表读数记录 + 退出信号表
TRACK-RECORD.md         公开判决账本：每次投资阶段/季检落一行，判决对错交给时间检验
scripts/fetch_letters.py  一条命令自建 48 封股东信语料库（语料不入库）
examples/               快照（泡泡玛特）· 域检出局（[已移除标的]）· 法眼停笔（立昂技术）·
                        自校准（苹果，对表巴菲特本人动作）· 外来快照接入（Tempus AI）·
                        季检示例（待 7-25 宁德时代中报后补）
```

## 数据质量说明

数据链的实际精度取决于运行环境，不是玄学：

- 本机装有 akshare 且可调用时，财务数据能拿到结构化一手数据，精度最高
- 仅靠通用网络工具（WebFetch/WebSearch）时：行情类数据（股价、市值）走行情接口/页面直接抓取当前价，不用搜索——搜索引擎索引的是历史资讯，天然搜不到"今天"的价格；财务类数据优先找官方公告的 HTML 摘要版，PDF 附件解析失败率不低，遇到解析失败会换二级来源交叉核对并如实说明，不假装拿到了实际没拿到的精度
- 报告的信息丰富度分级（数据链硬规则第 6 条）就是把这种精度差异如实暴露出来——拿不到的数据，报告里写清楚缺口在哪，不用旧数据或训练知识里的数字顶替

## 安装

将 `skills/buffett-gates/` 目录复制（或软链）到 `~/.claude/skills/` 即可在 Claude Code 中触发。

## English Summary

A Buffett-style assay bench for investment candidates you have already picked (listed companies only). One admission check (worth assaying at all: a cash-machine look, or a mispriced look), three gates traceable to specific shareholder-letter years (anchor / moat / circle-and-margin / Mr. Market), a four-quadrant verdict where the quadrant dictates the action, and a second stage — quarterly review — that reads the displacement of facts, price, and your own judgment against the last snapshot. Conclusions are structurally forced — no fence-sitting allowed.

## License

MIT
