"""AI Business Engine — Pricing Calculator."""

def calculate_content_studio_price(posts_per_month: int, include_graphics: bool = True, include_video: bool = False):
    base = posts_per_month * 125  # R125 per post
    if include_graphics:
        base += posts_per_month * 50  # R50 per graphic
    if include_video:
        base += 2000 * posts_per_month  # R2000 per video script
    return base


def calculate_automation_retainer(automations: int, has_monitoring: bool = True):
    base = automations * 1000  # R1,000 per automation
    if has_monitoring:
        base += automations * 300  # R300 monitoring fee
    return base


def calculate_consulting_package(package: str, hours: int, on_site: bool = False):
    rates = {"bronze": 1500, "silver": 4000, "gold": 8000}
    base = rates.get(package.lower(), 1500)
    if on_site:
        base += 500  # travel fee
    return base


def calculate_workshop_revenue(price_per_pax: float, num_pax: int, is_corporate: bool = False):
    if is_corporate:
        return max(10000, price_per_pax * num_pax)
    return price_per_pax * num_pax


def print_business_plan(target_monthly_income: float = 50000):
    print(f"""
╔══════════════════════════════════════════════════╗
║       AI BUSINESS ENGINE — INCOME PLAN            ║
║       Target: R{target_monthly_income:,.0f}/month            ║
╚══════════════════════════════════════════════════╝

Income Stacking Strategy:

1. AI Content Studio:   3 clients @ R4,000 = R12,000
2. AI Automation Agency: 4 clients @ R2,000 = R8,000
3. AI Digital Products:  50 sales @ R100   = R5,000
4. AI SMME Consulting:   2 clients @ R6,000 = R12,000
5. AI Training:          2 workshops @ R8,000 = R16,000
                                         ─────────
                           Total:       R53,000/month
""")

if __name__ == "__main__":
    print_business_plan()
