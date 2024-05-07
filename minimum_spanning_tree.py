import networkx


def generate_mst(G, spanning_trees):
    spanning_trees = spanning_trees
    mst = networkx.minimum_spanning_tree(G)
    mst_weight = 0
    for e in mst.edges():
        mst_weight += G.edges[e]["weight"]
    print("\nWeight : ", mst_weight)

    mst_list = []

    for tree in spanning_trees:
        weight = 0
        for e in tree.edges():
            weight += G.edges[e]["weight"]
        if weight == mst_weight:
            mst_list.append(tree)

    print(f"Number of minimum weight spanning trees : {len(mst_list)}")
    for tree in mst_list:
        for e in tree.edges():
            print(e, end=" ")
        print()

    return mst_list
