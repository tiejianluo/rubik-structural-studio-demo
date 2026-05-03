# Rubik Structural Studio

<div align="center">

**A cube-based interactive web prototype for teaching structural thinking**

[![Pages Target](https://img.shields.io/badge/Pages-Target-2563eb?style=for-the-badge)](https://tiejianluo.github.io/rubik-structural-studio-demo/)
[![Prototype](https://img.shields.io/badge/Status-Research%20Prototype-f59e0b?style=for-the-badge)](#project-status)
[![Theory Driven](https://img.shields.io/badge/Design-Theory%20Driven-10b981?style=for-the-badge)](#overview)

**English / 中文**

[Overview](#overview) •
[Pages Target](https://tiejianluo.github.io/rubik-structural-studio-demo/) •
[How It Works](#how-it-works) •
[Features](#features) •
[For Whom](#who-this-is-for) •
[Walkthrough](#suggested-first-walkthrough) •
[Repository Structure](#repository-structure)

</div>

---

## Overview

**Rubik Structural Studio** is not just a Rubik’s Cube demo. It is a **theory-driven learning prototype** that turns a learning-science framework into an interactive web app.

The project is built around one central question:

> **Under what conditions, and through what mechanism, can embodied manipulation support algebraic abstraction and transferable structural reasoning?**

Using a **Rubik’s Cube** as a candidate embodied system, the app helps learners move from action to structure:

1. **Embodied manipulation**  
   Interact with a reversible, order-sensitive, constraint-governed system.

2. **Relational encoding**  
   Shift attention from individual moves to relations such as **inverse**, **preserved structure**, **cycle/order**, and **local–global dependence**.

3. **Algebraic abstraction**  
   Redesign those relations using notation and structural language.

4. **Transfer**  
   Apply the same ideas to **cryptography**, **robotics**, and **symmetry-aware AI**.

**In one sentence:**  
Rubik Structural Studio is a cube-based web prototype for exploring how embodied manipulation can become algebraic abstraction and transferable structural reasoning under explicit instructional supports.

---

## 中文简介

**Rubik Structural Studio** 不是一个普通的魔方网页演示，而是一个由学习理论驱动的交互式教学原型。

它围绕一个核心问题展开：

> **在什么条件下，并通过什么机制，具身操作能够促进代数抽象与可迁移的结构性推理？**

这个网页把论文中的机制框架转成了可体验、可比较、可研究的软件流程：

1. **具身操作**  
   在一个可逆、顺序敏感、受约束的系统上行动。

2. **关系编码**  
   把注意力从单个动作转向动作之间的关系，例如**逆、保持不变的结构、周期/阶、局部—整体依赖**。

3. **代数抽象**  
   用符号记法和结构语言重新描述这些关系。

4. **迁移**  
   将这些结构性思路迁移到**密码学、机器人和对称性感知 AI**等场景。

---

## Why this repository exists

This repository exists to make the framework:

- **Inspectable** — readers and reviewers can see what the theory looks like in practice
- **Usable** — students and teachers can interact with it directly
- **Testable** — researchers can compare instructional conditions and export logs

The Rubik’s Cube is treated here **not as a self-justifying pedagogical tool**, but as a **candidate embodied system** that makes reversibility, composition, periodicity, and local–global dependence visible enough to study.

---

## How it works

The app is organized around a simple claim:

> **Hands-on activity alone is not enough.**  
> Embodied manipulation is predicted to support abstraction only when instructional supports redirect attention from moves to invariant relations.

That is why the prototype does more than let users “turn the cube.”  
It deliberately includes:

- comparison prompts,
- notation support,
- explanation prompts,
- teacher orchestration,
- and research logging / export.

These are treated as **drivers of transition**, not as optional decoration.

---

## Features

### Cube Lab
Manipulate a simplified Rubik’s Cube and observe state change.

### Compare
Compare move sequences and shift attention from steps to relations.

### Notation
Turn observed patterns into compact symbolic descriptions.

### Transfer
Apply structural ideas to cryptography, robotics, and symmetry-aware AI.

### Teacher Mode
Toggle instructional supports such as:

- comparison prompts
- notation support
- explanation prompts
- orchestration

### Research Mode
Compare three instructional conditions:

- **A — manipulation only**
- **B — manipulation + comparison**
- **C — manipulation + comparison + notation + explanation**

### Export
Export **JSON / CSV** logs for analysis.

---

## What the app is trying to capture

This prototype is not designed only to measure whether a learner can “do the moves.”  
It tries to distinguish **procedural performance** from **structural understanding**.

Typical signals include whether a learner can:

- describe an algorithm as a **whole relation** rather than a step list,
- identify **inverse** relations,
- notice **periodic return / order**,
- explain what stays **invariant** under transformation,
- and transfer those ideas to unfamiliar tasks.

---

## Screenshots

> Add screenshots here after updating the repository.

### Homepage
`docs/screenshots/homepage.png`

### Cube Lab
`docs/screenshots/cube-lab.png`

### Compare / Notation
`docs/screenshots/compare-notation.png`

### Research Mode
`docs/screenshots/research-mode.png`

---

## Who this is for

### Students
To move from concrete manipulation toward relational and symbolic understanding.

### Teachers
To orchestrate prompts, compare support conditions, and discuss what counts as a relation rather than a procedure.

### Researchers
To prototype or test instructional conditions related to embodied learning, abstraction, and transfer.

### Reviewers / readers
To inspect how the paper’s conceptual framework has been instantiated in software.

---

## Suggested first walkthrough

1. After GitHub Pages is enabled, open the [Pages app](https://tiejianluo.github.io/rubik-structural-studio-demo/)
2. Read the **Paper summary**
3. Turn on **Reviewer mode**
4. Try several moves in **Cube Lab**
5. Use **Compare** to inspect inverse, cycle, and preserved structure
6. Enter a short explanation in **Notation**
7. Try **Transfer**
8. In **Research mode**, compare **Condition A** and **Condition C**

This path mirrors the logic of the associated manuscript.

---

## Repository structure

```text
.
├── index.html
├── styles.css
├── app.js
├── README.md
├── README_DEPLOY.md
├── GITHUB_PAGES_GUIDE.md
└── docs/
    └── screenshots/
```

### Core files

- `index.html` — app entry
- `styles.css` — layout and styling
- `app.js` — interaction logic
- `README_DEPLOY.md` — deployment notes
- `GITHUB_PAGES_GUIDE.md` — step-by-step GitHub Pages guide

---

## Deployment

This project is designed to be published as a **static website**.

### Recommended option
**GitHub Pages**

See:

- `GITHUB_PAGES_GUIDE.md`
- `README_DEPLOY.md`

After GitHub Pages is enabled for this repository, open:

**https://tiejianluo.github.io/rubik-structural-studio-demo/**

---

## Project status

This is a **research prototype**, not a full production classroom platform.

### Good for
- theory demonstration
- reviewer-facing interaction
- pilot classroom use
- early research instrumentation

### Not yet intended for
- large-scale production deployment
- full assessment infrastructure
- mature learning analytics pipelines

---

## Limitations

- This app does **not** prove the theory by itself
- It does **not** establish causal learning effects on its own
- The Rubik’s Cube is a **candidate embodied system**, not a universal best manipulative
- The core claims remain empirical

---

## Possible next steps

- richer 3D cube interaction
- improved scoring of student explanations
- stronger classroom dashboards
- expanded research instrumentation
- export pipelines for behavioral analysis
- integration with formal study protocols

---

## Audit and Test Gates

This repository includes standard-library Python tests so the static prototype
can be checked even when Node is unavailable locally.

```bash
python run_tests.py
```

The command runs:

- unit tests for metadata, C1-C8 claim IDs, condition feature flags, scoring
  terms, export fields, and required UI targets;
- system tests that serve the static site and verify HTML/CSS/JS availability;
- acceptance tests that the reviewer journey exposes Cube Lab, Compare,
  Notation, Transfer, Teacher, and Research modules.

GitHub Actions runs the same command on push and pull request. Pull requests
should fill in `.github/pull_request_template.md` with the milestone, related
claims, unit/system/acceptance evidence, and any deferred risks.

---

## Citation

If you use or discuss this repository, please cite the associated manuscript and link to the live demo.

> Add the formal citation here once the paper status is finalized.

---

## Authors / note

This repository may be shared in anonymized or named form depending on submission stage.  
If you are viewing a reviewer-facing version, identifying details may be intentionally minimized.

---

## 中文快速说明

### 这个仓库是做什么的？
这是一个**基于魔方的结构思维教学原型**，把论文中的学习机制做成了交互网页。

### 它适合谁？
- 学生：从“会操作”走向“会解释结构”
- 教师：组织比较、记法、解释与讨论
- 研究者：比较不同教学条件并导出日志
- 审稿人：直接体验论文理论如何在软件中实现

### 它的核心不是“玩魔方”，而是：
通过魔方这个具身系统，帮助学习者从：
- 动作层  
走向
- 关系层  
再走向
- 代数抽象  
最后走向
- 跨领域迁移

---

<div align="center">

**If this project is useful, please star the repository and share the live demo.**

</div>
