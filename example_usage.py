from client import LlmProductionTraceObservabilityDebuggerClient

def main():
    client = LlmProductionTraceObservabilityDebuggerClient()
    res = client.debug_trace("sess_9a3f7b2c", "claude-3-5-sonnet")
    lat = res["latency_breakdown_ms"]
    print(f"Total E2E Latency: {lat['total_e2e']}ms (Inference: {lat['model_inference']}ms)")
    print(f"Prompt Regression Detected: {res['prompt_regression_detected']}")
    print("Top Errors:")
    for e in res["top_error_spans"]:
        print(f"  [{e['severity']}] {e['span']}: {e['error']}")
    print("Optimization Suggestions:")
    for s in res["optimization_suggestions"]:
        print(f"  - {s}")

if __name__ == "__main__":
    main()
