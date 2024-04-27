import streamlit as st

from src.app.services.frontend_max import client_input  #, client_output
# from src.services.backend import recsys_module


def start_app():
    """ Start of the Streamlit application. """
    data = client_input()
    # recommendations = recsys_module(data)
    # client_output(recommendations)
