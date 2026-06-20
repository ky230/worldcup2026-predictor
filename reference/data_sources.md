# 官方赛程与实时名单参考数据源 (Reference Data Sources)

为保证赛事预测与首发战术板的权威性和准确性，以下是我们在日常开发与预测过程中频繁查阅的官方及权威数据源。无论是人类手动更新还是其他 AI 接续工作，请首先参考这些网站。

---

## 🥇 赛程、对阵与裁判安排

### [FIFA 官方 2026 世界杯赛程中心](https://www.fifa.com/en/tournaments/mens/worldcup/2026/match-schedule)
* **用途**：赛程时间权威基准、比赛球馆与城市分配、裁判指派安排、分组实时积分榜。
* **说明**：国际足联（FIFA）最权威的官方大厅。

---

## 🥈 实时首发阵容与首发预测

### [FotMob 世界杯数据中心](https://www.fotmob.com)
* **用途**：获取实时首发阵容（Lineups）、战术阵型（Formation）、球员球衣号码，以及各大媒体在赛前发布的“预计首发”（Expected Lineups）。
* **说明**：更新极为迅速的足球比分与阵容软件。

### [Sofascore 实时比分与伤停](https://www.sofascore.com)
* **用途**：赛前 1 小时左右获取各队官报的 Team Sheet 首发/替补名单，查询球员近期状态评分及两队历史对决的深度统计。

---

## 🥉 突发伤停与动态新闻

### [Google Search / News 谷歌突发新闻聚合](https://news.google.com)
* **用途**：实时检索突发情报。例如：
  * **伤病与变动**：搜索 `"[球队/球员名] World Cup 2026 injury news"` 验证如远藤航等核心球员是否因伤临时退出大名单。
  * **教练变动**：搜索国家队换帅新闻。
* **搜索格式建议**：`[球队A] vs [球队B] 2026 World Cup lineups` 或 `[国家队名] roster changes`。

---

## 🌤️ 环境与天气信息

### [AccuWeather 国际气象网](https://www.accuweather.com)
* **用途**：查询北美各承办场馆城市在开球时间点的气温、湿度、体感温度以及降雨/雪概率。
* **说明**：用于预测极其闷热天气或雨战对球队体能、防守容错率和地面传控效率的影响。

---

## 📰 战术前瞻与更衣室背景

### [The Athletic](https://theathletic.com) / [BBC Sport](https://www.bbc.com/sport) / [Sky Sports](https://www.skysports.com)
* **用途**：深度阅读跟队记者的独家爆料、主帅赛前发布会言论、战术细节前瞻、更衣室心态和历史对决背景（如国家怨恨、战意强弱）。
* **说明**：提供丰富的新闻语料，帮助撰写极具说服力的 AI 预测分析。

---

## 📋 赛前首发名单预排规范 (沿用首轮与伤停排查)

在官方首发公布之前（通常为赛前 1.5 小时以上），为了确保战术板的客观严谨，必须严格按照以下流程进行名单预排：

### 1. 强制沿用第一轮真实首发
由于无法随意揣测教练变阵，在赛前预排阶段，**必须直接复制该队第一轮（上一场）的官方实际首发阵容与球衣号码**作为战术板的底版。
* **FotMob 历史首发查找路径**：访问 FotMob -> 世界杯赛程 -> 找到上一轮该队的比赛 -> 切换至 **Lineups** 标签页。
* **第一轮关键比赛 FotMob 直达链接备份 (Group F)**：
  * 🇯🇵 vs 🇳🇱 **荷兰 vs 日本**：[https://www.fotmob.com/matches/netherlands-vs-japan/1hn72b](https://www.fotmob.com/matches/netherlands-vs-japan/1hn72b)
  * 🇹🇳 vs 🇸🇪 **突尼斯 vs 瑞典**：[https://www.fotmob.com/matches/tunisia-vs-sweden/1x5290](https://www.fotmob.com/matches/tunisia-vs-sweden/1x5290)

### 2. 伤停与红黄牌停赛排查（高优先级核对项）
在克隆第一轮首发后，必须对这 11 名主力进行伤停与红牌排查：
* **红牌/黄牌停赛**：
  * 在 **Sofascore** 或官方战报中核对该球员首轮是否吃到红牌或累积黄牌触发停赛（如南非队的 Zwane 与 Sithole 因首战红牌而在 06-18 停赛）。
* **伤病与退队动态**：
  * 必须利用 **Google News** 检索 `"[国家队/球员名] injury news World Cup 2026"`，获取最新的伤病退赛情报（如日本队远藤航因伤退赛、久保建英次轮伤停）。
* **可视化标注规范**：
  * **保留节点**：伤停/停赛的主力球员依旧绘制在战术板的对应首发位置上。
  * **文字标注**：在球员名字后追加 **`(伤停)`** 或 **`(停赛)`**。
  * **圆圈样式**：将球员圆圈的 CSS 样式修改为 **`background:#555555; color:#888888; border:1px solid #ff4444;`**（灰色底色，红色边框），在战术板中进行强视觉警示。
