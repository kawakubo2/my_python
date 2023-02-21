from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://uta.pw/sakusibbs'
driver.get(url)
table = driver.find_element_by_id("tblIndex")
all_index_title = table.find_elements_by_css_selector("tbody tr td a.indextitle")
print(f'月間トップ5チャート: {len(all_index_title)}')
for index_title in all_index_title:
    print(f"index_title={index_title}")
    if index_title.get_attribute('href') is None:
        continue;
    url = index_title.get_attribute('href')
    print(f"url={url}")
    post_id = url.split('?')[1]
    print(f"post_id={post_id}")
    post_url = f'https://uta.pw/sakusibbs/post.php?{post_id}'
    driver.get(post_url)
    e = driver.find_element_by_class_name('posttitle')
    print(e.text)
driver.close()
    