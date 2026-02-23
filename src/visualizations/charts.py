import plotly.express as px
import plotly.graph_objects as go

def plot_bar_chart(df, x_col, y_col, title, color_discrete_sequence=None):
    if df is None or df.empty:
        return None
    fig = px.bar(df, x=x_col, y=y_col, title=title, color_discrete_sequence=color_discrete_sequence)
    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    return fig

def plot_line_chart(df, x_col, y_col, title):
    if df is None or df.empty:
        return None
    fig = px.line(df, x=x_col, y=y_col, title=title, markers=True)
    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    return fig

def plot_pie_chart(labels, values, title):
    if not labels or not values:
        return None
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title_text=title, template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    return fig
