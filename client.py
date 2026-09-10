import collections

class KnowledgeGraphPPR:
    """
    Personalized PageRank (PPR) / Random Walk with Restart (RWR) on Knowledge Graphs.
    Scores entity importance conditioned on seed query entities.
    """
    def __init__(self, damping=0.85):
        self.damping = damping
        self.adj = collections.defaultdict(list)
        self.nodes = set()

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def compute_ppr(self, seed_nodes, iterations=20):
        scores = {n: 0.0 for n in self.nodes}
        for s in seed_nodes:
            scores[s] = 1.0 / len(seed_nodes)

        for _ in range(iterations):
            next_scores = {n: 0.0 for n in self.nodes}
            for u in self.nodes:
                neighbors = self.adj[u]
                if neighbors:
                    spread = scores[u] / len(neighbors)
                    for v in neighbors:
                        next_scores[v] += self.damping * spread
                else:
                    for s in seed_nodes:
                        next_scores[s] += self.damping * (scores[u] / len(seed_nodes))

            teleport = (1.0 - self.damping) / len(seed_nodes)
            for s in seed_nodes:
                next_scores[s] += teleport
            scores = next_scores

        return scores
