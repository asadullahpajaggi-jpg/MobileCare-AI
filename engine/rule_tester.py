# MobileCare AI - Automatic Rule Testing System

from engine.inference_engine import (
    forward_chaining,
    backward_chaining
)


def run_rule_tests(rules):

    results = []

    for rule in rules:

        rule_id = rule["id"]
        conditions = rule["conditions"]
        conclusion = rule["conclusion"]

        # Test Forward Chaining
        forward_result = forward_chaining(
            conditions,
            rules
        )

        forward_pass = any(
            step["rule_id"] == rule_id
            for step in forward_result["trace"]
        )

        # Test Backward Chaining
        backward_result = backward_chaining(
            conclusion,
            conditions,
            rules
        )

        backward_pass = (
            backward_result["success"]
            and any(
                step["rule_id"] == rule_id
                for step in backward_result["trace"]
            )
        )

        # Final result for this rule
        passed = forward_pass and backward_pass

        results.append({
            "rule_id": rule_id,
            "conclusion": conclusion,
            "forward": forward_pass,
            "backward": backward_pass,
            "passed": passed
        })

    total = len(results)
    passed_count = sum(
        1 for result in results if result["passed"]
    )

    failed_count = total - passed_count

    return {
        "total": total,
        "passed": passed_count,
        "failed": failed_count,
        "results": results
      }
      
