def detect_fake(job_text):
    red_flags = [
        "application fee",
        "pay to apply",
        "send money",
        "telegram group",
        "bank details",
        "no experience required",
        "earn thousands quickly",
        "work from home and get rich"
    ]
    
    score = 0
    for flag in red_flags:
        if flag in job_text.lower():
            score += 1

    if score >= 2:
        return "❌ Likely Fake Job/Internship"
    elif score == 1:
        return "⚠️ Suspicious — Be Careful"
    else:
        return "✅ Looks Genuine (but always double-check!)"
