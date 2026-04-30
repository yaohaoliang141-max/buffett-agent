# 👴 Buffett‑Agent (巴菲特投资助手)

这是一个模仿 **沃伦·巴菲特（Warren Buffett）** 投资哲学与口吻的开源 AI Agent。它接入 **DeepSeek** 模型，能够根据实时财报数据分析公司的价值，并以巴菲特的风格给出点评。

## 🌟 特色
- **人格化**：深层模仿巴菲特的投资逻辑（护城河、ROE、安全边际）和幽默亲切的语言风格。
- **实时数据**：采用 **腾讯财经** + **AkShare** 双源接口获取 A 股与美股关键财务指标，避免 429/断连问题。
- **DeepSeek 驱动**：基于 DeepSeek‑Chat（兼容 OpenAI API）进行自然语言生成。
- **优雅 UI**：书页式羊皮纸配色、木纹按钮，配有巴菲特语录装饰，提升艺术感。
- **安全持久化**：API Key 保存于 `config.json`（已在 `.gitignore` 中排除），防止泄露。

## 🛠️ 技术栈
- **LLM**：DeepSeek‑Chat（OpenAI 兼容）
- **数据**：腾讯财经接口 + AkShare（A 股）
- **前端**：Streamlit（自适应宽屏）
- **语言**：Python 3.9+

## 🚀 快速开始
```bash
# 1️⃣ 克隆仓库
git clone https://github.com/yaohaoliang141-max/buffett-agent.git
cd buffet-agent

# 2️⃣ 创建并激活虚拟环境（推荐）
python -m venv venv
# Windows
.\\venv\\Scripts\\activate
# macOS / Linux
# source venv/bin/activate

# 3️⃣ 安装依赖
pip install -r requirements.txt
```

## 🔑 配置 DeepSeek API Key
项目会优先读取 `config.json` 中的 `api_key`，如果不存在则读取环境变量 `DEEPSEEK_API_KEY`。

**方式一 – 本地文件**（推荐，安全）
```json
{
  "api_key": "YOUR_DEEPSEEK_API_KEY"
}
```
将上述内容保存为项目根目录的 `config.json`（已在 `.gitignore` 中，不会被提交）。

**方式二 – 环境变量**
```powershell
# Windows PowerShell
$env:DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_API_KEY"
# macOS / Linux
export DEEPSEEK_API_KEY="YOUR_DEEPSEEK_API_KEY"
```

> **请务必把 `YOUR_DEEPSEEK_API_KEY` 替换为你在 DeepSeek 平台生成的 Personal Access Token。**

## ▶️ 启动应用
```bash
streamlit run app.py --server.port 8505
```
打开浏览器访问 `http://localhost:8505`，左侧会提示输入 API Key（如果已经有 `config.json` 会自动加载），在主页面输入股票代码（如 `600519` 或 `AAPL`），点击 **“开始深度剖析”** 即可看到财务快照和巴菲特的书页式点评。

## 📂 项目结构
```
buffett-agent/
├─ app.py               # Streamlit UI & 主交互
├─ engine.py            # DeepSeek 调用（requests 实现）
├─ data_provider.py     # 腾讯 + AkShare 数据抓取
├─ prompts.py           # 巴菲特系统提示词
├─ requirements.txt     # 依赖列表
├─ test_net.py          # 简单网络连通性示例（调试用）
├─ README.md            # 本说明文件
└─ config.json (ignored) # 本地保存的 DeepSeek API Key
```

## ⚠️ 注意事项
- **仅供学习与娱乐**：本工具不构成任何投资建议，请自行判断后使用。
- **API Key 保密**：切勿将 `config.json` 或 `DEEPSEEK_API_KEY` 公开提交。我们已在 `.gitignore` 中排除该文件。
- **网络环境**：如果在国内访问 DeepSeek 仍有不稳定，可自行在 `engine.py` 中修改 `base_url`（如使用国内镜像）。

## 📜 许可证
MIT License – 你可以自由使用、修改并分发本项目，只需保留原始版权声明。
