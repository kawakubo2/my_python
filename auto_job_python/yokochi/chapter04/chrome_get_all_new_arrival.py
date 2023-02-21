from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://uta.pw/sakusibbs'
driver.get(url)
table = driver.find_element_by_id("tblIndex")
urls = [indextitle.get_attribute('href') for indextitle in table.find_elements_by_css_selector("tbody tr td a.indextitle")]
print(f'月間トップ3チャート: {len(urls)}')
for url in urls:
    post_id = url.split('?')[1]
    post_url = f'https://uta.pw/sakusibbs/post.php?{post_id}'
    driver.get(post_url)
    e = driver.find_element_by_class_name('posttitle')
    print(e.text)
driver.close()
    