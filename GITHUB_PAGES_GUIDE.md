# GitHub Pages 发布图文说明（一步一步）

## 适用对象
本说明用于把 `Rubik Structural Studio` 发布到 **GitHub Pages**，让审稿人通过公开链接直接体验匿名原型。

---

## 0. 你需要准备什么
- 一个 GitHub 账号
- 下载并解压本包
- 保留这 3 个核心文件：
  - `index.html`
  - `styles.css`
  - `app.js`

---

## 1. 新建仓库
### 操作
1. 登录 GitHub
2. 点击右上角 **+** → **New repository**
3. 仓库名建议：`rubik-structural-studio-demo`
4. 选择 **Public**
5. 点击 **Create repository**

### 文字示意图
```
GitHub 首页
 └── +
     └── New repository
         ├── Repository name: rubik-structural-studio-demo
         ├── Visibility: Public
         └── Create repository
```

---

## 2. 上传网站文件
### 操作
1. 进入新仓库页面
2. 点击 **uploading an existing file**
3. 把这 3 个文件拖进去：
   - `index.html`
   - `styles.css`
   - `app.js`
4. 点击 **Commit changes**

### 文字示意图
```
仓库首页
 └── Add file
     └── Upload files
         ├── index.html
         ├── styles.css
         └── app.js
```

---

## 3. 打开 GitHub Pages
### 操作
1. 在仓库顶部点击 **Settings**
2. 左侧菜单点击 **Pages**
3. 在 **Build and deployment** 处选择：
   - **Source**: `Deploy from a branch`
   - **Branch**: `main`
   - **Folder**: `/root`
4. 点击 **Save**

### 文字示意图
```
Settings
 └── Pages
     ├── Source: Deploy from a branch
     ├── Branch: main
     ├── Folder: /root
     └── Save
```

---

## 4. 等待网站上线
### 操作
保存后等待 1–3 分钟。
GitHub 会显示一个网站地址，通常形如：

```
https://YOUR-USERNAME.github.io/rubik-structural-studio-demo/
```

如果页面还没出来，刷新 **Settings → Pages** 一次。

---

## 5. 审稿人匿名展示建议
### 建议保留
- 首页的 **Anonymous interactive prototype** 标签
- `Reviewer mode`
- `Paper summary`

### 建议不要出现
- 作者姓名
- 学校/实验室信息
- 个人 GitHub 简介链接
- 任何统计追踪脚本

---

## 6. 审稿人推荐体验路径
请在邮件或补充材料中提示审稿人：
1. 打开首页，阅读 **Paper summary**
2. 点击 **Open reviewer mode**
3. 在 **Research** 标签中分别选择：
   - Condition A — manipulation only
   - Condition C — manipulation + comparison + notation + explanation
4. 在 **Cube Lab** 中尝试几个动作
5. 在 **Notation** 中写一句解释并点击评分
6. 在 **Transfer** 中完成 1–3 个题目
7. 在 **Research** 中导出 JSON / CSV

---

## 7. 如果页面显示不正常
### 常见原因 1：文件路径不对
确保 `index.html`、`styles.css`、`app.js` 在仓库根目录。

### 常见原因 2：还没发布完成
GitHub Pages 有时需要 1–3 分钟。

### 常见原因 3：缓存问题
强制刷新浏览器：
- Windows: `Ctrl + F5`
- Mac: `Cmd + Shift + R`

---

## 8. 如果你想更新内容
只要重新上传修改后的文件并 commit，GitHub Pages 会自动重新部署。

---
## 9. 最终检查清单
- [ ] 首页可打开
- [ ] `Reviewer mode` 可打开
- [ ] Cube Lab 可操作
- [ ] Compare / Notation / Transfer / Research 都能切换
- [ ] JSON / CSV 可导出
- [ ] 页面没有作者身份信息
