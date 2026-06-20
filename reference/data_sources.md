# 官方赛程与实时名单参考数据源 (Reference Data Sources)

为保证赛事预测与首发战术板的权威性和准确性，以下是我们在日常开发与预测过程中频繁查阅的权威数据源。无论是人类手动更新还是其他 AI 接续工作，请**以 FotMob 作为主要参考数据源**。

---

## 🥇 赛程、对阵与裁判安排

### [FIFA 官方 2026 世界杯赛程中心](https://www.fifa.com/en/tournaments/mens/worldcup/2026/match-schedule)
* **用途**：赛程时间权威基准、比赛球馆与城市分配、裁判指派安排、分组实时积分榜。
* **说明**：国际足联（FIFA）最权威的官方大厅。

---

## 🥈 实时首发阵容与首发预测 (主参考 FotMob)

### [FotMob 世界杯数据中心](https://www.fotmob.com)
* **主专栏 (Overview)**: [https://www.fotmob.com/leagues/77/overview/world-cup](https://www.fotmob.com/leagues/77/overview/world-cup) —— 包含所有详细信息、积分榜及深度数据统计。
* **分组信息及目前局势**: [https://www.fotmob.com/leagues/77/table/world-cup?filter=all](https://www.fotmob.com/leagues/77/table/world-cup?filter=all) —— 全方位对阵积分榜与形势分析。
* **赛程淘汰赛表 (Playoff)**: [https://www.fotmob.com/leagues/77/playoff/world-cup](https://www.fotmob.com/leagues/77/playoff/world-cup) —— 实时更新的淘汰赛晋级树状图。
* **赛程按日期 (Fixtures by Date)**:
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date)
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=1](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=1)
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=2](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=2)
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=3](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=3) (对于较后天的比赛，若在page 2找不到，向后翻页即可找到)
* **球员统计数据**: [https://www.fotmob.com/leagues/77/stats/world-cup/players](https://www.fotmob.com/leagues/77/stats/world-cup/players)
* **球队统计数据**: [https://www.fotmob.com/leagues/77/stats/world-cup/teams](https://www.fotmob.com/leagues/77/stats/world-cup/teams)
* **用途**：获取精确到每一天的世界杯赛事列表，并进入单场比赛页面查看实时首发阵容 (Lineups)、战术阵型 (Formation)、球员号码、裁判、天气，以及赛前预计首发。

### [Sofascore 实时比分与伤停](https://www.sofascore.com)
* **用途**：赛前 1 小时左右获取各队官报的 Team Sheet 首发/替补名单，查询球员近期状态评分及两队历史对决的深度统计。

---

## 🥉 突发伤停与动态新闻

### [FotMob 赛事新闻](https://www.fotmob.com/leagues/77/news/world-cup)
* **用途**：作为第一优先级的战术前瞻与更衣室背景参考，包含球队大名单变动、集训新闻等。

### [Google Search / News 谷歌突发新闻聚合](https://news.google.com)
* **用途**：辅助检索，例如搜索 `"[球队/球员名] World Cup 2026 injury news"` 验证如远藤航等核心球员是否因伤临时退出大名单。
* **搜索格式建议**：`[球队A] vs [球队B] 2026 World Cup lineups`。

---

## 🌤️ 环境与天气信息

### [AccuWeather 国际气象网](https://www.accuweather.com)
* **用途**：辅助查询北美各承办场馆城市在开球时间点的气温、湿度、体感温度以及降雨/雪概率。

---

## 📰 战术前瞻与更衣室背景

* **主要参考**：**FotMob 世界杯新闻专栏** ([https://www.fotmob.com/leagues/77/news/world-cup](https://www.fotmob.com/leagues/77/news/world-cup))。
* **次要参考**：[The Athletic](https://theathletic.com) / [BBC Sport](https://www.bbc.com/sport) / [Sky Sports](https://www.skysports.com)。

---

## 📋 赛前首发名单预排规范 (主参考 FotMob Preview 阵型与伤停)

在官方首发公布之前（通常为赛前 1.5 小时以上），为了确保战术板的客观严谨，必须严格按照以下流程进行名单预排：

### 1. 优先查阅 FotMob 比赛页 Preview 预计阵容
* **操作**：访问 FotMob -> 按日期找到对应比赛页 -> 点击进入 Preview/Lineups 模块。
* **规范**：**必须直接复制该比赛页提供的 FotMob Preview 预计阵容、阵型与球衣号码进行绘制**。只有在没有提供 Preview 预计首发时，才作为后备方案沿用该队第一轮（上一场）的官方实际首发阵容与球衣号码。
* **Match 链接备份 (Group E & F)**：
  * 🇳🇱 vs 🇸🇪 **荷兰 vs 瑞典**：[https://www.fotmob.com/matches/netherlands-vs-sweden/1x1gy6](https://www.fotmob.com/matches/netherlands-vs-sweden/1x1gy6)
  * 🇩🇪 vs 🇨🇮 **德国 vs 科特迪瓦**：[https://www.fotmob.com/matches/ivory-coast-vs-germany/1xi59e#4667780](https://www.fotmob.com/matches/ivory-coast-vs-germany/1xi59e#4667780)
  * 🇪🇨 vs 🇨🇼 **厄瓜多尔 vs 库拉索**：[https://www.fotmob.com/matches/ecuador-vs-curacao/jy3jhs3#4667779](https://www.fotmob.com/matches/ecuador-vs-curacao/jy3jhs3#4667779)
  * 🇹🇳 vs 🇯🇵 **突尼斯 vs 日本**：[https://www.fotmob.com/matches/japan-vs-tunisia/1hqd1q#4667785](https://www.fotmob.com/matches/japan-vs-tunisia/1hqd1q#4667785)

### 2. 伤停与红黄牌停赛排查
* **数据源**：直接在 **FotMob 单场比赛的 Preview 页面、伤停板块 (Injuries/Suspensions) 或新闻列表** 中进行排查。
* **可视化标注规范**：
  * **文字标注**：在主力伤病或累计黄牌停赛的球员名字后追加 **`(伤停)`** 或 **`(停赛)`**。如果是黄牌在身但正常上场的球员，名字后追加 **`🟨`**（如范德芬 🟨、巴佐尔 🟨、赫迪拉 🟨）。
  * **圆圈样式**：对于伤停/停赛无法上场但需要保留在阵型中作对照的球员，将圆圈的 CSS 样式修改为 **`background:#555555; color:#888888; border:1px solid #ff4444;`**（灰色底色，红色边框）。
