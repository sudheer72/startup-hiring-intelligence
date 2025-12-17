def score_startup(row):
    score = 0
    reasons = []

    amount = row.get("Amount (USD)", 0) or 0
    hiring_tier = str(row.get("Hiring Tier", "")).upper()
    tech_roles = row.get("Tech Roles", 0) or 0

    # Funding score
    if amount >= 100_000_000:
        score += 40
        reasons.append("Large funding")
    elif amount >= 50_000_000:
        score += 30
        reasons.append("Strong funding")
    elif amount >= 20_000_000:
        score += 20
        reasons.append("Moderate funding")

    # Hiring tier score
    if hiring_tier == "A":
        score += 40
        reasons.append("High hiring tier")
    elif hiring_tier == "B":
        score += 20
        reasons.append("Medium hiring tier")

    # Tech roles
    if tech_roles >= 10:
        score += 20
        reasons.append("Many tech roles")
    elif tech_roles >= 3:
        score += 10
        reasons.append("Some tech roles")

    # Priority label
    if score >= 70:
        priority = "High Priority"
    elif score >= 40:
        priority = "Medium Priority"
    else:
        priority = "Low Priority"

    return score, priority, ", ".join(reasons)
