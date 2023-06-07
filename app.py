# https://discuss.streamlit.io/t/how-can-i-invoke-streamlit-from-within-python-code/6612
# The way how to invoke streamlit with run.py
if __name__ == "__main__":
    import sys
    from streamlit.web import cli

    sys.argv = ["streamlit", "run", "Home.py", "--server.port", "8080"]
    sys.exit(cli.main())
