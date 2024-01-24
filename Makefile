dep:	install_pygame_sdl2
	pip3 install -r requirements.txt

run:
	python3 src/main.py

clean:
	rm -rf __pycache__ .idea *.pyc

install_nuikta:
	sudo apt install -y nuitka

install_pygame_sdl2:	install_nuikta
	sudo apt install -y build-essential python-dev libsdl2-dev \
    libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libjpeg-dev libpng12-dev virtualenvwrapper && \
	cd `mktemp -d` && git clone https://github.com/renpy/pygame_sdl2 . && python3 setup.py install

exe_win:
	nuitka3 --follow-imports --standalone --remove-output --windows-icon=icon.ico src/main.py
	cp -r resource main.dist ; cp config.txt main.dist
exe_mac: exe
exe_lin: exe
exe:
	nuitka3 --follow-imports --standalone --remove-output --clang src/main.py
	cp -r resource main.dist ; cp config.txt main.dist