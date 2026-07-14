# workflow_engine.py

WORKFLOW_RULES = {

    "Dormant Low-Value Customers": {
        "workflow_name": "Customer Reactivation Flow",
        "workflow_trigger": "Launch re-engagement campaign",
        "priority": "Low"
    },

    "Active Omni-Channel Customers": {
        "workflow_name": "Cross-Channel Engagement Flow",
        "workflow_trigger": "Send personalized multi-channel recommendations",
        "priority": "Medium"
    },

    "Premium Loyal Customers": {
        "workflow_name": "Premium Loyalty Journey",
        "workflow_trigger": "Enroll customer in loyalty and retention program",
        "priority": "High"
    },

    "Family Budget Customers": {
        "workflow_name": "Family Bundle Campaign",
        "workflow_trigger": "Send family-oriented bundle offers",
        "priority": "Medium"
    },

    "Deal-Driven Customers": {
        "workflow_name": "Promotion Optimization Flow",
        "workflow_trigger": "Send minimum-spend discount campaign",
        "priority": "Medium"
    },

    "VIP Campaign Responders": {
        "workflow_name": "VIP Early-Access Journey",
        "workflow_trigger": "Enroll customer in priority campaign workflow",
        "priority": "High"
    }
}


def get_workflow(segment_name):
    """
    Return workflow package
    for a customer segment.
    """

    return WORKFLOW_RULES.get(
        segment_name,
        {
            "workflow_name": "Unknown",
            "workflow_trigger": "Unknown",
            "priority": "Low"
        }
    )