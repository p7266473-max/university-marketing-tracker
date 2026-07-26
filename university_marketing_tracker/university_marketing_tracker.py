import reflex as rx
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re

# --- Theme Constants ---
PRIMARY_NAVY = "#0B1F3A"
ROYAL_BLUE = "#0F4C81"
GOLD_ACCENT = "#D4AF37"
LIGHT_BG = "#F8FAFC"
WHITE = "#FFFFFF"
TEXT_PRIMARY = "#1F2937"
TEXT_MOBILE = "#000000"  # High contrast for mobile

CARD_STYLE = {
    "background_color": WHITE,
    "border_radius": "12px",
    "box_shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
    "padding": "24px",
    "border_top": f"4px solid {GOLD_ACCENT}",
}

# --- Detailed Data Structures ---
WEEK_1_DATA = [
    {"Staff Name": "Dato' Gilbert", "FB": "17th (PhD(ODL))", "LinkedIn": "17th (PhD(ODL))", "Telegram": "-", "WhatsApp Status": "17th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "17th (PhD(ODL))", "Remarks": ""},
    {"Staff Name": "Mr Uthia Kumar Subramany", "FB": "-", "LinkedIn": "17th (PhD(ODL))", "Telegram": "-", "WhatsApp Status": "17th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Prof. Dr. Asif M Karim", "FB": "-", "LinkedIn": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "WhatsApp Group": "17th, 18th (DBA RM, SL, PDC AI 1, 2, 3)", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mrs. Gurvinder", "FB": "-", "LinkedIn": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr. Muhammed Irfan A", "FB": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "LinkedIn": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms. Rozmania", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms Lini", "FB": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr SK", "FB": "18th (PhD(ODL))", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms Nurul Fatiha", "FB": "18th (Exec MBA, PhD(ODL))", "LinkedIn": "18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mrs. Vani", "FB": "18th (Exec MBA)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": ""},
    {"Staff Name": "Mr Jegen", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": ""}
]

WEEK_2_DATA = [
    {"Staff Name": "Dato' Gilbert", "FB": "22th (PhD(ODL),25th Prem Msc ITM) 25th (PhD(ODL)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "22th (PhD(OD25th Prem Msc ITM) 25th (PhD(ODL) L)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr Uthia Kumar Subramany", "FB": "-", "LinkedIn": "21th Prem Msc ITM) 23th (PhD(ODL)", "Telegram": "-", "WhatsApp Status": "21th Prem Msc ITM) 24th Prem Msc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Prof. Dr. Asif M Karim", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "25th 26th Prem Msc ITM) (PhD(ODL)", "WhatsApp Group": "25th 26th Prem Msc ITM) (PhD(ODL)", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mrs. Gurvinder", "FB": "25th Prem Msc ITM) 25th (PhD(ODL)", "LinkedIn": "25th Prem Msc ITM) 25th (PhD(ODL)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr. Muhammed Irfan A", "FB": "25th Prem Msc ITM) 18th, 25th (PhD(ODL)", "LinkedIn": "25th Prem Msc ITM) 25th (PhD(ODL)", "Telegram": "25th Prem Msc ITM", "WhatsApp Status": "23,24,25th Prem Msc ITM) (PhD(ODL)", "WhatsApp Group": "-", "Instagram": "25th Prem Msc ITM) 25th (PhD(ODL)", "Remarks": "-"},
    {"Staff Name": "Ms. Rozmania", "FB": "24th Prem Msc ITM) (PhD(ODL)", "LinkedIn": "24th Prem Msc ITM) (PhD(ODL)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms Lini", "FB": "26h Prem Msc ITM) 26h (PhD(ODL)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr SK", "FB": "26h Prem Msc ITM) 26h (PhD(ODL)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "26h Prem Msc ITM) 26h (PhD(ODL)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms Nurul Fatiha", "FB": "22th Prem Msc ITM) 22th (PhD(ODL)", "LinkedIn": "22th Prem Msc ITM) 22th (PhD(ODL)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mrs. Vani", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "26h Prem Msc ITM) 26h (PhD(ODL)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": ""},
    {"Staff Name": "Mr Jegen", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": ""}
]

def count_posts_in_string(text: str) -> int:
    if not text or text == "-": return 0
    dates = re.findall(r"\b\d{1,2}(?:th|h|nd|rd)\b", text)
    return len(dates) if dates else (1 if text.strip() else 0)

# --- State Management ---
class State(rx.State):
    selected_week: str = "Week 1"
    @rx.event
    def set_selected_week(self, week: str): self.selected_week = week
    
    @rx.var
    def week_dates(self) -> str:
        if self.selected_week == "Week 1": return "July 17-18, 2026"
        return "July 20-26, 2026"

    @rx.var
    def get_data(self) -> list[dict]:
        if self.selected_week == "Week 1": return WEEK_1_DATA
        return WEEK_2_DATA

    @rx.var
    def get_chart_data(self) -> go.Figure:
        data = self.get_data
        staff_counts = {}
        for entry in data:
            staff = entry["Staff Name"]; posts = 0
            for col in ["FB", "LinkedIn", "Telegram", "WhatsApp Status", "WhatsApp Group", "Instagram"]:
                posts += count_posts_in_string(entry[col])
            staff_counts[staff] = staff_counts.get(staff, 0) + posts
        df = pd.DataFrame({"Staff Name": list(staff_counts.keys()), "Total Posts": list(staff_counts.values())})
        fig = px.bar(df, x="Staff Name", y="Total Posts", title=f"Posts - {self.selected_week} ({self.week_dates})", color_discrete_sequence=[ROYAL_BLUE])
        fig.update_layout(plot_bgcolor=LIGHT_BG, paper_bgcolor=WHITE, font_family="Inter", margin=dict(t=40, b=40, l=40, r=40))
        return fig

    @rx.var
    def get_performance_list(self) -> list[dict]:
        data = self.get_data
        perf = []
        for entry in data:
            posts = 0
            for col in ["FB", "LinkedIn", "Telegram", "WhatsApp Status", "WhatsApp Group", "Instagram"]:
                posts += count_posts_in_string(entry[col])
            width_val = f"{(posts * 10)}%" if posts > 0 else "4px"
            perf.append({"name": entry["Staff Name"], "count": str(posts), "bar_width": width_val})
        return perf

# --- UI Components ---
def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.icon(tag="building-2", color=GOLD_ACCENT, size=30),
                rx.heading("Binary University", size=rx.breakpoints(initial="4", sm="6"), color=WHITE, weight="bold"),
                align="center",
            ),
            href="https://binary.edu.my/", is_external=True,
        ),
        padding_x=["1em", "4em"], padding_y="1em", background_color=PRIMARY_NAVY, width="100%", border_bottom=f"4px solid {GOLD_ACCENT}",
    )

def executive_card(title: str, content: rx.Component) -> rx.Component:
    return rx.card(
        rx.vstack(rx.heading(title, size="4", color=PRIMARY_NAVY, margin_bottom="0.5em"), content, align="start", width="100%"),
        style=CARD_STYLE, width="100%",
    )

def usp_card(title: str, description: str) -> rx.Component:
    return rx.card(
        rx.vstack(rx.heading(title, size="4", color=PRIMARY_NAVY, weight="bold"), rx.text(description, size="2", color=TEXT_PRIMARY), align="start", spacing="2"),
        style=CARD_STYLE, width="100%",
    )

# --- Responsive Wrappers ---
def desktop_overview():
    return rx.desktop_only(
        rx.vstack(
            rx.heading("Binary University Internal Marketing Team Dashboard", size="9", color=PRIMARY_NAVY),
            rx.divider(border_color=GOLD_ACCENT, width="100px", border_width="4px", margin_y="1em"),
            executive_card("Why is Binary University Asia's Most Exclusive University?", rx.vstack(
                rx.text("Unlike mass-market institutions, Binary University is a highly specialized, boutique university that strictly limits cohorts exclusively to 45 students per Master's, DBA, and PhD program.", color=TEXT_PRIMARY, size="3", font_style="italic"),
                rx.text("By employing the unique Industry Specialist Professional (ISP) curriculum and leveraging a network of over 1,280 faculty practitioners, Binary graduates are developed as highly-demanded 'Outstanding Talents'.", color=TEXT_PRIMARY, size="3", margin_top="0.5em"),
                align="start"
            )),
            rx.heading("Our 5 Premier USPs", size="7", color=PRIMARY_NAVY, margin_y="1em"),
            rx.grid(
                usp_card("1. ISP: Industry Specialist Professionals", "Acquisition of deep, industry-specific skills from over 1280 Faculty of Industry Professionals transforming students into highly demanded Talents."),
                usp_card("2. BEE: Binary Entrepreneurship Ecosystem thro' ACE", "Creating Entrepreneurial Mindset Professionals with innovative problem solving and creative thinking skills nurtured through the Asia Centre for Entrepreneurship (ACE) which has over 10,500 real entrepreneurs."),
                usp_card("3. WOCA: The World Is Our Campus", "Curated study-abroad experience at another world-class university in Asia to open more career opportunities."),
                usp_card("4. LII: Learning In Industry", "True mastery happens beyond classrooms. Thro's LII, students meet leaders and shapers of industries. Real-world insights through industry visits and CEO engagements."),
                usp_card("5. BTI: Guaranteed Internships with Premium Allowance", "Guaranteed allowance of 300% higher than other universities ( RM 3000 for Masters & RM 2000 for Bachelors)."),
                columns="2", spacing="4", width="100%",
            ),
            width="100%", padding="2em", align="center",
        )
    )

def mobile_overview():
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.heading("Internal Marketing Dashboard", size="6", color=PRIMARY_NAVY, text_align="center"),
            rx.divider(border_color=GOLD_ACCENT, width="60px", border_width="3px"),
            rx.card(
                rx.text("Asia's Most Exclusive University: Specialized boutique environment limited to 45 students per cohort.", size="2", font_style="italic", color=TEXT_MOBILE),
                style=CARD_STYLE, width="100%",
            ),
            rx.vstack(
                usp_card("1. ISP: Industry Specialist Professionals", "Acquisition of deep, industry-specific skills from over 1280 Faculty of Industry Professionals."),
                usp_card("2. BEE: Binary Entrepreneurship Ecosystem", "Creating Entrepreneurial Mindset Professionals nurtured through the Asia Centre for Entrepreneurship (ACE)."),
                usp_card("3. WOCA: The World Is Our Campus", "Curated study-abroad experience at another world-class university in Asia."),
                usp_card("4. LII: Learning In Industry", "True mastery happens beyond classrooms through CEO engagements and industry visits."),
                usp_card("5. BTI: Guaranteed Internships", "Guaranteed allowance of 300% higher than other universities."),
                width="100%", spacing="3",
            ),
            width="100%", padding="1em", align="center",
        )
    )

