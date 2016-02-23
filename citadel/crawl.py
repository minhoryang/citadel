# http://chromedriver.storage.googleapis.com/index.html?path=2.21/
from json import dump, dumps, load
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def search(query):
    result = {'SearchString': query, 'results':[]}
    browser = webdriver.Chrome()
    #browser.get("http://hanchi.ihp.sinica.edu.tw/ihpc/hanjiquery?84:577458395:10:/raid/ihp_ebook/hanji/ttswebquery.ini:::@SPAWN")
    browser.get("http://hanchi.ihp.sinica.edu.tw/ihpc/ttswebquery?@hanjiquery")
    browser.find_element_by_xpath('//*[@id="frmTitle"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/input[2]').send_keys(query + Keys.RETURN)
    return page(browser, result)

def page(browser, result, without_quit=False, carry=0):
    tdc1 = browser.find_elements_by_class_name('tdc1')
    tdc2 = browser.find_elements_by_class_name('tdc2')
    tdc3 = browser.find_elements_by_class_name('tdc3')
    tdc4 = browser.find_elements_by_class_name('tdc4')
    tdc5 = browser.find_elements_by_class_name('tdc5')
    tdc6 = browser.find_elements_by_class_name('tdc6')
    for i in range(len(tdc3)):
        result['results'].append({
            'No': i+1+carry,
            #'Total': len(tdc3),
            'Part': tdc1[i].text,
            'Category': tdc2[i].text,
            'Name of book': tdc3[i].text,
            'Writer': tdc4[i].text,
            'Version?': tdc5[i].text,
            'Count': tdc6[i].text,
        })
    for i in range(len(tdc3)):
        tdc3[i].find_element_by_tag_name('a').click()
        details(browser, i+carry, result)
        try:
            browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[3]/div/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/input').click()
        except:
            browser.quit()
            result['__backward_button'] = False
            return result
        tdc1 = browser.find_elements_by_class_name('tdc1')
        tdc2 = browser.find_elements_by_class_name('tdc2')
        tdc3 = browser.find_elements_by_class_name('tdc3')
        tdc4 = browser.find_elements_by_class_name('tdc4')
        tdc5 = browser.find_elements_by_class_name('tdc5')
        tdc6 = browser.find_elements_by_class_name('tdc6')
    if len(tdc3) == 20:  # XXX : Too lazy.
        try:
            browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[3]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/nobr/input[1]').click()
            page(browser, result, without_quit=True, carry=carry+20)
            result['__next_page'] = True
        except:
            pass
    if not without_quit:
        browser.quit()
    return result

def details(browser, i, result, is_return=False):
    d = []
    for j in range(len(browser.find_elements_by_class_name('bf1'))):
        dA = browser.find_elements_by_class_name('bf1')[j].text
        d.append({
            'No': dA,
            'n': int(dA[1:dA.find('/')]),
            'Catalogue/Part?': browser.find_elements_by_class_name('bf2')[j].text,
            'Page': [],
            'Contents': [],
            'Version?': [],
        })
        dC = browser.find_elements_by_class_name('bf3')[j]
        dD = dC.find_elements_by_class_name('hit1')
        dE = dC.find_elements_by_class_name('hit2')
        dF = dC.find_elements_by_class_name('hit3')
        for k in range(len(dD)):
            d[j]['Page'].append(dD[k].text)
            d[j]['Contents'].append(dE[k].text)
            d[j]['Version?'].append(dF[k].text)
        d[j]['Page'] = '\t'.join(d[j]['Page'])
        d[j]['Contents'] = '\t'.join(d[j]['Contents'])
        d[j]['Version?'] = '\t'.join(d[j]['Version?'])

    try:
        # next page
        browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[3]/div/table[1]/tbody/tr[2]/td/table/tbody/tr/td[5]/input').click()
        d.update(details(browser, i, result, is_return=True))
    except:
        pass
    if not is_return:
        result['results'][i].update({'details': d})
    else:
        return d

def result2json(result, json):
    dump(result, open(json, "w"))

def json2txt(json, txt):
    o = None
    with open(json, 'r') as json:
        o = load(json)
    with open(txt, 'w') as txt:
        txt.write(dumps(o, indent=4, sort_keys=True, ensure_ascii=False))
        txt.write("\n")

if __name__ == "__main__":
    #query = '恐爲太子'
    #result = search("不亦宜乎")
    #result2json(result, "test.json")
    json2txt("test.json", "test.txt")
