# 官方赛程与实时名单参考数据源 (Reference Data Sources)

为保证赛事预测与首发战术板的权威性和准确性，以下是本项目日常开发与预测过程中频繁查阅的权威数据源。无论是人类手动更新还是其他 AI 接续工作，请**以本数据手册作为唯一的数据指引源**。

---

## 一、赛程与分组积分核对 (官方与备用)

### 1-A. [FIFA 官方 2026 世界杯赛程中心](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026)
* **用途**：大盘赛程时间权威基准、分组实时积分与晋级形势核对。
* **说明**：单场的主裁判指派、执裁记录、比赛场馆、城市以及实时气温/海拔等环境信息，**应直接在 FotMob 单场 Match Details 页面中查阅，无需访问此 FIFA 官网**。本链接主要作为大盘全局的备用校验源。

---

## 二、实时首发阵容与首发预测 (主参考 FotMob)

### 2-A. [FotMob 世界杯数据中心](https://www.fotmob.com)
* **主专栏 (Overview)**: [https://www.fotmob.com/leagues/77/overview/world-cup](https://www.fotmob.com/leagues/77/overview/world-cup) —— 包含所有详细信息、积分榜及深度数据统计。
* **分组信息及目前局势**: [https://www.fotmob.com/leagues/77/table/world-cup?filter=all](https://www.fotmob.com/leagues/77/table/world-cup?filter=all) —— 全方位对阵积分榜与形势分析。
* **赛程淘汰赛表 (Playoff)**: [https://www.fotmob.com/leagues/77/playoff/world-cup](https://www.fotmob.com/leagues/77/playoff/world-cup) —— 实时更新的淘汰赛晋级树状图。
* **赛程按日期 (Fixtures by Date)**:
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date)
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=1](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=1)
  * [https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=2](https://www.fotmob.com/leagues/77/fixtures/world-cup?group=by-date&page=2) (对于较后天的比赛，若在 page 1 找不到，向后翻页即可找到)
  * **单场历史交锋 (H2H) 核对规范**：在进入单场 Match Details 详情页后，找到 **Head-to-head** (H2H) 栏目核对两队交战历史。**🚨 历史交锋限制：年份超过 5 年的交手记录不能作为参考，直接过滤掉；若 5 年内无交战记录，该项 15% 权重归 0，均摊给近期状态与硬实力。**
* **球员统计数据**: [https://www.fotmob.com/leagues/77/stats/world-cup/players](https://www.fotmob.com/leagues/77/stats/world-cup/players)
  * **用途**：检索关键球员的个人数据表现。
  * **各项核心球员指标直达链接 (Season ID: 24254)**：
    * **进球 (Goals)**: [https://www.fotmob.com/leagues/77/stats/season/24254/players/goals/world-cup-players](https://www.fotmob.com/leagues/77/stats/season/24254/players/goals/world-cup-players)
    * **助攻 (Assists)**: [https://www.fotmob.com/leagues/77/stats/season/24254/players/goal_assist/world-cup-players](https://www.fotmob.com/leagues/77/stats/season/24254/players/goal_assist/world-cup-players)
    * **期望进球 (xG)**: [https://www.fotmob.com/leagues/77/stats/season/24254/players/expected_goals/world-cup-players](https://www.fotmob.com/leagues/77/stats/season/24254/players/expected_goals/world-cup-players)
    * **期望助攻 (xA)**: [https://www.fotmob.com/leagues/77/stats/season/24254/players/expected_assists/world-cup-players](https://www.fotmob.com/leagues/77/stats/season/24254/players/expected_assists/world-cup-players)
    * **创造重大机会 (Big chances created)**: [https://www.fotmob.com/leagues/77/stats/season/24254/players/big_chance_created/world-cup-players](https://www.fotmob.com/leagues/77/stats/season/24254/players/big_chance_created/world-cup-players)
    * **评分 (FotMob rating)**: [https://www.fotmob.com/leagues/77/stats/season/24254/players/rating/world-cup-players](https://www.fotmob.com/leagues/77/stats/season/24254/players/rating/world-cup-players)
* **球队统计数据**: [https://www.fotmob.com/leagues/77/stats/world-cup/teams](https://www.fotmob.com/leagues/77/stats/world-cup/teams)
  * **用途**：检索团队层面的整体战术实力指标。
  * **各项核心团队指标直达链接 (Season ID: 24254)**：
    * **期望进球 (xG)**: [https://www.fotmob.com/leagues/77/stats/season/24254/teams/expected_goals_team/world-cup-teams](https://www.fotmob.com/leagues/77/stats/season/24254/teams/expected_goals_team/world-cup-teams)
    * **期望进球差 (xG Diff)**: [https://www.fotmob.com/leagues/77/stats/season/24254/teams/_xg_diff_team/world-cup-teams](https://www.fotmob.com/leagues/77/stats/season/24254/teams/_xg_diff_team/world-cup-teams)
    * **控球率 (Average Possession)**: [https://www.fotmob.com/leagues/77/stats/season/24254/teams/possession_percentage_team/world-cup-teams](https://www.fotmob.com/leagues/77/stats/season/24254/teams/possession_percentage_team/world-cup-teams)
    * **期望失球 (xGA)**: [https://www.fotmob.com/leagues/77/stats/season/24254/teams/expected_goals_conceded_team/world-cup-teams](https://www.fotmob.com/leagues/77/stats/season/24254/teams/expected_goals_conceded_team/world-cup-teams)
    * **前场夺回球权次数 (Possession won final 3rd per match)**: [https://www.fotmob.com/leagues/77/stats/season/24254/teams/poss_won_att_3rd_team/world-cup-teams](https://www.fotmob.com/leagues/77/stats/season/24254/teams/poss_won_att_3rd_team/world-cup-teams) —— **此项作为高位逼抢强度 (PPDA) 的直接代理指标。**
    * **场均精准传球 (Accurate Passes per match)**: [https://www.fotmob.com/leagues/77/stats/season/24254/teams/accurate_pass_team/world-cup-teams](https://www.fotmob.com/leagues/77/stats/season/24254/teams/accurate_pass_team/world-cup-teams)

---

## 三、场外雷达与更衣室舆情检索指南 (Off-Pitch Barometer)

本项目的特色在于**将非结构化的场外吃瓜舆情量化为概率修正因子**。查询与检索流程遵循以下分级优先级规范：

### 3-A. 舆情与伤停信息分级检索流

1. 🥇 **第一优先级（主要参考 · FotMob 比赛详情页）**
   - 直接前往对应的 **FotMob 单场比赛详情页**（如荷兰对瑞典：`https://www.fotmob.com/matches/netherlands-vs-sweden/1x1gy6#4667786`），查阅以下板块：
     - **Insights & News**（情报与新闻）：FotMob 比赛页面会对伤停、红黄牌停赛信息进行实时更新，这是核对伤停的最主要、最前沿的数据源。
     - **Team Form**（近五场战绩）：获取状态走势。
     - **About the Match**：获取环境、裁判等赛事实时信息。
2. 🥈 **第二优先级（次要参考 · 综合新闻大厅）**
   - **Sofascore 世界杯新闻**: [https://www.sofascore.com/news?category=world-cup](https://www.sofascore.com/news?category=world-cup) —— 查阅世界杯相关的实时赛事战报与深度爆料。
   - **FIFA 官方新闻**: [https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/news](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/news) —— 查阅大名单调整、突发官宣及伤退通告。
3. 🥉 **第三优先级（辅助补充 · Google 搜索与社媒）**
   - 当上述两级数据源存在争议或需要核查深层舆情（如更衣室内讧细节、战术泄密等）时，使用 Google 搜索或查阅社媒官方账号。

### 3-B. Google 搜索 Query 检索模板
将 `[Country A]` / `[Star Player]` 替换为具体球队/球员名：
```
# 🔴 更衣室与内部矛盾（核心侦察项）
[Country A] "dressing room" OR "camp dispute" OR "player clash" OR "internal conflict" 2026 World Cup
[国家A名] 国家队 内讧 OR 矛盾 OR 派系 OR 更衣室 2026 世界杯

# 🟡 伤停真假与训练缺席（烟雾弹识别）
[Star Player] injury "training" OR "doubt" OR "miss" OR "ruled out" 2026 World Cup
[球星名] 伤病 OR 训练缺席 OR 缺战 OR 不确定 2026 世界杯 site:fotmob.com OR site:bbc.com

# 🟠 外部舆论与战术泄密
[Country] coach "press conference" tactics OR "starting lineup" 2026 World Cup
```

### 3-C. 舆情爆料源信源分级与可信度目录

| 优先级 | 来源名称与语种 | 覆盖范围与官方链接 | 检索与获取方式 |
|--------|------|---------|---------|
| 🥇 **一级**<br>(公信力极高) | **The Athletic** (英语) | 英格兰、欧洲五大联赛豪门及全球世界杯动态<br>[https://theathletic.com](https://theathletic.com) | 搜索 `site:theathletic.com [球队/球员名] 2026` |
| 🥇 **一级** | **L'Équipe** / **RMC Sport**<br>**Le Parisien** (法语) | 法国国家队、法甲随队记者及非洲法语系国家队内幕<br>[https://www.lequipe.fr](https://www.lequipe.fr) \| [https://rmcsport.bfmtv.com](https://rmcsport.bfmtv.com) \| [https://www.leparisien.fr](https://www.leparisien.fr) | 搜索 `site:lequipe.fr OR site:rmcsport.bfmtv.com OR site:leparisien.fr [球员/队名] 2026` |
| 🥇 **一级** | **Marca** / **AS** / **Relevo**<br>**Mundo Deportivo** (西语) | 西班牙国家队、西甲背景国脚、阿根廷及拉美国家队<br>[https://www.marca.com](https://www.marca.com) \| [https://as.com](https://as.com) \| [https://www.relevo.com](https://www.relevo.com) \| [https://www.mundodeportivo.com](https://www.mundodeportivo.com) | 搜索 `site:marca.com OR site:as.com OR site:relevo.com OR site:mundodeportivo.com [球队名] 2026` |
| 🥇 **一级** | **Bild** / **Kicker**<br>**Sky Sport DE** (德语) | 德国国家队、德甲背景球员伤停与更衣室动向<br>[https://www.bild.de](https://www.bild.de) \| [https://www.kicker.de](https://www.kicker.de) \| [https://sport.sky.de](https://sport.sky.de) | 搜索 `site:bild.de OR site:kicker.de OR site:sport.sky.de [德国队/球员] 2026` |
| 🥇 **一级** | **Globo Esporte (GE)**<br>**UOL Esporte** (葡语) | 巴西国家队、巴甲随队爆料及南美其他球队一手内情<br>[https://ge.globo.com](https://ge.globo.com) \| [https://www.uol.com.br/esporte](https://www.uol.com.br/esporte) | 搜索 `site:ge.globo.com OR site:uol.com.br/esporte [巴西队/球员名] 2026` |
| 🥇 **一级** | **La Gazzetta dello Sport**<br>**Sky Sport Italia** (意语) | 意大利国家队、意甲球员、意甲背景国脚战术与内伤<br>[https://www.gazzetta.it](https://www.gazzetta.it) \| [https://sport.sky.it](https://sport.sky.it) | 搜索 `site:gazzetta.it OR site:sport.sky.it [意甲球队/国脚] 2026` |
| 🥈 **二级**<br>(主力辅助) | **De Telegraaf** / **VI**<br>**AD Sportwereld** (荷兰语) | 荷兰国家队、荷甲背景球员动态及更衣室消息<br>[https://www.telegraaf.nl/sport](https://www.telegraaf.nl/sport) \| [https://www.vi.nl](https://www.vi.nl) \| [https://www.ad.nl/sport](https://www.ad.nl/sport) | 搜索 `site:telegraaf.nl OR site:vi.nl OR site:ad.nl/sport [荷兰队/球员] 2026` |
| 🥈 **二级** | **A Bola** / **Record**<br>**O Jogo** (葡语) | 葡萄牙国家队、葡超三强国脚动态、更衣室平衡度<br>[https://www.abola.pt](https://www.abola.pt) \| [https://www.record.pt](https://www.record.pt) \| [https://www.ojogo.pt](https://www.ojogo.pt) | 搜索 `site:abola.pt OR site:record.pt OR site:ojogo.pt [葡萄牙队/C罗] 2026` |
| 🥈 **二级** | **ESPN Deportes** / **TyC Sports**<br>**Olé** / **La Nación** (西语) | 阿根廷、乌拉圭、哥伦比亚等南美强队内幕与大名单<br>[https://espndeportes.espn.com](https://espndeportes.espn.com) \| [https://www.tycsports.com](https://www.tycsports.com) \| [https://www.ole.com.ar](https://www.ole.com.ar) \| [https://www.lanacion.com.ar/deportes](https://www.lanacion.com.ar/deportes) | 搜索 `site:tycsports.com OR site:ole.com.ar OR site:lanacion.com.ar OR site:espndeportes.espn.com [队名] 2026` |
| 🥈 **二级** | **Sky Sports** / **BBC Sport**<br>**The Guardian** (英语) | 英格兰代表队、英超大牌球员、非洲英语区队伍<br>[https://www.bbc.com/sport](https://www.bbc.com/sport) \| [https://www.skysports.com](https://www.skysports.com) \| [https://www.theguardian.com/football](https://www.theguardian.com/football) | 搜索 `site:bbc.com/sport OR site:skysports.com OR site:theguardian.com/football [队名] 2026` |
| 🥈 **二级** | **日刊スポーツ** / **Gekisaka**<br>**Football Zone** (日语) | 日本国家队、东亚队伍战术爆料、旅欧国脚伤停细节<br>[https://www.nikkansports.com](https://www.nikkansports.com) \| [https://web.gekisaka.jp](https://web.gekisaka.jp) \| [https://www.football-zone.net](https://www.football-zone.net) | 搜索 `site:nikkansports.com OR site:gekisaka.jp OR site:football-zone.net [球队/球员名] 2026` |
| 🥈 **二级** | **Naver Sports** / **Sports Chosun**<br>**Sports Seoul** (韩语) | 韩国国家队内乱/内讧排查、核心球员伤病与战术地位<br>[https://sports.news.naver.com](https://sports.news.naver.com) \| [https://sports.chosun.com](https://sports.chosun.com) \| [https://www.sportsseoul.com](https://www.sportsseoul.com) | 搜索 `site:sports.chosun.com OR site:sportsseoul.com [球员名] 2026` (利用门户或特定报社搜索) |
| 🥈 **二级** | **Afrik-Foot** / **KickOff**<br>**Sport News Africa** (法语/英语) | 非洲各队（尼日利亚/喀麦隆/塞内加尔等）更衣室及战术爆料新闻<br>[https://www.afrik-foot.com](https://www.afrik-foot.com) \| [https://www.kickoff.com](https://www.kickoff.com) \| [https://sportnewsafrica.com](https://sportnewsafrica.com) | 搜索 `site:afrik-foot.com OR site:sportnewsafrica.com OR site:kickoff.com [队名] 2026` |
| 🥉 **三级**<br>(官方核实) | **官方社交账号 (X/IG)** | 各国足协官方发布会文字稿、大名单变动、突发伤退公告确认 | 搜索 `@[国家足协/球员官方账号] latest` 或直接访问官方社交动态 |

### 3-D. 八卦舆情与无结果时的“终极搜索检索策略”（针对 Google 与 X/Twitter）

当主流媒体和官方网站出于公关目的封锁消息，或在 FotMob/新闻大厅搜不到具体传言的实锤时，**使用以下高级检索指令在 Google 和 X (Twitter) 中发掘第一手民间或边缘记者曝出的八卦内幕**：

#### 1. 🔍 Google 高级论坛与社群检索法（突破传统媒体屏障）
当媒体没有直接报道时，小道消息和知情人爆料最先在 Reddit 或本地社区流出。
* **特定论坛/贴吧深度检索**：
  * 英格兰/英超球员：`site:reddit.com/r/soccer [国家/球员] (clash OR dispute OR training)`
  * 俱乐部球迷分版（可了解国脚球员的最新健康和社交动态）：`site:reddit.com/r/reddevils OR site:reddit.com/r/chelseafc OR site:reddit.com/r/gunners [球员名] (injury OR dispute)`
  * 针对日本代表队（5ch/Gekisaka评论区）：`site:5ch.net 2026 日本代表 (内紛 OR 衝突 OR 怪我 OR ボーナス)`
  * 针对韩国代表队（DC Inside 足球版）：`site:dcinside.com 2026 국가대표 (내분 OR 갈등 OR 부상 OR 불참)`
  * 针对西语系/拉美（ForoCoches等）：`site:forocoches.com [国家/球员名] (pelea OR lesion OR vestuario) Mundial 2026`
* **Google 排除词检索（排除干扰，直击干货）**：
  * `"[Player Name]" (injury OR training) -site:premierleague.com -site:transfermarkt.com -site:ea.com` (排除常规英超、身价网站及 FIFA 游戏卡牌数据)

#### 2. 🐦 X (Twitter) 随队记者与大V极速检索（时效最高）
利用 X 检索未经编辑的实时讨论、知情球迷现场路透、以及跟队记者个人号的第一手推特：
* **带媒体（图片/视频）验证指令**（可直观确认球员是否坐轮椅、拄拐、包扎或没有下大巴）：
  * `"[Player Name]" (injury OR training OR gym OR crutches) filter:media`
* **高互动量检索（过滤低质和机器自动发推账号）**：
  * `"[Player Name]" (fight OR clash OR dropped OR bench) min_faves:15 min_replies:3`
* **核心记者/随队大V定向监控**（在 X 的搜索框直接使用 `from:[handle]` 指令）：
  * **全球 & 欧洲顶级**：`from:FabrizioRomano` (Fabrizio Romano), `from:David_Ornstein` (David Ornstein)
  * **西班牙 & 阿根廷队内消息第一人**：`from:relevo` (Relevo), `from:gerardromero` (Gerard Romero), `from:gastonedul` (Gastón Edul)
  * **法国 & 非洲法语区**：`from:SaberDesfa` (Saber Desfarges), `from:Tanziloic` (Loïc Tanzi), `from:RMCsport`
  * **德国 & 德甲背景**：`from:cfbayern` (Christian Falk), `from:Plettigoal` (Florian Plettenberg)
  * **意大利**：`from:DiMarzio` (Gianluca Di Marzio)
  * **荷兰**：`from:MikeVerweij` (Mike Verweij), `from:RikElfrink` (Rik Elfrink)
  * **日本**：`from:aishiterutokyo` (Dan Orlowitz), `from:gekisaka` (Gekisaka)
  * **韩国**：`from:sungmolee` (李圣模)
  * **非洲大陆独家爆料**：`from:UsherKomugisha` (Usher Komugisha), `from:MickyJnr__` (Micky Jnr)

#### 3. 🌐 跨语言（小语种）核心爆料检索关键词对照表
如果用英语/中文在 Google 或 X 上搜不到内幕，**直接复制以下国家母语的敏感爆料词进行搜索**，往往能直接发现当地论坛的火爆贴：

| 语种 (国家队) | 进球/助攻 (常规) | 受伤/缺席 (身体) | 内讧/冲突 (更衣室) | 罢训/开除 (纪律) |
|---|---|---|---|---|
| **西语** (阿/西/墨/哥/拉美) | gol / asistencia | lesión / baja / duda / descartado | pelea / bronca / vestuario / conflicto | expulsado / sanción / huelga / motín |
| **法语** (法/比/科特/喀/塞) | but / passe décisive | blessure / entraînement / incertain | conflit / vestiaire / bagarre / exclu | exclu / sanction / grève / mutinerie |
| **德语** (德/奥/瑞士) | Tor / Vorlage | Verletzung / Training / fraglich | Zoff / Streit / Kabine / suspendiert | suspendiert / Streik / Meuterei |
| **葡语** (巴/葡) | gol / assistência | lesão / treino / dúvida / cortado | briga / discussão / vestiário / conflito | afastado / punição / greve / motim |
| **意语** (意) | gol / assist | infortunio / allenamento / in dubbio | rissa / spogliatoio / escluso / tensione | fuori rosa / squalifica / sciopero |
| **日语** (日) | ゴール / アシスト | 怪我 / 負傷 / 練習欠席 / 離脱 | 内紛 / 衝突 / 不仲 / メンバー落ち | ボイコット / 規律違反 / 開除 / 追放 |
| **韩语** (韩) | 골 / 어시스트 | 부상 / 불참 / 재활 / 엔트리 제외 | 내분 / 갈등 / 충돌 / 불화 / 징계 | 보이콧 / 규율 위반 / 퇴출 / 파업 |

---

## 四、伤停与黄牌可视化标注规范 (HTML 战术板)

### 4-A. 伤停烟雾弹识别规则
针对主帅在发布会上的“出战成疑 (questionable / doubt)”表述，按以下规则处理：
1. **FotMob Preview** 中仍出现在预计首发 → **战术板正常画出，名字后加 `？`**（不置灰）。
2. **FotMob Preview** 已将其移出预计首发 → **战术板置灰 + 红边 + 后缀 `(伤停?)`**。
3. 多个独立媒体（≥2个一级源）均确认伤病 → **强制置灰 + 后缀 `(伤停确认)`**。

### 4-B. 可视化 HTML 样式规则
凡是确认为**伤停、停赛、吃黄牌**的球员，战术板中**必须保留其节点**以确保两队阵型对照，但必须追加以下样式：
- **因伤病/停赛无法上场者**：
  - 名字后缀改为 `(伤停)` 或 `(停赛)`。
  - 球员圆圈底色与边框样式强制改为：`style="background:#555555; color:#888888; border:1px solid #ff4444;"`。
- **黄牌在身照常上场者**：
  - 名字后缀追加 **`🟨`**（例如：`弗兰基·德容 🟨`）。
