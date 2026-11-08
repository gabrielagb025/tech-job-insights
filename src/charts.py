import plotly.express as px


def technology_demand_chart(df):
    """Bar chart with the number of job offers per technology."""
    counts = df["Main Technology"].value_counts().reset_index(name="Offers")
    return px.bar(counts, x="Main Technology", y="Offers", title="Most in-demand technologies")


def salary_by_level_chart(df):
    """Box plot with the salary distribution for each experience level."""
    return px.box(
        df,
        x="Experience Level",
        y="Salary (EUR)",
        category_orders={"Experience Level": ["Junior", "Mid", "Senior"]},
        title="Salary by experience level",
    )


def work_mode_chart(df):
    """Donut chart with the share of offers per work mode."""
    counts = df["Work Mode"].value_counts().reset_index(name="Offers")
    return px.pie(counts, names="Work Mode", values="Offers", hole=0.5, title="Work mode")
