# Real World QA Automation

This project demonstrates how to create automated tests for both **UI** and **API** using **Python**, **Selenium**, **Pytest**, and other popular libraries. The project contains two types of tests:

- **UI Tests**: Using **Selenium** for browser automation (Login, Forms, Tables, etc.).
- **API Tests**: Using **requests** to test RESTful APIs (Login, User Management, etc.).

## Technologies Used:
- **Selenium**: For UI testing.
- **Pytest**: For running and structuring the tests.
- **Requests**: For API testing.
- **Faker**: For generating fake data for tests.
- **Allure**: For generating beautiful test reports.
- **Pytest-xdist**: For parallel test execution.
- **GitHub Actions**: For CI/CD pipeline setup.
- **Docker (Optional)**: To run tests inside containers.

## Project Structure:

realworld-qa-automation/ │ ├── tests/ │ ├── ui/ │ │ ├── test_login.py │ │ └── test_forms.py │ └── api/ │ ├── test_users.py │ └── test_login_api.py │ ├── pages/ │ ├── base_page.py │ ├── login_page.py │ └── form_page.py │ ├── utils/ │ ├── logger.py │ ├── config.py │ └── faker_data.py │ ├── data/ │ └── test_data.json │ ├── screenshots/ └── reports/


## How to Run Tests:

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests:

    ```bash
    pytest --alluredir=reports/allure-results --maxfail=1 --disable-warnings
    ```

3. Generate Allure Report:

    ```bash
    allure serve reports/allure-results
    ```

## Contributing:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add your feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

