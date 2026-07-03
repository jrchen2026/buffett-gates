# buffett-gates

**验金台。** 标的从哪来不管——你自己选的、筛选工具出的、券商研报推的——放上来，只验一件事：**成色配不配下注；下注之后，赌注对不对。**

不筛选（那是投研流水线的活）、不做全流程研究、只验上市公司。输入永远是"已被某人选中的标的"，输出永远是"配不配 + 凭什么 + 什么情况该跑"。

## 为什么不是又一份 checklist

1. **可溯源**：每道闸背后站着具体年份的股东信原文（1986 owner earnings / 1987 市场先生 / 2007 护城河三分法 / 1989 烟蒂降级），非名言级转述
2. **生成器而非清单**：一锚三闸是从伯克希尔股东信 1977–2024 全量原文降秩出的最小生成器——市面上的六关/十条 checklist 都能从这四根推出来；清单答有准备的题，生成器答没见过的题
3. **强制结论**：法眼二选一、三闸不许骑墙、格子决定动作、格子结论必须与建议一致——靠结构逼，不靠原则劝
4. **季检闭环**：快照留下四闸读数 + 退出信号表；gates-review 每季重读仪表，对事实/价格/认知三层报告位移与归因，画四象限轨迹——是体检，不是审判

## 工作时间线

```
下注前                                    持有后（每季度）
  │                                          │
  ▼                                          ▼
┌──────┐  ┌──────┐  ┌────────────────┐   ┌─────────────────────┐
│ 域检  │─▶│ 法眼  │─▶│ 三闸读数        │   │ gates-review 季检    │
│ 上市? │  │ 好生意 │  │ 锚·竞争·认知·情绪 │─▶│ 三层位移与归因        │
│ 报价? │  │ or    │  │ → 四象限定格    │   │ Δ事实/Δ价格/Δ认知    │
└──────┘  │ 好错价 │  │ → 快照+退出信号 │   │ → 四象限轨迹         │
  域外→出局 └──────┘  └────────────────┘   └─────────────────────┘
            两相皆无→停笔                      无变化 = 好消息
```

## 快速开始

```
# 独立验金（A 模式）
对 <标的名/代码> 过闸 / 验成色 / 跑 buffett-gates

# 复核验金（B 模式）
对这份研报做巴菲特检验：<粘贴或指向既有分析>

# 季检
对 <标的> 跑季检（需已有一份含仪表读数的快照）
```

## 仓库结构

```
skills/buffett-gates/   主 skill：域检 → 法眼 → 三闸 → 四象限 → 快照
  └── references/       一锚三闸降秩全文 + 10 张概念卡（每张含原文引文）
skills/gates-review/    配套 skill：季检（三层位移与归因）
PROTOCOL.md             两 skill 唯一接口：仪表读数记录 + 退出信号表
scripts/fetch_letters.py  一条命令自建 48 封股东信语料库（语料不入库）
examples/               快照示例 + 域检出局示例 + 季检示例
```

## 安装

将 `skills/` 下两个目录复制（或软链）到 `~/.claude/skills/` 即可在 Claude Code 中触发。

## English Summary

A Buffett-style assay bench for investment candidates you have already picked (listed companies only). One admission check (worth assaying at all: a cash-machine look, or a mispriced look), three gates traceable to specific shareholder-letter years (anchor / moat / circle-and-margin / Mr. Market), a four-quadrant verdict where the quadrant dictates the action, and a quarterly companion skill that reads the displacement of facts, price, and your own judgment against the last snapshot. Conclusions are structurally forced — no fence-sitting allowed.

## License

MIT
