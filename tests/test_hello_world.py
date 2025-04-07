def test_opencart_main(browser, base_url):
    browser.get(base_url)

    assert "Your Store" in browser.title


def test_opencart_admin(browser, base_url):
    browser.get(base_url + "/administration")

    assert "Administration" in browser.title
