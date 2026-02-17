def kelly(edge, odds):
    return max((edge*(odds-1)-(1-edge))/(odds-1),0)
