Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~

Usage:
~~~
cd cffi_c
gcc -fPIC -shared -o lib_matrix.so matrix.c
cd ..
python main.py
~~~

Tests:
~~~
python -m unittest tests.py

coverage run -m unittest tests.py
coverage report -m
coverage html
~~~
