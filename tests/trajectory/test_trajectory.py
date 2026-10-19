from google.adk.agents import LoopAgent, ParallelAgent, SequentialAgent

from app.agent import root_agent

# User
#  ↓
# Strategy Agent
#  ↓
# Guess
#  ↓
# Answer

# User
#  ↓
# Race Director
#  ↓
# Race Data
#  ↓
# Weather
#  ↓
# Tyres
#  ↓
# Strategy
#  ↓
# Answer

# Question:
#
# "What is Norris's tyre condition?"
#
# Expected:
#
# Race Director
#      ↓
# Race Data Tool
#      ↓
# Tyre analysis
#      ↓
# Answer

# Race Director
#      ↓
# Weather
#      ↓
# Strategy
#      ↓
# Race data
#      ↓
# Weather again
#      ↓
# Answer

# Slower ❌
#
# More expensive ❌
#
# Harder to debug ❌
#
# Potentially less reliable ❌

# AI EVALUATION
#
# "Is this strategy useful,
# grounded and safe?"
#
# Probabilistic.