def desktop_tracker():
    return rx.desktop_only(
        rx.vstack(
            rx.heading("Marketing Activity Tracker", size="6", color=PRIMARY_NAVY),
            rx.text(State.week_dates, size="4", color=GOLD_ACCENT, weight="medium", margin_bottom="1em"),
            rx.select(["Week 1", "Week 2", "Combined"], value=State.selected_week, on_change=State.set_selected_week),
            rx.box(
                rx.table.root(
                    rx.table.header(rx.table.row(rx.table.column_header_cell("Staff"), rx.table.column_header_cell("FB"), rx.table.column_header_cell("LinkedIn"), rx.table.column_header_cell("Telegram"), rx.table.column_header_cell("WA Status"), rx.table.column_header_cell("WA Group"), rx.table.column_header_cell("Instagram"), rx.table.column_header_cell("Remarks"))),
                    rx.table.body(rx.foreach(State.get_data, lambda row: rx.table.row(rx.table.cell(row["Staff Name"]), rx.table.cell(row["FB"]), rx.table.cell(row["LinkedIn"]), rx.table.cell(row["Telegram"]), rx.table.cell(row["WhatsApp Status"]), rx.table.cell(row["WhatsApp Group"]), rx.table.cell(row["Instagram"]), rx.table.cell(row["Remarks"])))),
                    width="100%",
                ),
                width="100%", overflow_x="auto",
            ),
            padding="2em", width="100%",
        )
    )

