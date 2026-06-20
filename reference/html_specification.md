# 2026 世界杯 AI 预测引擎 · HTML 生成规范

本文档是生成比赛日预测页面（`index.html`）的完整 HTML 与 CSS 样式规范。每次创建新的比赛日面板时，可直接参考此文档及配套的空模板进行生成与组装。

---

## 一、项目目录结构

```
/Users/ky230/Desktop/FF2026/
├── index.html                  ← 主控制台（比赛日卡片入口列表）
├── 2026-06-18/index.html       ← 比赛日面板
├── 2026-06-19/index.html
├── 2026-06-20/index.html
├── 2026-06-XX/index.html       ← 新比赛日目录
└── reference/
    ├── html_specification.md   ← 本文档
    ├── match_day_template.html ← 空白比赛日模板
    └── data_sources.md         ← 数据源规范
```

---

## 二、创建新比赛日的完整流程

1. **创建目录**：`/Users/ky230/Desktop/FF2026/2026-06-XX/`
2. **复制并重命名模板**：复制 `reference/match_day_template.html` 为 `2026-06-XX/index.html`。
3. **编辑内容**：修改页面标题和日期徽章，并填入当日所有的 `match-card` 卡片。
4. **更新主控台**：在根目录 `/Users/ky230/Desktop/FF2026/index.html` 的 `<div class="grid">` 中追加指向新比赛日的卡片入口。

---

## 三、CSS 设计系统（Glassmorphism 视觉规范）

```css
:root {
    --bg-color: #0b0c10;
    --card-bg: rgba(255, 255, 255, 0.03);
    --card-hover-bg: rgba(255, 255, 255, 0.06);
    --primary-color: #00ff66;          /* 绿色高亮 */
    --primary-glow: rgba(0, 255, 102, 0.1);
    --text-main: #f5f6f9;
    --text-muted: #8b949e;
    --border-color: rgba(255, 255, 255, 0.08);
    --accent-color: #38bdf8;           /* 蓝色辅助 */
    --accent-glow: rgba(56, 189, 248, 0.1);
}
```

---

## 四、单场比赛卡片结构（match-card）

每张 `match-card` 按以下顺序包含以下模块：
```html
<div class="match-card">
    ① match-meta        → 小组标签 + 开球时间
    ② match-vs          → 主队名(主) VS 客队名（含国旗 emoji）
    ③ match-info-banner  → 3 列环境信息（场地/天气/场馆类型）
    ④ squad-info-section → 大名单关键人物 + 伤停情报
    ⑤ match-details      → details-grid 两栏：
       ├─ detail-pane 1: 战术板 (soccer-pitch)
       └─ detail-pane 2: AI 预测报告
</div>
```

### 4.1 战术板 (soccer-pitch) 球员节点定位规则
战术板是一个 `position: relative` 的 380px 高容器，主客队分别从左右两侧排阵，球员通过 `left` / `top` 百分比定位：

#### 主队（从左到右进攻）：
* 门将 (GK)：`left: 6%`
* 后卫线 (DEF)：`left: 18%–24%`
* 中场线 (MID)：`left: 28%–34%`
* 前锋线 (FWD)：`left: 38%–45%`

#### 客队（从右到左进攻）：
* 门将 (GK)：`left: 94%`
* 后卫线 (DEF)：`left: 76%–84%`
* 中场线 (MID)：`left: 66%–74%`
* 前锋线 (FWD)：`left: 56%–62%`

#### top 分布规则（纵向）：
* 单人：50%
* 双人：35%, 65%
* 三人：25%, 50%, 75% 或 30%, 50%, 70%
* 四人：15%, 40%, 60%, 85%
* 五人：10%, 30%, 50%, 70%, 90%

> **关键注意**：球员节点的 `top` 值要错开至少 15%，防止名字牌重叠。同一条横线上的球员如果纵向间距小于 15%，需要在 `left` 方向也做 2%–4% 的错开。

#### 🚫 严防「上下颠倒/镜像」排阵错误（核心避坑指南）
由于主客队进攻方向相反，绝对不能想当然地认为“所有左路位置都在上方，右路都在下方”。必须严格遵循以下纵向（top）坐标对应逻辑：
* **主队（从左向右进攻，面向右侧）**：
  * **左翼/左路**（如左后卫 LB、左边锋 LW、偏左中场 LCM）：对应屏幕 **上方**（`top` 较小，如 15%, 20%, 35%）。
  * **右翼/右路**（如右后卫 RB、右边锋 RW、偏右中场 RCM）：对应屏幕 **下方**（`top` 较大，如 85%, 80%, 65%）。
* **客队（从右向左进攻，面向左侧）**：
  * **右翼/右路**（如右后卫 RB、右边锋 RW、偏右中场 RCM）：对应屏幕 **上方**（`top` 较小，如 15%, 20%, 35%）。
  * **左翼/左路**（如左后卫 LB、左边锋 LW、偏左中场 LCM）：对应屏幕 **下方**（`top` 较大，如 85%, 80%, 65%）。

**核对金标准**：比对 FotMob 上的示意图。在 FotMob 水平赛场图中，**最顶部的球员总是主队的左路和客队的右路**。如果生成的代码中客队左路（例如 LB）被放在了顶部，说明已经犯了镜像错误！

#### 球员节点 HTML 格式：
```html
<div class="player-node" style="left: XX%; top: YY%;">
    <div class="player-circle" style="background:#颜色; color:#字色; border:1px solid #边框色;">号码</div>
    <div class="player-name">中文姓名</div>
</div>
```
球员圆圈颜色应使用该队球衣的主色调，客队使用深色系区分。对于黄牌在身但照常上场的球员，名字后追加 **`🟨`**。
如果确认因伤病或停赛无法上场，在战术板中**必须保留该球员节点**，名字后缀改为 `(伤停)` 或 `(停赛)`，且圆圈圆点施加灰色底色及红色边框（`background:#555555; color:#888888; border:1px solid #ff4444;`）。

### 4.2 AI 预测报告面板 (detail-pane 2) 结构
```
pane-title: "🤖 AI 赛事预测报告 (智能分析)"

① prob-container     → 胜/平/负概率条（prob-bar + prob-labels）
② section-sub-title   → "让球指数预测 (让球方 ±N)"
   recommendation-tag → 首选 + 次选
③ section-sub-title   → "波胆/比分倾向"
   score-tags         → 稳胆 X-X + 防冷 X-X（score-badge / score-badge.upset）
④ section-sub-title   → "核心战术要点"
   factor-list        → 3条战术分析要点（< 50 字/条）
⑤ prediction-detail-text → 解说倾向（100–200字口语化专业分析）
```

---

## 五、主控台卡片模板（index.html）

在根目录 `/Users/ky230/Desktop/FF2026/index.html` 的 `<div class="grid">` 中追加：
```html
<a href="2026-06-XX/index.html" class="card">
    <div class="card-header">
        <span class="date-badge">2026-06-XX / YY</span>
        <span class="status-badge status-active">未开始</span>
    </div>
    <div class="card-body">
        <h3>小组赛第N轮 - XY组阶段</h3>
        <p>将进行N场重要对战：[比赛列表及时间]。包含首发名单、天气、场馆及AI预测报告。</p>
    </div>
    <div class="card-footer">
        进入比赛日面板
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
    </div>
</a>
```
