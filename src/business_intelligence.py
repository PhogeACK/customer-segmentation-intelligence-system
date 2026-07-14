from src.persona_engine import enrich_cluster_output
from src.recommendation_engine import get_recommendation
from src.workflow_engine import get_workflow


def generate_business_intelligence(cluster_id):

    persona = enrich_cluster_output(cluster_id)

    recommendation = get_recommendation(
        persona["segment_name"]
    )

    workflow = get_workflow(
        persona["segment_name"]
    )

    return {
        **persona,
        **recommendation,
        **workflow
    }