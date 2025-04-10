setup:
	@pyenv virtualenv 3.10.12 st7_quantum
install:
	@eval "$$(pyenv init -)" && \
	pyenv activate st7_quantum && \
	pip install -r requirements.txt
run_lab_1:
	@eval "$$(pyenv init -)" && \
	pyenv activate st7_quantum && \
	echo "Running lab 1" && \
	cd Qiskit1-intro && \
	python examples.py && \
	python exercise1.py && \
	python exercise2.py && \
	python exercise3.py
run_lab_2:
	@eval "$$(pyenv init -)" && \
	pyenv activate st7_quantum && \
	cd Qiskit2-Grover-QPE && \
	echo "Running lab 2" && \
	python grover.py && \
	python qpe.py
run_lab_3:
	@eval "$$(pyenv init -)" && \
	pyenv activate st7_quantum && \
	cd Qiskit3-Noise-IBM && \
	echo "Note: You should put your IBM key in executionIBM.py" && \
	echo "Running lab 3" && \
	python simulation.py && \
	python executionIBM.py
run_lab_4:
	@eval "$$(pyenv init -)" && \
	pyenv activate st7_quantum && \
	cd Qiskit4-VQC && \
	echo "Running lab 4" && \
	python parametrized_circuit.py && \
	python ml_optimization.py
run_lab_5:
	@eval "$$(pyenv init -)" && \
	pyenv activate st7_quantum && \
	cd Qiskit5-QML && \
	echo "Running lab 5" && \
	python embedding.py && \
	python fidelity.py && \
	python similarity.py && \
	python qml_clustering.py
