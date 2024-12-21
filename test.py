import pytest
import main

@pytest.fixture
def my_fixture():
    data=main.get_word_count_of_wiki_page("Tamil Nadu")
    print(data)