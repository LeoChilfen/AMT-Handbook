# AMT-Handbook

FAA《Aviation Maintenance Technician Handbook》（航空维修技师手册）的中文读书笔记。

三册共 42 章，对应 44 份笔记（部分长章拆成上下两半）：

| 分册 | 笔记数 | 目录 |
|---|---|---|
| General 通用 | 15 份 | [`notes/general/`](notes/general/) |
| Airframe 机体 | 18 份 | [`notes/airframe/`](notes/airframe/) |
| Powerplant 动力装置 | 11 份 | [`notes/powerplant/`](notes/powerplant/) |

**从总索引开始看**：[`INDEX.md`](INDEX.md) —— 每章一句话概括，点进去看全文。

## 目录结构

```
.
├── INDEX.md              总索引（每章一句话）
├── notes/
│   ├── general/          General 分册笔记
│   ├── airframe/         Airframe 分册笔记
│   └── powerplant/       Powerplant 分册笔记
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
7. 高频考点
8. 易混点

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
