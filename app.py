import streamlit as st
import pandas as pd
from data_provider import get_stock_data
from engine import BuffettEngine
import os
import json

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

# 设置页面
st.set_page_config(page_title="奥马哈先知 - 巴菲特AI助理", page_icon="👴", layout="wide")

# 加载配置
user_config = load_config()

# --- 优雅的 UI 样式控制 ---
st.markdown("""
    <style>
    /* 全局背景：象牙色/羊皮纸底色 */
    .stApp {
        background-color: #fdfaf1;
    }
    
    /* 侧边栏样式 */
    [data-testid="stSidebar"] {
        background-color: #f1ebd7;
        border-right: 1px solid #dcd3b6;
    }

    /* 按钮样式：深木棕色 */
    .stButton>button {
        width: 100%;
        border-radius: 4px;
        height: 3.5em;
        background-color: #5d4037;
        color: #fdfaf1;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #795548;
        color: #fff;
    }

    /* 核心对话框：羊皮纸书页样式 */
    .buffett-card {
        background-color: #fffdf5; /* 纸张色 */
        padding: 30px;
        border: 1px solid #e0d5b1;
        border-radius: 2px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
        position: relative;
        font-family: 'Georgia', serif;
        line-height: 1.8;
        color: #3e2723;
        font-size: 1.1em;
        margin-top: 20px;
    }
    
    /* 书页左侧的艺术装饰线 */
    .buffett-card::before {
        content: "";
        position: absolute;
        top: 0; left: 5px; bottom: 0;
        width: 2px;
        background: #dcd3b6;
    }

    .buffett-header {
        font-family: 'Georgia', serif;
        color: #5d4037;
        font-style: italic;
        font-weight: bold;
        border-bottom: 1px solid #dcd3b6;
        margin-bottom: 15px;
        padding-bottom: 5px;
    }

    .buffett-footer {
        text-align: right;
        font-size: 0.9em;
        color: #8d6e63;
        margin-top: 20px;
        font-style: italic;
    }

    /* 输入框样式 */
    .stTextInput>div>div>input {
        background-color: #fff;
        border-radius: 4px;
    }
    
    /* 标题样式 */
    h1 {
        color: #3e2723;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📜 奥马哈先知：巴菲特投资随笔")

# 侧边栏
with st.sidebar:
    st.markdown("### 🖋️ 签名与配置")
    saved_key = user_config.get("api_key", "")
    api_key = st.text_input("DeepSeek API Key", value=saved_key, type="password")
    
    if api_key != saved_key:
        user_config["api_key"] = api_key
        save_config(user_config)
        st.success("配置已更新")

    st.divider()
    st.info("巴菲特在此为你剖析企业价值，不谈投机，只谈成长。")

# 主界面
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🔍 目标企业")
    symbol = st.text_input("输入代码 (A股或美股)", placeholder="例如: 600519 或 AAPL")
    analyze_btn = st.button("开始深度剖析")

if analyze_btn:
    if not api_key:
        st.error("请先在侧边栏填入 API Key。")
    elif not symbol:
        st.warning("请输入代码。")
    else:
        with st.spinner("正在奥马哈办公室翻阅财报..."):
            data, summary = get_stock_data(symbol)
            if data:
                with col2:
                    st.markdown("### 📈 财务快照")
                    # 使用表格展示，更像报纸
                    st.table(pd.DataFrame([data]).T.rename(columns={0: '数值'}))
                    
                    # 巴菲特评价
                    st.markdown("### 🗣️ 股神笔记")
                    engine = BuffettEngine(api_key=api_key)
                    response_text = engine.analyze(summary, data)
                    
                    # 使用自定义的羊皮纸 HTML
                    st.markdown(f"""
                    <div class="buffett-card">
                        <div class="buffett-header">奥马哈的来信：</div>
                        {response_text}
                        <div class="buffett-footer">— 你的老伙计，沃伦·巴菲特</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.error("数据暂不可用，请检查代码。")

# 页脚
st.divider()
st.markdown("<center style='color: #8d6e63; font-family: serif;'>做时间的朋友 · 远离市场噪音</center>", unsafe_allow_html=True)
