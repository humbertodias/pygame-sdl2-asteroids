dep:	install_pygame_sdl2	install_nuikta
	pip3 install -r requirements.txt

run:
	python3 src/main.py

clean:
	rm -rf __pycache__ .idea *.pyc

install_nuikta:
	sudo apt install -y nuitka

install_pygame_sdl2_dep:
	pip3 install cython
	sudo apt update -y && \
	sudo apt install -y build-essential python3-dev libsdl2-dev \
    libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libjpeg-dev libpng-dev virtualenvwrapper

install_pygame_sdl2:	install_pygame_sdl2_dep
	cd `mktemp -d` && git clone --branch renpy-8.1.0.23050902 https://github.com/renpy/pygame_sdl2 . && python3 setup.py install

exe_win:
	nuitka3 --follow-imports --standalone --remove-output --windows-icon=icon.ico src/main.py
	cp -r resource main.dist
exe_mac: exe
exe_lin: exe
exe:
	nuitka3 --follow-imports --standalone --remove-output --clang src/main.py
	cp -r resource main.dist