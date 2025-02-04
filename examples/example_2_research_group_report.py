""" 2. Research Lab Report
Provides a list with all the papers published by a group of researchers in one year
"""
from sciencer import Sciencer
from sciencer.providers import SemanticScholarProvider
from sciencer.collectors import CollectByAuthorID
from sciencer.filters import FilterByYear

researchers = ["145136631", "3233831", "1816411", "145813496", "145955156", "145125979", "2151066261", "144518313", "2158393415", "143825592"]

if __name__ == "__main__":

    s = Sciencer()
    s.add_provider(SemanticScholarProvider())

    for researcher in researchers:
        s.add_collector(CollectByAuthorID(author_id=researcher))
    
    s.add_filter(FilterByYear(min_year=2022, max_year=2022))
    
    for paper in s.iterate( remove_source_from_results=False):
        print(f"{paper.year}@{paper.paper_id} - {paper.title} => {paper.authors}")
