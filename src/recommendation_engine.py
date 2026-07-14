# recommendation_engine.py

RECOMMENDATION_RULES = {

    "Dormant Low-Value Customers": {
        "primary_goal": "Reactivate inactive customers",
        "opportunity": "Recover lost purchasing activity",
        "risk": "Customer disengagement and churn",
        "recommended_campaign": "Customer Re-Engagement Campaign"
    },

    "Active Omni-Channel Customers": {
        "primary_goal": "Increase cross-channel engagement",
        "opportunity": "Cross-sell relevant products",
        "risk": "Gradual reduction in engagement across channels",
        "recommended_campaign": "Personalized Cross-Channel Recommendations"
    },

    "Premium Loyal Customers": {
        "primary_goal": "Maximize customer lifetime value",
        "opportunity": "Upsell premium products and loyalty benefits",
        "risk": "Loss of high-value customers to competitors",
        "recommended_campaign": "VIP Loyalty Program"
    },

    "Family Budget Customers": {
        "primary_goal": "Increase basket size",
        "opportunity": "Promote bundled purchases",
        "risk": "Price-sensitive behavior reducing spend",
        "recommended_campaign": "Family Bundle Promotions"
    },

    "Deal-Driven Customers": {
        "primary_goal": "Increase profitability",
        "opportunity": "Reduce discount dependency",
        "risk": "Low margins caused by excessive discount usage",
        "recommended_campaign": "Minimum-Spend Promotion Campaign"
    },

    "VIP Campaign Responders": {
        "primary_goal": "Maximize campaign ROI",
        "opportunity": "Leverage high campaign responsiveness",
        "risk": "Overcommunication causing fatigue",
        "recommended_campaign": "VIP Early-Access Campaign"
    }
}


def get_recommendation(segment_name):
    """
    Return recommendation package
    for a customer segment.
    """

    return RECOMMENDATION_RULES.get(
        segment_name,
        {
            "primary_goal": "Unknown",
            "opportunity": "Unknown",
            "risk": "Unknown",
            "recommended_campaign": "Unknown"
        }
    )