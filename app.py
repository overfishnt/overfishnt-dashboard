# To run streamlit
if __name__ == "__main__":
    import sys
    from streamlit.web import cli

    sys.argv = ["streamlit", "run", "Home.py", "--server.port", "8080"]
    sys.exit(cli.main())
