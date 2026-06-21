# 👴 巴菲特 AI 投资助手（Buffett-Agent）

> 一个模仿沃伦·巴菲特投资哲学与口吻的 AI 助手。输入股票代码，它会像巴菲特一样分析公司价值，并以幽默亲切的风格给出点评。

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 效果预览

- 📜 羊皮纸 + 书页式 UI，满满复古艺术感
- 🧠 以巴菲特口吻分析：护城河、ROE、安全边际
- 📊 实时 A 股行情数据（腾讯财经接口）
- 🤖 DeepSeek 大模型驱动，自然语言生成

---

## 🚀 从零开始使用（保姆级教程）

### 第一步：安装 Python

> 如果你已经装过 Python 3.9+，直接跳到第二步。

1. 打开 [Python 官网下载页](https://www.python.org/downloads/)
2. 点击 **Download Python 3.x.x**（黄色大按钮）
3. 运行安装程序，**⚠️ 一定要勾选底部的 `Add Python to PATH`**，然后点 Install Now
4. 安装完成后，打开 **命令提示符**（Windows 按 `Win+R`，输入 `cmd` 回车），输入：
   ```
   python --version
   ```
   能看到版本号（如 `Python 3.10.x`）就说明成功了 ✅

---

### 第二步：下载本项目

**方法 A：直接下载 ZIP（不会 git 的用这个）**

1. 点击本页面右上角绿色的 **`<> Code`** 按钮
2. 点击 **`Download ZIP`**
3. 解压到你喜欢的位置（比如桌面）

**方法 B：用 Git 克隆（会 git 的用这个）**

```bash
git clone https://github.com/yaohaoliang141-max/buffett-agent.git
```

---

### 第三步：安装依赖

1. 打开 **命令提示符**（或 PowerShell / 终端）
2. 用 `cd` 命令进入项目文件夹，比如：
   ```bash
   # 如果你解压到了桌面
   cd C:\Users\你的用户名\Desktop\buffett-agent
   
   # 如果你用 git clone 到了某个目录
   cd E:\workplace\buffett-agent
   ```
3. 运行以下命令安装所有依赖：
   ```bash
   pip install -r requirements.txt
   ```
   > 💡 如果提示 `pip 不是内部命令`，说明第一步没有勾选 `Add to PATH`，重新安装 Python 并勾选。
   >
   > 💡 如果下载很慢，可以用国内镜像：
   > ```bash
   > pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   > ```

---

### 第四步：获取 DeepSeek API Key（免费）

1. 打开 [DeepSeek 开放平台](https://platform.deepseek.com/)
2. 注册/登录账号
3. 进入 **API Keys** 页面，点击 **创建 API Key**
4. 复制生成的 Key（以 `sk-` 开头），**保存好，后面要用**

---

### 第五步：启动应用 🎉

在项目目录下运行：

```bash
streamlit run app.py --server.port 8505
```

然后打开浏览器访问：**http://localhost:8505**

页面打开后：
1. 在 **左侧边栏** 粘贴你的 DeepSeek API Key
2. 在主页面输入股票代码（例如 `600519` 是茅台，`AAPL` 是苹果）
3. 点击 **「开始深度剖析」**
4. 等待几秒，即可看到财务快照 + 巴菲特风格的点评 📜

---

## 📂 项目结构

```
buffett-agent/
├── app.py               # Streamlit 主界面
├── engine.py             # DeepSeek API 调用引擎
├── data_provider.py      # 腾讯财经数据抓取
├── prompts.py            # 巴菲特人格系统提示词
├── requirements.txt      # Python 依赖列表
├── test_net.py           # 网络连通性测试（调试用）
└── README.md             # 你正在看的这个文件
```

---

## ❓ 常见问题

### Q：启动后报 `ProxyError` 或 `SSLError`

你的电脑开了代理/VPN。项目已内置代理绕过，如果仍然出错，尝试**关闭代理软件**后重新运行。

### Q：`pip install` 报错或很慢

使用清华镜像源：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q：`streamlit: 不是内部命令`

说明 streamlit 没装上或不在 PATH 中，尝试：
```bash
python -m streamlit run app.py --server.port 8505
```

### Q：输入美股代码没有财务数据

目前实时数据主要支持 **A 股**（腾讯财经接口），美股/港股会使用 DeepSeek 模型自身的知识进行分析，数据可能不是最新的。

---

## 🛠️ 技术栈

| 组件 | 技术 |
|------|------|
| 大模型 | DeepSeek-Chat（OpenAI 兼容接口） |
| 数据源 | 腾讯财经实时行情 |
| 前端 | Streamlit（自适应宽屏） |
| 语言 | Python 3.9+ |

---

## ⚠️ 注意事项

- **仅供学习与娱乐**，不构成任何投资建议
- **保护好你的 API Key**，不要公开分享
- 如遇到 DeepSeek 接口不稳定，可在 `engine.py` 中修改 `base_url` 使用镜像

---

## 📜 许可证

MIT License — 自由使用、修改、分发，保留原始版权声明即可。
