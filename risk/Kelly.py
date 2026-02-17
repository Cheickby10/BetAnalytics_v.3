def kelly(edge, odds):
    """
    Kelly Criterion position sizing
    edge = probability advantage (0-1)
    odds = payout multiplier
    """

    try:
        fraction = (edge * (odds - 1) - (1 - edge)) / (odds - 1)
        return max(fraction, 0)
    except:
        return 0
