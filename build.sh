if [ python ]; then
    python -m venv .venv
    source .venv/bin/activate
    pip install colorama pyfiglet requests pillow survey

    touch main.sh
    echo "source .venv/bin/activate && python bin/main.py" > main.sh
    echo "Sucessfully built Pyndows, to launch it, type in terminal: 'sh main.sh'."
    rm build.sh

else
    echo "Error! Python is not installed."
fi