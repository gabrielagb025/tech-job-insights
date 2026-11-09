import plotly.express as px

BAR_COLOR = "#8C9BD8"
DONUT_COLORS = ["#8C9BD8", "#BBAEE3", "#A8D0E6"]
TEXT_COLOR = "#2F2A26"


def _style(fig):
    """Apply the shared look to a figure: transparent background and dark text."""
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color=TEXT_COLOR, title_x=0, height=380)
    return fig


def technology_demand_chart(df):
    """Horizontal bar chart with the number of job offers per technology."""
    counts = df["Main Technology"].value_counts().reset_index(name="Offers")
    fig = px.bar(
        counts,
        x="Offers",
        y="Main Technology",
        orientation="h",
        text_auto=True,
        labels={"Main Technology": "", "Offers": "Number of offers"},
        title="Most in-demand technologies",
        color_discrete_sequence=[BAR_COLOR],
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_xaxes(visible=False)
    return _style(fig)


def salary_by_level_chart(df):
    """Box plot with the salary distribution for each experience level."""
    fig = px.box(
        df,
        x="Experience Level",
        y="Salary (EUR)",
        category_orders={"Experience Level": ["Junior", "Mid", "Senior"]},
        labels={"Experience Level": "Experience level"},
        title="Salary by experience level",
        color_discrete_sequence=[BAR_COLOR],
    )
    return _style(fig)


def work_mode_chart(df):
    """Donut chart with the share of offers per work mode."""
    counts = df["Work Mode"].value_counts().reset_index(name="Offers")
    fig = px.pie(
        counts,
        names="Work Mode",
        values="Offers",
        hole=0.5,
        title="Work mode",
        color_discrete_sequence=DONUT_COLORS,
    )
    fig.update_traces(textposition="outside", textinfo="percent", textfont_color=TEXT_COLOR)
    return _style(fig)