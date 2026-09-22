
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CodeSentinel | Repository Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------------- GLOBAL ---------------- */

    .stApp {
        background: #0b0f19;
        color: #f8fafc;
    }

    [data-testid="stHeader"] {
        background: rgba(11, 15, 25, 0.95);
    }

    [data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #263244;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    /* ---------------- SIDEBAR ---------------- */

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }

    .sidebar-logo {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        border-radius: 12px;
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: 750;
        color: #f8fafc;
    }

    .sidebar-subtitle {
        font-size: 12px;
        color: #94a3b8;
        margin-top: -4px;
    }

    .sidebar-section {
        color: #64748b;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 30px;
        margin-bottom: 12px;
    }

    .sidebar-feature {
        color: #cbd5e1;
        font-size: 14px;
        padding: 7px 0;
    }

    /* ---------------- HEADER ---------------- */

    .hero-container {
        padding: 25px 30px;
        border-radius: 18px;
        background:
            linear-gradient(
                120deg,
                rgba(37, 99, 235, 0.20),
                rgba(124, 58, 237, 0.12),
                rgba(15, 23, 42, 0.40)
            );
        border: 1px solid #263b61;
        margin-bottom: 28px;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(37, 99, 235, 0.16);
        border: 1px solid #315ba5;
        color: #93c5fd;
        border-radius: 30px;
        padding: 5px 12px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 14px;
    }

    .hero-title {
        font-size: 40px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin: 0;
        color: #f8fafc;
    }

    .hero-title span {
        color: #60a5fa;
    }

    .hero-description {
        color: #94a3b8;
        font-size: 15px;
        line-height: 1.7;
        margin-top: 10px;
        max-width: 850px;
    }

    /* ---------------- SECTION HEADINGS ---------------- */

    .section-heading {
        color: #f8fafc;
        font-size: 21px;
        font-weight: 700;
        margin-top: 26px;
        margin-bottom: 14px;
    }

    .section-description {
        color: #94a3b8;
        font-size: 13px;
        margin-bottom: 16px;
    }

    /* ---------------- KPI CARDS ---------------- */

    .metric-card {
        background: #131b2b;
        border: 1px solid #27354b;
        border-radius: 14px;
        padding: 19px;
        min-height: 125px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.10);
    }

    .metric-label {
        color: #94a3b8;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 32px;
        font-weight: 800;
        line-height: 1;
    }

    .metric-footer {
        color: #64748b;
        font-size: 11px;
        margin-top: 12px;
    }

    .metric-icon {
        font-size: 18px;
        float: right;
    }

    /* ---------------- INPUTS ---------------- */

    .stTextInput > div > div > input {
        background: #151e2e;
        border: 1px solid #334155;
        border-radius: 10px;
        color: #f8fafc;
        padding: 14px;
    }

    .stTextInput > div > div > input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 1px #3b82f6;
    }

    .stButton > button {
        background: linear-gradient(90deg, #2563eb, #4f46e5);
        color: white;
        border: none;
        border-radius: 10px;
        min-height: 46px;
        font-weight: 700;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #4338ca);
        border: none;
        transform: translateY(-1px);
    }

    /* ---------------- PANELS ---------------- */

    .dashboard-panel {
        background: #111827;
        border: 1px solid #263244;
        border-radius: 14px;
        padding: 20px;
        margin-top: 15px;
    }

    .panel-title {
        color: #e2e8f0;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .panel-description {
        color: #64748b;
        font-size: 12px;
        margin-bottom: 16px;
    }

    /* ---------------- STATUS BADGES ---------------- */

    .risk-high {
        background: rgba(239, 68, 68, 0.15);
        color: #fca5a5;
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 4px 9px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
    }

    .risk-medium {
        background: rgba(245, 158, 11, 0.15);
        color: #fcd34d;
        border: 1px solid rgba(245, 158, 11, 0.35);
        padding: 4px 9px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
    }

    .risk-low {
        background: rgba(34, 197, 94, 0.15);
        color: #86efac;
        border: 1px solid rgba(34, 197, 94, 0.35);
        padding: 4px 9px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
    }

    /* ---------------- TABLE ---------------- */

    [data-testid="stDataFrame"] {
        border: 1px solid #263244;
        border-radius: 10px;
        overflow: hidden;
    }

    /* ---------------- EXPANDERS ---------------- */

    .streamlit-expanderHeader {
        background: #131b2b;
        border: 1px solid #263244;
        border-radius: 10px;
        color: #e2e8f0;
        font-weight: 600;
    }

    /* ---------------- FOOTER ---------------- */

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        padding-top: 25px;
        padding-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CONSTANTS
# =========================================================

BACKEND_URL = "http://127.0.0.1:8000/analyze-repo/"


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_risk_level(file_data):
    value = file_data.get("risk_level", "UNKNOWN")

    if value is None:
        return "UNKNOWN"

    return str(value).upper()


def get_risk_score(file_data):
    value = file_data.get("risk_score", 0)

    try:
        return float(value)
    except (TypeError, ValueError):
        return 0


def extract_analysis_output(data):
    output = data.get("output", data)

    if isinstance(output, dict):
        return output

    return {}


def create_analysis_dataframe(analysis_output):
    rows = []

    for filename, file_data in analysis_output.items():

        if not isinstance(file_data, dict):
            continue

        rows.append(
            {
                "File": filename,
                "Risk Level": get_risk_level(file_data),
                "Risk Score": get_risk_score(file_data),
                "Quality Score": file_data.get(
                    "quality_score", "N/A"
                ),
                "Line Count": file_data.get(
                    "line_count", "N/A"
                ),
                "Loop Count": file_data.get(
                    "loop_count", "N/A"
                ),
                "Complexity": file_data.get(
                    "complexity", "N/A"
                ),
                "Bugs": file_data.get(
                    "bugs", "N/A"
                ),
                "Recommendation": file_data.get(
                    "recommendation",
                    "No recommendation available."
                )
            }
        )

    return pd.DataFrame(rows)


def display_metric_card(
    label,
    value,
    icon,
    footer,
    accent_color="#60a5fa"
):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">
                {label}
                <span class="metric-icon">{icon}</span>
            </div>
            <div class="metric-value" style="color: {accent_color};">
                {value}
            </div>
            <div class="metric-footer">
                {footer}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-logo">🛡️</div>
            <div>
                <div class="sidebar-title">CodeSentinel</div>
                <div class="sidebar-subtitle">Developer Intelligence</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">Platform</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">📊 Repository Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🔥 Risk Prioritization</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🎯 Developer Action Plan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🔍 Code Complexity Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">Analysis Capabilities</div>',
        unsafe_allow_html=True
    )

    features = [
        "Multi-file Python analysis",
        "Syntax issue detection",
        "Complexity indicators",
        "Loop counting",
        "Nested loop detection",
        "Code quality scoring",
        "Risk classification",
        "Priority ranking"
    ]

    for feature in features:
        st.markdown(
            f'<div class="sidebar-feature">✓ {feature}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="sidebar-section">About</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "CodeSentinel helps developers analyze repositories "
        "and identify files that need attention first."
    )

    st.divider()

    st.caption("Version 1.0 • Repository Intelligence")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    """
    <div class="hero-container">
        <div class="hero-badge">● REPOSITORY INTELLIGENCE PLATFORM</div>
        <h1 class="hero-title">
            Analyze code.<br>
            <span>Prioritize risk.</span>
        </h1>
        <p class="hero-description">
            CodeSentinel analyzes public GitHub repositories,
            evaluates code complexity, detects risk indicators,
            ranks files by priority, and provides actionable
            engineering recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# REPOSITORY INPUT
# =========================================================

st.markdown(
    '<div class="section-heading">🔗 Connect a GitHub Repository</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Enter a public GitHub repository to begin automated analysis.'
    '</div>',
    unsafe_allow_html=True
)

input_col, button_col = st.columns([4, 1])

with input_col:

    repo_name = st.text_input(
        "Repository",
        placeholder="owner/repository  •  e.g. ShivanshiSharma05/CodeSentinel",
        label_visibility="collapsed"
    )

with button_col:

    analyze_button = st.button(
        "🚀 Analyze Repository",
        use_container_width=True
    )


# =========================================================
# ANALYSIS
# =========================================================

if analyze_button:

    if not repo_name.strip():

        st.warning(
            "Please enter a GitHub repository."
        )

    elif "/" not in repo_name.strip():

        st.error(
            "Invalid repository format. Use owner/repository."
        )

    else:

        repository = repo_name.strip()

        with st.spinner(
            "Fetching repository and analyzing source files..."
        ):

            try:

                response = requests.post(
                    BACKEND_URL,
                    json={"repo": repository},
                    timeout=180
                )

                if response.status_code != 200:

                    st.error(
                        f"Backend returned status code "
                        f"{response.status_code}."
                    )

                    try:
                        st.json(response.json())
                    except ValueError:
                        st.code(response.text)

                else:

                    data = response.json()

                    analysis_output = extract_analysis_output(data)

                    dataframe = create_analysis_dataframe(
                        analysis_output
                    )

                    if dataframe.empty:

                        st.warning(
                            "The backend returned no analyzable files."
                        )

                    else:

                        st.success(
                            "Repository analysis completed successfully."
                        )

                        # ---------------------------------------------
                        # SUMMARY VALUES
                        # ---------------------------------------------

                        total_files = len(dataframe)

                        high_risk = len(
                            dataframe[
                                dataframe["Risk Level"] == "HIGH"
                            ]
                        )

                        medium_risk = len(
                            dataframe[
                                dataframe["Risk Level"] == "MEDIUM"
                            ]
                        )

                        low_risk = len(
                            dataframe[
                                dataframe["Risk Level"] == "LOW"
                            ]
                        )

                        total_risk = high_risk + medium_risk

                        # ---------------------------------------------
                        # SUMMARY HEADER
                        # ---------------------------------------------

                        st.markdown(
                            '<div class="section-heading">'
                            '📊 Repository Overview'
                            '</div>',
                            unsafe_allow_html=True
                        )

                        st.caption(
                            f"Analysis results for: {repository}"
                        )

                        card_1, card_2, card_3, card_4 = st.columns(4)

                        with card_1:
                            display_metric_card(
                                "TOTAL FILES",
                                total_files,
                                "📁",
                                "Files analyzed",
                                "#60a5fa"
                            )

                        with card_2:
                            display_metric_card(
                                "HIGH RISK",
                                high_risk,
                                "🔴",
                                "Require immediate review",
                                "#f87171"
                            )

                        with card_3:
                            display_metric_card(
                                "MEDIUM RISK",
                                medium_risk,
                                "🟠",
                                "Should be reviewed",
                                "#fbbf24"
                            )

                        with card_4:
                            display_metric_card(
                                "LOW RISK",
                                low_risk,
                                "🟢",
                                "Currently lower risk",
                                "#4ade80"
                            )

                        # ---------------------------------------------
                        # TABS
                        # ---------------------------------------------

                        overview_tab, priority_tab, action_tab, detail_tab = (
                            st.tabs(
                                [
                                    "📈 Overview",
                                    "🔥 Priority Queue",
                                    "🎯 Action Plan",
                                    "🔍 File Details"
                                ]
                            )
                        )

                        # =============================================
                        # OVERVIEW TAB
                        # =============================================

                        with overview_tab:

                            chart_col, summary_col = st.columns(
                                [1.3, 1]
                            )

                            with chart_col:

                                st.markdown(
                                    '<div class="section-heading">'
                                    'Risk Distribution'
                                    '</div>',
                                    unsafe_allow_html=True
                                )

                                risk_counts = pd.Series(
                                    {
                                        "High": high_risk,
                                        "Medium": medium_risk,
                                        "Low": low_risk
                                    }
                                )

                                if risk_counts.sum() > 0:

                                    fig, ax = plt.subplots(
                                        figsize=(7, 4.5)
                                    )

                                    fig.patch.set_facecolor(
                                        "#111827"
                                    )

                                    ax.set_facecolor("#111827")

                                    ax.pie(
                                        risk_counts.values,
                                        labels=risk_counts.index,
                                        autopct="%1.1f%%",
                                        startangle=90,
                                        textprops={
                                            "color": "white"
                                        }
                                    )

                                    ax.set_title(
                                        "Repository Risk Distribution",
                                        color="white",
                                        pad=15
                                    )

                                    st.pyplot(
                                        fig,
                                        use_container_width=True
                                    )

                                    plt.close(fig)

                            with summary_col:

                                st.markdown(
                                    '<div class="section-heading">'
                                    'Analysis Summary'
                                    '</div>',
                                    unsafe_allow_html=True
                                )

                                summary_df = pd.DataFrame(
                                    {
                                        "Risk Category": [
                                            "High",
                                            "Medium",
                                            "Low"
                                        ],
                                        "Files": [
                                            high_risk,
                                            medium_risk,
                                            low_risk
                                        ]
                                    }
                                )

                                st.dataframe(
                                    summary_df,
                                    use_container_width=True,
                                    hide_index=True
                                )

                                st.info(
                                    f"{total_risk} file(s) require "
                                    "additional review based on "
                                    "their assigned risk level."
                                )

                        # =============================================
                        # PRIORITY QUEUE TAB
                        # =============================================

                        with priority_tab:

                            st.markdown(
                                '<div class="section-heading">'
                                '🔥 Developer Priority Queue'
                                '</div>',
                                unsafe_allow_html=True
                            )

                            st.caption(
                                "Files are ordered by risk score, "
                                "with higher scores appearing first."
                            )

                            priority_df = dataframe.sort_values(
                                by="Risk Score",
                                ascending=False
                            )

                            priority_columns = [
                                "File",
                                "Risk Level",
                                "Risk Score",
                                "Quality Score",
                                "Complexity",
                                "Line Count"
                            ]

                            available_columns = [
                                column
                                for column in priority_columns
                                if column in priority_df.columns
                            ]

                            st.dataframe(
                                priority_df[available_columns],
                                use_container_width=True,
                                hide_index=True
                            )

                        # =============================================
                        # ACTION PLAN TAB
                        # =============================================

                        with action_tab:

                            st.markdown(
                                '<div class="section-heading">'
                                '🎯 Developer Action Plan'
                                '</div>',
                                unsafe_allow_html=True
                            )

                            st.caption(
                                "Use these categories to organize "
                                "engineering review priorities."
                            )

                            fix_now = dataframe[
                                dataframe["Risk Level"] == "HIGH"
                            ]

                            improve_soon = dataframe[
                                dataframe["Risk Level"] == "MEDIUM"
                            ]

                            healthy = dataframe[
                                dataframe["Risk Level"] == "LOW"
                            ]

                            with st.expander(
                                "🔴 Fix Immediately",
                                expanded=True
                            ):

                                if fix_now.empty:

                                    st.success(
                                        "No high-risk files detected."
                                    )

                                else:

                                    for _, row in fix_now.iterrows():

                                        st.markdown(
                                            f"**{row['File']}**"
                                        )

                                        st.write(
                                            f"Risk Score: "
                                            f"`{row['Risk Score']}`"
                                        )

                                        st.caption(
                                            str(row["Recommendation"])
                                        )

                                        st.divider()

                            with st.expander(
                                "🟠 Improve Soon",
                                expanded=True
                            ):

                                if improve_soon.empty:

                                    st.success(
                                        "No medium-risk files detected."
                                    )

                                else:

                                    for _, row in improve_soon.iterrows():

                                        st.markdown(
                                            f"**{row['File']}**"
                                        )

                                        st.write(
                                            f"Risk Score: "
                                            f"`{row['Risk Score']}`"
                                        )

                                        st.caption(
                                            str(row["Recommendation"])
                                        )

                                        st.divider()

                            with st.expander(
                                "🟢 Healthy Files",
                                expanded=False
                            ):

                                if healthy.empty:

                                    st.info(
                                        "No low-risk files detected."
                                    )

                                else:

                                    for _, row in healthy.iterrows():

                                        st.markdown(
                                            f"**{row['File']}**"
                                        )

                                        st.write(
                                            f"Risk Score: "
                                            f"`{row['Risk Score']}`"
                                        )

                                        st.caption(
                                            str(row["Recommendation"])
                                        )

                                        st.divider()

                        # =============================================
                        # FILE DETAILS TAB
                        # =============================================

                        with detail_tab:

                            st.markdown(
                                '<div class="section-heading">'
                                '🔍 Detailed File Analysis'
                                '</div>',
                                unsafe_allow_html=True
                            )

                            selected_file = st.selectbox(
                                "Select a file",
                                dataframe["File"].tolist()
                            )

                            selected_rows = dataframe[
                                dataframe["File"] == selected_file
                            ]

                            if not selected_rows.empty:

                                row = selected_rows.iloc[0]

                                detail_col_1, detail_col_2 = st.columns(2)

                                with detail_col_1:

                                    st.markdown(
                                        "#### File Information"
                                    )

                                    st.write(
                                        f"**File:** {row['File']}"
                                    )

                                    st.write(
                                        f"**Risk Level:** "
                                        f"{row['Risk Level']}"
                                    )

                                    st.write(
                                        f"**Risk Score:** "
                                        f"{row['Risk Score']}"
                                    )

                                    st.write(
                                        f"**Quality Score:** "
                                        f"{row['Quality Score']}"
                                    )

                                with detail_col_2:

                                    st.markdown(
                                        "#### Code Metrics"
                                    )

                                    st.write(
                                        f"**Line Count:** "
                                        f"{row['Line Count']}"
                                    )

                                    st.write(
                                        f"**Loop Count:** "
                                        f"{row['Loop Count']}"
                                    )

                                    st.write(
                                        f"**Complexity:** "
                                        f"{row['Complexity']}"
                                    )

                                    st.write(
                                        f"**Bugs:** {row['Bugs']}"
                                    )

                                st.markdown(
                                    "#### 💡 Recommendation"
                                )

                                st.info(
                                    str(row["Recommendation"])
                                )

                        # ---------------------------------------------
                        # COMPLETE DATASET
                        # ---------------------------------------------

                        with st.expander(
                            "📋 View Complete Analysis Dataset"
                        ):

                            st.dataframe(
                                dataframe,
                                use_container_width=True,
                                hide_index=True
                            )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Could not connect to the FastAPI backend. "
                    "Start the backend using: "
                    "`uvicorn main:app --reload`"
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out. "
                    "Try analyzing a smaller repository."
                )

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Request error: {error}"
                )

            except Exception as error:

                st.error(
                    f"Unexpected error: {error}"
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🛡️ CodeSentinel &nbsp;•&nbsp;
        Repository Risk & Change Intelligence Platform
        <br>
        Automated analysis for better engineering decisions
    </div>
    """,
    unsafe_allow_html=True
)