def mobile_tracker():
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.heading("Activity Tracker", size="5", color=PRIMARY_NAVY),
            rx.text(State.week_dates, size="2", color=GOLD_ACCENT, weight="bold"),
            rx.select(["Week 1", "Week 2"], value=State.selected_week, on_change=State.set_selected_week),
            rx.scroll_area(
                rx.vstack(
                    rx.foreach(State.get_data, lambda row: rx.card(
                        rx.vstack(
                            rx.heading(row["Staff Name"], size="3", color=ROYAL_BLUE),
                            rx.vstack(
                                rx.hstack(rx.text("Facebook:", size="1", weight="bold", color=TEXT_MOBILE, width="100px"), rx.text(row["FB"], size="1", color=TEXT_MOBILE)),
                                rx.hstack(rx.text("LinkedIn:", size="1", weight="bold", color=TEXT_MOBILE, width="100px"), rx.text(row["LinkedIn"], size="1", color=TEXT_MOBILE)),
                                rx.hstack(rx.text("WA Status:", size="1", weight="bold", color=TEXT_MOBILE, width="100px"), rx.text(row["WhatsApp Status"], size="1", color=TEXT_MOBILE)),
                                rx.hstack(rx.text("WA Group:", size="1", weight="bold", color=TEXT_MOBILE, width="100px"), rx.text(row["WhatsApp Group"], size="1", color=TEXT_MOBILE)),
                                rx.hstack(rx.text("Instagram:", size="1", weight="bold", color=TEXT_MOBILE, width="100px"), rx.text(row["Instagram"], size="1", color=TEXT_MOBILE)),
                                align="start", spacing="0", width="100%",
                            ),
                            align="start", spacing="2",
                        ),
                        padding="12px", border_top=f"2px solid {GOLD_ACCENT}", width="100%",
                    )),
                    width="100%", spacing="2",
                ),
                height="60vh", width="100%",
            ),
            padding="1em", width="100%",
        )
    )

