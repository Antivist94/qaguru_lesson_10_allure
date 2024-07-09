import allure
from selene import browser, have


def test_github_search_with_allure_steps():
    open_github_main_page()
    find_repo(repo = 'repo:Antivist94/qaguru_lesson_10_allure')
    open_issue_list()
    open_issue_by_name(issue = 'Test issue')
    assert_name_of_issue_is_correct(issue = 'Test issue')


@allure.step('Открыть github.com')
def open_github_main_page():
    browser.open('https://github.com')


@allure.step('Найти репозиторий {repo} и перейти в него')
def find_repo(repo):
    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Открыть список issues')
def open_issue_list():
    browser.element('#issues-tab').click()


@allure.step('Открыть issue с названием {issue}')
def open_issue_by_name(issue):
    browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text(issue)).click()


@allure.step('Убедиться, что у открытого issue название {issue}')
def assert_name_of_issue_is_correct(issue):
    browser.all('.markdown-title').first.should(have.text(issue))
