from web_scraper.scraper import webScraper


def test_get_citations_needed_count():
    URL ="https://en.wikipedia.org/wiki/History_of_Mexico"
    assert webScraper(URL).get_citations_needed_count() == 5
   
def test_get_citations_needed_report():
    with open('./tests/paragraphs_tests.txt', 'r') as f:
        assert "".join(f.readlines()).count("[citation needed]") == 5    
