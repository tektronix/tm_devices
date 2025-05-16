# Contributing Guidelines

Contributions are welcome, and they are greatly appreciated! Every bit helps,
and credit will always be given.

> [!TIP]
> View this page in the [online documentation](https://tm-devices.readthedocs.io/latest/CONTRIBUTING) for the best experience.

## Types of Contributions

There are several types of contributions that can be made:

### Report Bugs

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even on the
web in blog posts, articles, and such.

The docstring and commenting convention this project follows is the
[Google Python styleguide](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
with a few minor exceptions:

- This project uses imperative-style docstrings (`Fetch rows from a Bigtable.`),
    **not** Google's recommended descriptive-style docstrings
    (`Fetches rows from a Bigtable.`).

### Submit Feedback

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are
    welcome :)

## Get Started!

Ready to contribute? Here's how to set up `tm_devices` for local development.

1. Set up commit signing, see [GitHub's documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification) for details.

    !!! hint

        All commits going into the main repository are required to be signed, so make sure
        to set up commit signing before starting to make changes.

2. Fork `tm_devices` into a new repository.

3. Set up a virtual environment and install the project with its dependencies:

    - Using the helper script (recommended):
        ```console
        python scripts/contributor_setup.py
        ```
    - Or manually:
        ```console
        python -m venv .env
        ```
        ```console
        # Linux
        source .venv/bin/activate

        # Windows
        .venv\Scripts\activate.bat
        ```
        ```console
        python -m pip install -U pip poetry
        poetry install
        pre-commit install
        ```

4. Check to see if there are any [open issues](https://github.com/tektronix/tm_devices/issues) or [pull requests](https://github.com/tektronix/tm_devices/pulls) that are related to the change you wish to make.

5. Create or update an [issue](https://github.com/tektronix/tm_devices/issues) to track the status of your change.

6. Use `git` to create a branch for local development and make your changes:

    ```console
    git checkout -b name-of-your-bugfix-or-feature
    ```

7. Update the **Unreleased** section in the [CHANGELOG](./CHANGELOG.md) using the proper format.

8. When you're done making changes, check that your changes conform to any code
    formatting requirements and pass any tests.

    !!! note

        Always remember to activate the virtual environment before attempting to run tests or other code.

        ```console
        # Linux
        source .venv/bin/activate

        # Windows
        .venv\Scripts\activate.bat
        ```

    - To run full static code analysis, tests, and documentation validation
        (running this prior to opening a pull request is highly recommended, but it is slow):

        ```console
        tox -p
        ```

    - To run just the tests and static code analysis (**much quicker**):

        ```console
        tox -p -m basic
        ```

    - To run just the pre-commit checks:

        ```console
        pre-commit run --all
        ```

    - To run just the tests:

        ```console
        tox -e tests
        ```

        !!! note

            Two html outputs are generated:

            - Code coverage report: `.results_tests/htmlcov/index.html`
            - Test results: `.results_tests/results.html`

    - To just build the documentation:

        ```console
        tox -e docs
        ```

        !!! hint

            To view the documentation locally you will need to first build and then serve the site using one of the following methods:

            ```console
            mkdocs serve --clean --no-livereload
            ```

            ```console
            tox -e docs
            python -m http.server -d .results_docs
            ```

9. Commit and push your changes, then open a pull request from
    the fork back into the main repository.

    - Commit messages must be structured as follows:
        ```
        <type>[optional scope]: <description>

        [optional body]

        [optional footer(s)]
        ```
    - `<type>` can be one of `fix`, `feat`, `build`, `ci`, `docs`, `style`,
        `refactor`, or `test`.
    - See the
        [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
        website for more details on this format.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems
    and versions of Python.
4. The **Unreleased** section in the [Changelog](./CHANGELOG.md) should be updated.

## Project Test Plan

This project undergoes rigorous testing to ensure a high quality product.

### All Changes

1. 100% of the source code will have unit tests (except for accepted exceptions)
2. All static code analysis will pass
3. All features will have documentation
4. [Changelog](./CHANGELOG.md) will be updated
5. Pull requests will have all required approvals prior to merging

### Major Changes

1. Each supported VISA Implementation will be validated as working
2. Each supported Connection Type will be validated as working

## Code of Conduct

Please note that the `tm_devices` project is released with a
[Code of Conduct](./CODE_OF_CONDUCT.md). By contributing to this project you agree
to abide by its terms.
