<!-- repo links -->
[repo_main]: https://github.com/domi119017/prynterface
[repo_issues_open]: https://github.com/domi119017/prynterface/issues
[repo_issues_new]: https://github.com/domi119017/prynterface/issues/new
[repo_releases]: https://github.com/domi119017/prynterface/releases
<!-- links to files -->
[repo_license]: LICENSE
[repo_logo_icon]: misc/images/logo_icon.png
[repo_logo_text]: misc/images/logo_text.png
[repo_logo_combined]: misc/images/logo.png
[project_screenshot]: misc/images/screenshot.png

<!-- shields -->
[shield_downloads]: https://img.shields.io/github/downloads/domi119017/prynterface/total
[shield_contributors]: https://img.shields.io/github/contributors/domi119017/prynterface?color=dark-green
[shield_issues]: https://img.shields.io/github/issues/domi119017/prynterface
[shield_license]: https://img.shields.io/badge/License-GPLv3-blue.svg
[shield_codecov]: https://codecov.io/gh/domi119017/prynterface/branch/master/graph/badge.svg?token=DFD15VCX40
[shield_dependencys]: https://img.shields.io/librariesio/github/domi119017/prynterface

<!-- icons -->
[icon_python]: https://simpleicons.org/icons/python.svg

<!-- websites -->
[python_download]: https://www.python.org/downloads/

<!-- other -->
[add_to_path]: prynterface/docs/path.md

<!-- workflow shields -->
[pytest_quick]: https://github.com/domi119017/prynterface/actions/workflows/pytest_quick.yml/badge.svg
[pytest_versions_ubuntu]: http://github-actions.40ants.com/domi119017/prynterface/matrix.svg?only=pytest%20detailed.test.ubuntu-latest
[pytest_versions_windows]: http://github-actions.40ants.com/domi119017/prynterface/matrix.svg?only=pytest%20detailed.test.windows-latest

<!-- @todo Project Logo 
[![Logo][repo_logo_combined]][repo_main]
-->
Welcome! This is the **development branch** for [Prynterface][repo_main].

[![License][shield_license]][repo_license]
[![Contributors][shield_contributors]][repo_main]
[![Issues][shield_issues]][repo_main]

![tests][pytest_quick]
![Codecov](https://img.shields.io/codecov/c/gh/domi119017/prynterface)
![Dependencies][shield_dependencys]

Tested Versions:
| **Ubuntu**  | ![pytest][pytest_versions_ubuntu]  |
| ----------- | ---------------------------------- |
| **Windows** | ![pytest][pytest_versions_windows] |


<!-- Table Of Contents -->
<details>
<summary>Table of Contents</summary>
<ol>
<li>
<a href="#about-the-project">About The Project</a>
</li>
<li>
<a href="#getting-started-with-development">Getting Started with Development</a>
<ul>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#installation">Installation</a></li>
</ul>
</li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#contributing">Contributing</a>
<ul>
<li><a href="#editing-in-general">Editing in general</a></li>
<li><a href="#the-plan">The Plan</a></li>
<li><a href="#creating-a-pull-request">Creating A Pull Request</a></li>
</ul>
</li>
<li>
<a href="#license">License</a>
</li>
</ol>
</details>

</details>

## About The Project

<!-- @todo Project Screenshot [later]
[![Screenshot][project_screenshot]](#getting-started)
-->
Prynterface will be a python application for interfacing with 3D printers over serial connection.

## Getting Started with Development
The following section will guide you through the process of setting up a development environment.

### Prerequisites
* Python 3.10 or newer (click [here][python_download] for more information)
* Python is in your PATH (if not, [add it manually][add_to_path])

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/domi119017/prynterface
    ```
2. Upgrade pip
   ```sh
   python -m pip install --upgrade pip
   ```
3. Install poetry
   ```sh
   python -m pip install poetry
    ```
4. Poetry does the rest
   ```sh
   python -m poetry install
   ```

    You should now have a virtual environment with all the necessary dependencies installed.
    To activate the virtual environment, run:
    ```sh
    python -m poetry shell
    ```
    After that, you can run any of the project files.

## Roadmap

See the [open issues][repo_issues_open] for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/domi119017/prynterface/issues/new) to discuss it, or directly create a pull request.

### Editing in general

This project uses poetry for dependency management. <br>
Adding a new dependency is easy, but you have to do it in the right way.
- If you want to add a new dependency (after discussing it), run:
  ```sh
  python -m poetry add <dependency>
  ```
- If the dependency is only needed for development, run:
  ```sh
  python -m poetry add -G dev <dependency>
  ```

Before committing your changes, make sure to run:
```sh
python -m poetry lock
```
This will update the `poetry.lock` file to include your changes.

### The Plan:
- User interface
  - Choice between CLI and GUI
  - Customizable GUI
  - Dark / Light mode
- Interfacing with 3D printers
  - Serial connection (USB)
- Parsing: via pipeline
  - Detection of temp/pos/progress/etc. updates
  - colored output for busy/waiting
  - Firmware capabilities via M115 (for setting up the UI)
  - Detection of multi line responses (UBL, M420, etc.)
- Plotting
  - Temperature
  - Position
  - Progress
- Pipeline:
  ```mermaid
  graph LR
  detect-->extract-->parse
  ```
- Configuration
  - Config file
  - CLI arguments
  - GUI
  - Custom pipeline
  - Custom commands

### Creating A Pull Request
<!-- 
@todo change to reflect changes in repo security
-->
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Make some changes. See [Editing in general](#editing-in-general)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the GPL-3.0 License. See [LICENSE](https://github.com/domi119017/prynterface/LICENSE) for more information.

## Authors

* [Dominik Ullrich](github.com/domi119017)

## Acknowledgements

* [Othneil Drew](https://github.com/othneildrew/Best-README-Template)
* [ImgShields](https://shields.io/)
* [Natalie Weizenbaum](https://gist.github.com/nex3)
* [Printrun](https://github.com/kliment/Printrun)
