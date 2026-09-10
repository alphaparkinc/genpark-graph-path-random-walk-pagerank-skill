import sys
import json
from client import KnowledgeGraphPPR

ppr = KnowledgeGraphPPR()

def handle_call(name, arguments):
    if name == "add_edge":
        ppr.add_edge(arguments["u"], arguments["v"])
        return {"node_count": len(ppr.nodes)}
    elif name == "score":
        seeds = arguments["seeds"]
        return {"scores": ppr.compute_ppr(seeds)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
