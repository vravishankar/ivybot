help:
	@echo "		clean"
	@echo "			Remove python artifacts and build artifacts"
	@echo "		train-core"
	@echo "			Train a dialogue model using Rasa core"
	@echo "		run-core"
	@echo "			Spin up the core server on the command line"
	@echo "		run-actions"
	@echo "			Spin up the action server"
	@echo "		run"
	@echo "			Spin up both core and the action server"
	@echo "		visualize"
	@echo "			Show your stories as a graph"

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build

train-core:
	python3 -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue -c policies.yml --debug

train-nlu:
	python3 -m rasa_nlu.train -c config.yml --fixed_model_name current --data data/nlu.md -o models --project nlu --verbose

train-interactive:
	python3 -m rasa_core.train interactive -s data/stories.md -d domain.yml -o models/dialogue --verbose --endpoints endpoints.yml

visualize:
	python3 -m rasa_core.visualize -s data/stories.md -d domain.yml -o story_graph.html

test-core:
	python3 -m rasa_core.test --core models/dialogue -s data/stories.md --fail_on_prediction_errors

run-core:
	python3 -m rasa_core.run --core models/dialogue --nlu models/nlu/current --verbose --endpoints endpoints.yml --debug

run-actions:
	python3 -m rasa_core_sdk.endpoint --actions api.actions

run:
	make run-actions&
	make run-core