def static_mobile_performance():
    return rx.mobile_and_tablet(
        rx.vstack(
            rx.heading("Performance Overview", size="5", color=PRIMARY_NAVY),
            rx.text(State.week_dates, size="2", color=GOLD_ACCENT, weight="bold"),
            rx.text("Static performance breakdown for mobile stability.", size="1", color=TEXT_MOBILE),
            rx.scroll_area(
                rx.vstack(
                    rx.foreach(
                        State.get_performance_list,
                        lambda item: rx.vstack(
                            rx.hstack(
                                rx.text(item["name"], size="1", weight="bold", color=TEXT_MOBILE),
                                rx.spacer(),
                                rx.text(item["count"], size="1", color=TEXT_MOBILE),
                                width="100%",
                            ),
                            rx.box(
                                background_color=ROYAL_BLUE,
                                height="8px",
                                width=item["bar_width"],
                                border_radius="4px",
                            ),
                            width="100%", spacing="1",
                        )
                    ),
                    width="100%", spacing="4",
                ),
                height="50vh", width="100%",
            ),
            padding="1em", width="100%",
        )
    )

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.tabs.root(
            rx.tabs.list(rx.tabs.trigger("🏠 Overview", value="1"), rx.tabs.trigger("📊 Tracker", value="2"), rx.tabs.trigger("📈 Performance", value="3")),
            rx.tabs.content(rx.fragment(desktop_overview(), mobile_overview()), value="1"),
            rx.tabs.content(rx.fragment(desktop_tracker(), mobile_tracker()), value="2"),
            rx.tabs.content(
                rx.fragment(
                    rx.desktop_only(
                        rx.vstack(
                            rx.heading("Performance Analytics", size="6", color=PRIMARY_NAVY),
                            rx.text(State.week_dates, size="4", color=GOLD_ACCENT, weight="medium"),
                            rx.plotly(data=State.get_chart_data, height="500px", width="100%"),
                            padding="2em", width="100%"
                        )
                    ),
                    static_mobile_performance()
                ), 
                value="3"
            ),
            default_value="1", width="100%", padding_x=["0.5em", "4em"],
        ),
        background_color=LIGHT_BG, min_height="100vh", width="100%",
    )

app = rx.App(theme=rx.theme(accent_color="blue", gray_color="slate", radius="large"))
app.add_page(index, route="/")
