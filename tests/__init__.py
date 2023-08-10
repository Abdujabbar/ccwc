import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = f"{TEST_DIR}/fixtures"



def get_fixture_path(file_path):
    return f"{FIXTURES_DIR}/{file_path}"