from selene import browser, have


def test_github_search_without_allure_steps():
    browser.open("https://github.com")
    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('#query-builder-test').send_keys('repo:Antivist94/qaguru_lesson_10_allure').press_enter()
    browser.element('#issues-tab').click()
    browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text('Test issue')).click()
    browser.all('.markdown-title').first.should(have.text('Test issue'))