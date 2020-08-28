# Format, Lint, Test (FLT)
black . \
&& isort . \
&& flake8 tests/ website/ \
&& pytest
