[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL3 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Ask Me Anything][ask-me-anything]][personal-page]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/stiliajohny/Repo-Template">
    <img src=".assets/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Molecule Cookiecutter Template</h3>

  <p align="center">
    This is  a template to be used with cookiecuter to create a molecule role
    <br />
    <a href="./README.md"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/stiliajohny/Repo-Template/issues/new?labels=i%3A+bug&template=1-bug-report.md">Report Bug</a>
    ·
    <a href="https://github.com/stiliajohny/Repo-Template/issues/new?labels=i%3A+enhancement&template=2-feature-request.md">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [To initialize the role with cookiecuter](#to-initialize-the-role-with-cookiecuter)
  - [To initialize the role with molecule](#to-initialize-the-role-with-molecule)
  - [To test the default scenario docker](#to-test-the-default-scenario-docker)
  - [To test the scenario with vagrant](#to-test-the-scenario-with-vagrant)
- [What this template provides?](#what-this-template-provides)
- [Directory structure](#directory-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

[![Molecule CookieCutter Template][product-screenshot]](./.assets/screenshot.png)

<!--
There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need.

Here's why:

- Your time should be focused on creating something amazing. A project that solves a problem and helps others
- You shouldn't be doing the same tasks over and over like creating a README from scratch
- You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I find helpful are listed in the acknowledgements.
-->

### Built With

- Cookiecutter
-  Molecule
-  Python
-  YAML
-  Ansible
-  JSON
-  Docker

---

<!-- GETTING STARTED -->

## Getting Started

<!--
This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
-->

### Prerequisites

-  cookiecutter
-  pre-commit
-   molecule-vagrant
-   molecule-docker
-  Vagrant
-  Docker

### Installation

Install them doing `pip install cookiecutter pre-commit molecule-vagrant molecule-docker`

---


## Usage

### To initialize the role with cookiecuter

`$ pip install cookiecutter pre-commit`

`$ cookiecutter gh:cat-oid/ansible-molecule-cookiecutter`


### To initialize the role with molecule


`$ pip install molecule pre-commit`

`$ molecule init template --url https://github.com/cat-oid/ansible-molecule-cookiecutter`

### To test the default scenario docker

`$ molecule test`

### To test the scenario with vagrant
`$ molecule test -s vagrant`

---
## What this template provides?

* Initialize a new git repo in the local machine
* Add [.yamllint](https://github.com/adrienverge/yamllint) config file (used by molecule)
* Add .pre-commit-config.yaml used by [pre-commit](http://pre-commit.com/)
* Add .gitignore with common files I don't want to track in git
* Add configuration for [Molecule](http://molecule.readthedocs.io) in the "molecule" folder
  * default molecule scenario runs on docker
  * There is another molecule scenario using Vagrant
  * The vagrant scenario requires `pip install molecule-vagrant`
* Add a travis or Gitlab-CI config file (Optional. By default it's not added)
* Populates, variables, tasks, handlers on demand
* Checks role name validity

---

## Directory structure
```
ansible-role-example/
├── defaults
│   └── main.yml
├── .gitignore
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   ├── default
│   │   ├── converge.yml
│   │   ├── INSTALL.rst
│   │   ├── molecule.yml
│   │   └── verify.yml
│   └── vagrant
│       ├── converge.yml
│       ├── INSTALL.rst
│       ├── molecule.yml
│       └── verify.yml
├── .pre-commit-config.yaml
├── README.md
├── tasks
│   └── main.yml
├── vars
│   └── main.yml
└── .yamllint
```

---

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/stiliajohny/Repo-Template/issues) for a list of proposed features (and known issues).

---

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<!-- LICENSE -->

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

John Stilia - [@john_stilia](https://twitter.com/john_stilia) - stilia.johny@gmail.com


---
<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/stiliajohny/Repo-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/stiliajohny/Repo-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/stiliajohny/Repo-Template.svg?style=for-the-badge
[forks-url]: https://github.com/stiliajohny/Repo-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/stiliajohny/Repo-Template.svg?style=for-the-badge
[stars-url]: https://github.com/stiliajohny/Repo-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/stiliajohny/Repo-Template.svg?style=for-the-badge
[issues-url]: https://github.com/stiliajohny/Repo-Template/issues
[license-shield]: https://img.shields.io/github/license/stiliajohny/Repo-Template?style=for-the-badge
[license-url]: https://github.com/stiliajohny/Repo-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/johnstilia/
[product-screenshot]: .assets/screenshot.png
[ask-me-anything]: https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg?style=for-the-badge
[personal-page]: https://github.com/stiliajohny

https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
https://img.shields.io/github/license/stiliajohny/Repo-Template.svg?style=for-the-badge
