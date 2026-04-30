# 👴 Buffett-Agent (巴菲特投资助手)

这是一个模仿沃伦·巴菲特（Warren Buffett）投资哲学与口吻的开源 AI Agent。它接入了 DeepSeek 模型，能够根据实时财报数据分析公司的价值。

## 🌟 特色
- **真实的人格化**：深层模仿巴菲特的投资逻辑（护城河、ROE、安全边际）和幽默亲切的谈话风格。
- **实时数据支撑**：通过 `yfinance` 获取真实的上市公司财务报表指标。
- **DeepSeek 驱动**：利用 DeepSeek-V3 的强大推理能力进行深度财报解读。

## 🚀 快速开始

### 1. 环境准备
确保已安装 Python 3.9+。

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行应用
```bash
streamlit run app.py
```

## 🛠️ 技术栈
- **LLM**: DeepSeek-V3
- **Data**: Yahoo Finance (yfinance)
- **Framework**: Streamlit
- **Language**: Python

## ⚠️ 注意事项
本工具仅供娱乐和研究 AI 人格模拟使用，其输出内容不构成任何真实投资建议。投资有风险，入市需谨慎。
