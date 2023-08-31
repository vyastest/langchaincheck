import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent
import openai
openai.api_key = st.secrets["my_api_key"]

st.title("new csv app")
