env_dir:=venv
pip:=$(env_dir)/bin/pip

install:
	
	python3.6 -m venv $(env_dir)
	$(pip) install --upgrade pip
	$(pip) install -r requirements.txt

clean:
	rm -r $(env_dir)

reinstall:
	make clean install
