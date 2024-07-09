import allure
from selene import browser, have


def test_github_search_with_allure_steps():
    with allure.step('Открыть github.com'):
        browser.open("https://github.com")
    with allure.step('Найти репозиторий Antivist94/qaguru_lesson_10_allure'):
        browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
        browser.element('#query-builder-test').send_keys('repo:Antivist94/qaguru_lesson_10_allure').press_enter()
    with allure.step('Открыть список issues'):
        browser.element('#issues-tab').click()
    with allure.step('Открыть issue с названием Test issue'):
        browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text('Test issue')).click()
    with allure.step('Убедиться, что у открытого issue название "Test issue"'):
        browser.all('.markdown-title').first.should(have.text('Test issue'))
