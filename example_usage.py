from client import KnowledgeGraphPPR

def main():
    print("=== Testing Knowledge Graph Personalized PageRank ===")
    ppr = KnowledgeGraphPPR(damping=0.85)
    ppr.add_edge("Einstein", "Physics")
    ppr.add_edge("Physics", "Relativity")
    ppr.add_edge("Physics", "Quantum")

    ranks = ppr.compute_ppr(seed_nodes=["Einstein"])
    print("Personalized PageRank Scores from seed 'Einstein':")
    for entity, score in sorted(ranks.items(), key=lambda x: x[1], reverse=True):
        print(f"  {entity}: {round(score, 4)}")

    assert ranks["Physics"] > ranks["Relativity"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
