# Mutation testing in Python

## …using _`mutmut`_ library

---

30.06.2023, lightning talk at PyCon by Piotr Grędowski ([Ørsted](https://orsted.com))

---

## Reproduce

Repository:
[https://github.com/piotrgredowski/try-mutation-testing](https://github.com/piotrgredowski/try-mutation-testing)

Use tags: `start` for starting point, and `end` for result showed during the talk.

Install requirements:

```bash
pip install -r requirements.txt
```

Run pytest:

```bash
python -m pytest --cov --cov-branch --cov-report=html --pdb
```

Mutmut commands:

```bash
mutmut run
mutmut results
mutmut show <mutant_id>
```

### Sources

- https://about.codecov.io/blog/getting-started-with-mutation-testing-in-python-with-mutmut/
- https://mutmut.readthedocs.io/en/latest/
- https://opensource.com/article/20/7/mutmut-python
