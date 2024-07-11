# Mainfilm Automation

## Installion
1. Clone the repository by running the following command
```shell
git clone https://github.com/jordan-jakisa/mainfilm-automation 
```
2. Change directory to the cloned repository
```shell
cd mainfilm-automation
```
3. Create a virtual environment
```shell
python3 -m venv venv
```
4. Activate the virtual environment
```shell
venv\Scripts\activate
```
5. Install the neccesary dependencies
```shell
pip install -r requirements.txt
```
6. Create a `.env` file in the root directory of the project and add the following environment variables
```shell
OPENAI_API_KEY=<your_open_ai_api_key>
MOCO_API_KEY=<your_moco_api_key>
MOCO_DOMAIN=<your_moco_domain>
EMAIL_USERNAME=<your_email_username>
EMAIL_PASSWORD=<your_email_app_password>
```
7. Run the application
```shell
python manage.py runserver
```
