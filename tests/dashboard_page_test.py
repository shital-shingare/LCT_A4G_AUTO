
def test_dashboard_page_title(dashboard_page):
    assert dashboard_page.validate_page_title().is_visible(), "Dashboard page title is not visible"