import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from core.environment import CrashEnv
from core.bayesian import EdgeEstimator

st.title("BetAnalytics Pro AI Dashboard")

env = CrashEnv()
est = EdgeEstimator()

rounds = st.slider("Rounds",100,5000,1000)
action = st.slider("Cashout Target",1.1,5.0,2.0)

wins=0

for _ in range(rounds):
    crash,reward=env.step(action)
    win = reward>0
    est.update(win)
    if win:
        wins+=1

edge = est.estimate()
fraction = kelly(edge, action)

st.metric("Win Rate",wins/rounds)
st.metric("Bayesian Edge",edge)
st.metric("Kelly Fraction",fraction)
