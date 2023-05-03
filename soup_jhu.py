import requests
from bs4 import BeautifulSoup

URL: str = "https://ep.jhu.edu/programs/applied-and-computational-mathematics/courses/"

r: requests.Response = requests.get(URL)
soup: BeautifulSoup = BeautifulSoup(r.content, 'html5lib')

# css label strings
ALL_COURSES_CONTAINER_CSS_CLASSNAME: str = "courses"
COURSE_SECTION_TITLE_CSS_CLASSNAME: str = "course_group_title_label"

courses_sections: list = soup.find_all("div", {"class": ALL_COURSES_CONTAINER_CSS_CLASSNAME})

print(f"Found number of course sections: {len(courses_sections)}\n\n")

for section in courses_sections:
    section_title: str = section.find("span", {"class": COURSE_SECTION_TITLE_CSS_CLASSNAME}).decode_contents()
    course_table_rows: list = section.find_all("tr", {"class": ["course_item", "course_item_last"]})
    
    print(f"\n\n{section_title}, number of courses: {len(course_table_rows)}\n")
    
    course_hrefs: list = []
    for course_tr in course_table_rows:
        # get course name
        course_name: str = course_tr.find("span", {"class": "course_item_link_name"})
        print(f"{course_name.decode_contents()},")
        
        # get link
        course_table_row_link_href: str = course_tr.find("a", href=True)['href']
        course_hrefs.append(course_table_row_link_href)
        # print(f"{course_table_row_link_href}")
        # print(f"{course_name.decode_contents()},{course_table_row_link_href}")
    print(f"\n")
    for _ in course_hrefs:
        print(f"{_}")
    