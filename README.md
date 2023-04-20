<!-- Repo links -->
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

<!-- Shields -->
[shield_downloads]: https://img.shields.io/github/downloads/domi119017/prynterface/total
[shield_contributors]: https://img.shields.io/github/contributors/domi119017/prynterface?color=dark-green
[shield_issues]: https://img.shields.io/github/issues/domi119017/prynterface
[shield_license]: https://img.shields.io/badge/License-GPLv3-blue.svg
[shield_codecov]: https://codecov.io/gh/domi119017/prynterface/branch/master/graph/badge.svg?token=DFD15VCX40

<!-- Misc -->
[printrun]: https://github.com/kliment/Printrun


<!-- 
@todo Create logos, screenshots, etc.
logos: @domi119017
Screenshot: https://carbon.now.sh/ @domi119017
-->

<!-- Project Logo -->
[![Logo][repo_logo_combined]][repo_main]

Welcome! This is the **development branch** for [Prynterface][repo_main].

[![License][shield_license]][repo_license]
[![Contributors][shield_contributors]][repo_main]
[![Issues][shield_issues]][repo_main]
[![codecov][shield_codecov]][repo_main]

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [What about Printrun/Pronterface?](#what-about-printrunpronterface)
  - [The Plan:](#the-plan)
- [Building With](#building-with)
- [Getting Started (Developing)](#getting-started-developing)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
  - [Creating A Pull Request](#creating-a-pull-request)
- [License](#license)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## About The Project

[![Screenshot][project_screenshot]](#getting-started)

Prynterface will be a python application for interfacing with 3D printers over serial connection.

### What about [Printrun/Pronterface][printrun]?
First of all, Printrun is a great project and I highly recommend it. <br>
However, I wanted to create a project that is more suited to my needs and that I can customize to my liking.

### The Plan:
- User interface
  - Choice between CLI and GUI
  - Customizable GUI
  - Dark / Light mode
- Interfacing with 3D printers
  - Serial connection (USB)
- Parsing: via pipelines similar to [Grafana Loki](https://grafana.com/oss/loki/)
  - Detection of temp/pos/progress/etc. updates
  - Firmware capabilities via M115 (for setting up the UI)
  - Detection of multi line responses (UBL, M420, etc.)
- Plotting
  - Temperature
  - Position
  - Progress
  - 3D Surface (for UBL)
  - Anything else customizable via pipelines/configs
- Some other stuff maybe


## Building With
TODO
<!-- @todo Add badges and info -->

## Getting Started (Developing)
TODO

<!-- @todo Getting Started (Developing) Description -->

### Prerequisites
TODO

<!-- @todo Prerequisites Description -->

### Installation
TODO

<!-- @todo Installation Description -->

## Roadmap

See the [open issues][repo_issues_open] for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/domi119017/prynterface/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the GPL-3.0 License. See [LICENSE](https://github.com/domi119017/prynterface/LICENSE) for more information.

## Authors

* [Dominik Ullrich](github.com/domi119017)

## Acknowledgements

* [ShaanCoding](https://github.com/ShaanCoding/)
* [Othneil Drew](https://github.com/othneildrew/Best-README-Template)
* [ImgShields](https://shields.io/)
