python3 service_1/create.py
source venv/bin/activate
python3 -m pytest service_1/testing/test_service_1.py --cov=application
python3 -m pytest service_2/testing/test_service_2.py --cov=app
python3 -m pytest service_3/testing/test_service_3.py --cov=app
python3 -m pytest service_4/testing/test_service_4.py --cov=app