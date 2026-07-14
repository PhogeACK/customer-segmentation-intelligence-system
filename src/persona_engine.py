CLUSTER_PERSONAS = {

    0: {
        "segment_name": "Dormant Low-Value Customers",
        "behavior": (
            "Low spending, weak purchasing activity, "
            "low engagement across channels, "
            "minimal campaign responsiveness"
        ),
        "business_value": (
            "Low immediate revenue contribution "
            "but potential reactivation opportunity"
        ),
        "recommended_action": (
            "Launch re-engagement campaigns, "
            "simplified offers, and low-cost "
            "retention workflows"
        )
    },

    1: {
        "segment_name": "Active Omni-Channel Customers",
        "behavior": (
            "Strong purchasing activity across web, "
            "catalog, and store channels with "
            "balanced engagement"
        ),
        "business_value": (
            "Stable and valuable customer base "
            "with consistent activity"
        ),
        "recommended_action": (
            "Maintain engagement through personalized "
            "recommendations and cross-channel marketing"
        )
    },

    2: {
        "segment_name": "Premium Loyal Customers",
        "behavior": (
            "High spending behavior, strong catalog purchases, "
            "high engagement, premium behavioral profile"
        ),
        "business_value": (
            "High customer lifetime value and "
            "strong retention potential"
        ),
        "recommended_action": (
            "Prioritize loyalty programs, "
            "exclusive offers, and premium "
            "customer experiences"
        )
    },

    3: {
        "segment_name": "Family Budget Customers",
        "behavior": (
            "Family-oriented purchasing patterns "
            "with lower overall spending and "
            "moderate engagement"
        ),
        "business_value": (
            "Moderate long-term value with "
            "price-sensitive behavior"
        ),
        "recommended_action": (
            "Promote bundles, family-oriented offers, "
            "and value-driven campaigns"
        )
    },

    4: {
        "segment_name": "Deal-Driven Customers",
        "behavior": (
            "High promotion and discount sensitivity, "
            "active deal purchasing behavior"
        ),
        "business_value": (
            "Strong transactional activity "
            "but potentially lower margins"
        ),
        "recommended_action": (
            "Use targeted discounts, flash sales, "
            "and promotion-based automations "
            "strategically"
        )
    },

    5: {
        "segment_name": "VIP Campaign Responders",
        "behavior": (
            "Extremely high campaign responsiveness "
            "combined with strong spending behavior"
        ),
        "business_value": (
            "Highly marketable and highly responsive "
            "premium segment"
        ),
        "recommended_action": (
            "Trigger VIP workflows, early-access campaigns, "
            "premium retention strategies, and "
            "high-priority personalization"
        )
    }
}


def enrich_cluster_output(cluster_id):

    return CLUSTER_PERSONAS.get(
        cluster_id,
        {
            "segment_name": "Unknown Segment",
            "behavior": "Unknown",
            "business_value": "Unknown",
            "recommended_action": "Manual review required"
        }
    )