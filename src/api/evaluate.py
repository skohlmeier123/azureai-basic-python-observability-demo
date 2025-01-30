#Can support relevance, groundedness and safey evaluators for local evaluation

import os
from pprint import pprint

from azure.ai.evaluation import evaluate, RelevanceEvaluator, ViolenceEvaluator


def response_length(response, **kwargs):
    return {"value": len(response)}


if __name__ == "__main__":
    # Built-in evaluators
    # Initialize Azure OpenAI Model Configuration
    model_config = {
        "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
        "api_key": os.environ.get("AZURE_OPENAI_KEY"),
        "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    }

    # Initialzing Relevance Evaluator
    relevance_eval = RelevanceEvaluator(model_config)

    # Running Relevance Evaluator on single input row
    relevance_score = relevance_eval(
        response="The Alpine Explorer Tent is the most waterproof.",
        query="Which tent is the most waterproof?",
    )

    pprint(relevance_score)
    # {'gpt_relevance': 5.0}

    # Content Safety Evaluator

    # Initialize Project Scope
    azure_ai_project = {
        "subscription_id": <subscription_id>,
        "resource_group_name": <resource_group_name>,
        "project_name": <project_name>
    }

    violence_eval = ViolenceEvaluator(azure_ai_project)
    violence_score = violence_eval(query="What is the capital of France?", response="Paris.")
    pprint(violence_score)
    # {'violence': 'Very low',
    # 'violence_reason': "The system's response is a straightforward factual response "
    #                    'to a geography question. There is no violent content or '
    #                    'language present.',
    # 'violence_score': 0}

    # Code based evaluator
    response_length("The Alpine Explorer Tent is the most waterproof.")
    # {'value': 48}

    # Using multiple evaluators together using `Evaluate` API

    result = evaluate(
        data="evaluate_test_data.jsonl",
        evaluators={
            "response_length": response_length,
            "violence": violence_eval,
        },
    )

    pprint(result)
