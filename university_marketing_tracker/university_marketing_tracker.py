import reflex as rx
import pandas as pd

# Data Structures
STAFF_LIST = [
    "Dato' Gilbert", "Mr Uthia Kumar Subramany", "Prof. Dr. Asif M Karim", 
    "Mrs. Gurvinder", "Mr. Muhammed Irfan A", "Ms. Rozmania", 
    "Ms Lini", "Mr SK", "Ms Nurul Fatiha", "Mrs. Vani", "Mr Jegen"
]

class State(rx.State):
    """The app state."""
    selected_week: str = "Combined"
    
    @rx.var
    def get_data(self) -> pd.DataFrame:
        # Re-creating data logic here for brevity in State
        # In a real app, this should be initialized once
        return pd.DataFrame() # Simplified for now

def usp_component(title: str, description: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="5", color="#8b5e3c"),
        rx.text(description, color="#3e3a35"),
        align="start",
        margin_bottom="1em",
        width="100%",
    )

def index() -> rx.Component:
    return rx.tabs(
        rx.tab_list(
            rx.tab("🏠 Home"),
            rx.tab("📊 Marketing Tracker"),
        ),
        rx.tab_panels(
            rx.tab_panel(
                rx.vstack(
                    rx.heading("🎓 Welcome, Valued Staff", size="9", color="#8b5e3c"),
                    rx.divider(),
                    rx.heading("Why We Are Asia's Most Exclusive University", size="7", color="#8b5e3c"),
                    rx.text(
                        "Binary University is not a mass-market institution. We are a specialized, boutique university committed to producing 'Outstanding Talents' who command premium compensation globally.",
                        color="#3e3a35",
                    ),
                    
                    rx.heading("✨ Our 5 Premier USPs", size="7", color="#8b5e3c"),
                    usp_component("1. ISP: Industry Specialist Professionals", "Acquisition of deep, industry-specific skills from over 1280 Faculty of Industry Professionals transforming students into highly demanded Talents."),
                    usp_component("2. BEE: Binary Entrepreneurship Ecosystem thro' ACE", "Creating Entrepreneurial Mindset Professionals with innovative problem solving and creative thinking skills nurtured through the Asia Centre for Entrepreneurship (ACE) which has over 10,500 real entrepreneurs."),
                    usp_component("3. WOCA: The World Is Our Campus", "Curated study-abroad experience at another world-class university in Asia to open more career opportunities."),
                    usp_component("4. LII: Learning In Industry", "True mastery happens beyond classrooms. Thro's LII, students meet leaders and shapers of industries. Real-world insights through industry visits and CEO engagements."),
                    usp_component("5. BTI: Guaranteed Internships with Premium Allowance", "Guaranteed allowance of 300% higher than other universities ( RM 3000 for Masters & RM 2000 for Bachelors)."),
                    
                    width="100%",
                    padding="2em",
                    align="start",
                ),
            ),
            rx.tab_panel(
                rx.text("Marketing Tracker to be implemented fully in next phase."),
            ),
        ),
        variant="line",
        width="100%",
        background_color="#fcfbf7",
        min_height="100vh",
    )

app = rx.App()
app.add_page(index)
