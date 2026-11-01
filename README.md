# AMT-Handbook

FAA《Aviation Maintenance Technician Handbook》（航空维修技师手册）的中文读书笔记。

三册共 42 章，对应 44 份笔记（部分长章拆成上下两半）：

| 分册 | 笔记数 | 目录 |
|---|---|---|
| General 通用 | 15 份 | [`notes/general/`](notes/general/) |
| Airframe 机体 | 18 份 | [`notes/airframe/`](notes/airframe/) |
| Powerplant 动力装置 | 11 份 | [`notes/powerplant/`](notes/powerplant/) |

**从总索引开始看**：[`INDEX.md`](INDEX.md) —— 每章一句话概括，点进去看全文。

## 在线阅读（带目录的站点）

在线站点：**<https://leochilfen.github.io/AMT-Handbook/>**（GitHub Pages，`main` 分支 `/docs` 目录）

站点功能：左侧三册目录、顶部搜索框（按章节标题过滤，快捷键 `/`）、每页小节跳转、上一章 / 下一章翻页。

`docs/` 是生成产物，别手改。改完 `notes/` 下的 Markdown 后重新生成再推送：

```powershell
python tools/build_site.py .      # 重新生成 docs/
git add -A; git commit -m "更新笔记"; git push
```

（`tools/build_site.py` 只用标准库，不需要装 markdown 之类的包；`tools/check_cloze.py` 可校验每章第 7 节完形填空的题号、选项、答案条数。）

## 目录结构

```
.
├── INDEX.md              总索引（每章一句话）
├── notes/
│   ├── general/          General 分册笔记
│   ├── airframe/         Airframe 分册笔记
│   └── powerplant/       Powerplant 分册笔记
├── docs/                 静态站点（GitHub Pages 用，自动生成）
│   ├── index.html        站点入口
│   ├── data.js           章节清单
│   ├── assets/           样式与脚本
│   └── pages/            每章渲染好的 HTML
├── .gitignore
└── README.md
```

## 笔记体例

每份笔记固定 8 个小节：

1. 一句话
2. 要点
3. 术语对照（中英）
4. 关键数字
5. 结构部件
6. 检查 / 维修
7. 高频考点（TECC 英语完形填空）
8. 易混点

第 7 节共 10 道英文完形填空题，取材本章内容，每题一个空、四个选项，干扰项按**形近词、同词族变体、近义词**设置；答案与解析在每章末尾，用中文讲清语法点和词义辨析。

## 常用命令

```powershell
git status              # 看现在有哪些改动
git add .               # 把改动加入暂存区
git commit -m "说明"     # 提交
git push                # 推到 GitHub
git pull                # 拉回最新
git log --oneline       # 看提交历史
```

## 说明

- 分支：`main`，远程：`origin` → https://github.com/LeoChilfen/AMT-Handbook
- 笔记是根据 FAA《AMT Handbook》公开出版物整理的中文材料，公式与数据按原文抄录，供复习与查阅
- 只收录笔记本身；原文 PDF / 抽取的 txt 不入库
