# CHANGELOG


## v0.5.1 (2024-10-31)

### Features

* feat: Feature to collect and process multiple po files from folders + command verbose incremented ([`67fb937`](https://github.com/itzune/po2dataset/commit/67fb9370163c7ffeed4fc9df74b69ac2024ebd51))

### Unknown

* Merge pull request #26 from itzune/dev

Process multiple po files from folder + more verbose ([`9f6bff7`](https://github.com/itzune/po2dataset/commit/9f6bff7c89e824fdeff6a940f779152a103e56d9))

* change: Package description changed ([`04b7554`](https://github.com/itzune/po2dataset/commit/04b7554c5046d8718d19b7561506576c8d692a9e))


## v0.5.0 (2024-10-30)

### Features

* feat: implement string placeholders algorithms ([`fbf298b`](https://github.com/itzune/po2dataset/commit/fbf298b3767ea2c7f1f42b606aa2a231608485b8))

### Fixes

* fix: Properly remove all placeholders from strings when using 'remove' placeholder policy ([`497940e`](https://github.com/itzune/po2dataset/commit/497940e1b8882b6f435e0c900679318f10ce7713))

### Unknown

* Merge pull request #25 from itzune/dev

String placeholder algorithms ([`5b1430e`](https://github.com/itzune/po2dataset/commit/5b1430e3f592c530d9a32cf662a537286573a62d))


## v0.4.0 (2024-10-25)

### Fixes

* fix: README needs corrections ([`3a9b93d`](https://github.com/itzune/po2dataset/commit/3a9b93d383a3a4828732d9678d4505176f85029b))

### Refactoring

* refactor: reorder imports + add some placeholder definitions ([`5f7a46f`](https://github.com/itzune/po2dataset/commit/5f7a46ff180310051f5202cda8891901a0e74821))

### Testing

* test: add more test assets to the readme test ([`0180d17`](https://github.com/itzune/po2dataset/commit/0180d17296e9578a8cf91e94e7456446d50d2db2))

### Unknown

* Merge pull request #24 from itzune/dev

Some fix and tests ([`bd9f89e`](https://github.com/itzune/po2dataset/commit/bd9f89eb88b4860ca22414bba3440628363ffd10))


## v0.3.1 (2024-10-25)

### Features

* feat: add readme function implemented + test for this function ([`35c27d5`](https://github.com/itzune/po2dataset/commit/35c27d5166b0c2b567754a3c0cd35655645ebbf6))

### Unknown

* Merge pull request #23 from itzune/dev

Documentation + Option to add custom README file into a project ([`25c77cf`](https://github.com/itzune/po2dataset/commit/25c77cfcac05b0b1a081f37dc2bc234d77d8cc61))

* add: more information with use cases in README ([`f48920f`](https://github.com/itzune/po2dataset/commit/f48920faa585127e8c5d768d779b7a539aacd7f0))

* Test README file added ([`fc753e3`](https://github.com/itzune/po2dataset/commit/fc753e39c836bf7eab28deecb77d506de6860473))

* Add: Changelog path added to pyproject.toml ([`7b5dc18`](https://github.com/itzune/po2dataset/commit/7b5dc1846f2e1b790e7cbc804d01ad804936c099))


## v0.3.0 (2024-10-22)

### Build System

* build(deps): bump tox from 4.23.0 to 4.23.2

Bumps [tox](https://github.com/tox-dev/tox) from 4.23.0 to 4.23.2.
- [Release notes](https://github.com/tox-dev/tox/releases)
- [Changelog](https://github.com/tox-dev/tox/blob/main/docs/changelog.rst)
- [Commits](https://github.com/tox-dev/tox/compare/4.23.0...4.23.2)

---
updated-dependencies:
- dependency-name: tox
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] <support@github.com> ([`de104db`](https://github.com/itzune/po2dataset/commit/de104dbde5d13c1a59b9db4a31750c67d7e135df))

* build(deps): bump tox from 4.21.2 to 4.23.0

Bumps [tox](https://github.com/tox-dev/tox) from 4.21.2 to 4.23.0.
- [Release notes](https://github.com/tox-dev/tox/releases)
- [Changelog](https://github.com/tox-dev/tox/blob/main/docs/changelog.rst)
- [Commits](https://github.com/tox-dev/tox/compare/4.21.2...4.23.0)

---
updated-dependencies:
- dependency-name: tox
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] <support@github.com> ([`05e795f`](https://github.com/itzune/po2dataset/commit/05e795f30b44a3f648f3bda8beac681ff542bf99))

### Unknown

* Merge pull request #22 from itzune/dependabot/pip/tox-4.23.2

build(deps): bump tox from 4.23.0 to 4.23.2 ([`0249192`](https://github.com/itzune/po2dataset/commit/024919250012a2b7bd958e42bcc4dd00f0f3217b))

* Merge pull request #21 from urtzai/dependabot/pip/tox-4.23.0

build(deps): bump tox from 4.21.2 to 4.23.0 ([`850049e`](https://github.com/itzune/po2dataset/commit/850049e51bc669600f4ce7da3c3412e0ef9855b9))


## v0.2.0 (2024-10-11)

### Fixes

* fix: a step cannot have both the  and  keys ([`9509e78`](https://github.com/itzune/po2dataset/commit/9509e78f3ea3fe2350ad10b8f12e8763de262f9a))

* fix: another workflow change in order to have python enviroment and tools properly installed ([`d3a3d23`](https://github.com/itzune/po2dataset/commit/d3a3d235dc8d882ede8b1a310c5f634803710fa3))

* fix: unclosed array ([`cd9421b`](https://github.com/itzune/po2dataset/commit/cd9421b82dfc3fa4d9440a1f0e94c6861f2fa9d0))

* fix: semantic release #7 ([`f9f9a51`](https://github.com/itzune/po2dataset/commit/f9f9a515457a506f29a248e7e478c7ca23b5bb52))

* fix: Semantic release workflow ([`5587306`](https://github.com/itzune/po2dataset/commit/55873060fd3feefd59cd0f3291ed30ca92137fda))

* fix: use pypa/gh-action-pypi-publish@release/v1 as publisher ([`06b43a0`](https://github.com/itzune/po2dataset/commit/06b43a0435bd89569f39080689bb0261c344f6c7))

* fix: Tests are launched in dev branch ([`7dab16f`](https://github.com/itzune/po2dataset/commit/7dab16f68ee6ef844720aca1c925cf896c4b0f2c))

### Unknown

* Merge pull request #20 from urtzai/dev

Workflow change ([`f0105f3`](https://github.com/itzune/po2dataset/commit/f0105f3a3244d63a227d6984e9b3888342e8f4f8))

* remove python build setup and insert build installation directly in the semantic release build_command definition ([`6a40081`](https://github.com/itzune/po2dataset/commit/6a400815ba6d58955966fabb9ded336eb98bd36f))

* Merge pull request #19 from urtzai/dev

Dev ([`5391cf1`](https://github.com/itzune/po2dataset/commit/5391cf17a6ae70901ed9b8b4da25ec53c1413b1e))

* downgrade release version ([`28c1a0b`](https://github.com/itzune/po2dataset/commit/28c1a0bbb5808e3ec0ea515ef00e80370d9194fa))

* removed repo_dir setup ([`76ca11b`](https://github.com/itzune/po2dataset/commit/76ca11bdfa71b5a6523f94f02a67c935c3b073cc))

* Merge pull request #18 from urtzai/dev

fix: a step cannot have both the  and  keys ([`ec5a450`](https://github.com/itzune/po2dataset/commit/ec5a4502082598c94358d90fd32b586659725969))

* Merge pull request #17 from urtzai/dev

Workflow changes ([`819e2a1`](https://github.com/itzune/po2dataset/commit/819e2a1a1890ba4dc5b557fb800fcced5d3cb2c4))

* Merge branch 'main' of github.com:urtzai/po2dataset into dev ([`748b707`](https://github.com/itzune/po2dataset/commit/748b707f22cc4efe095ff5364f676845da7149e3))

* Merge pull request #16 from urtzai/dev

Semantic release working ([`4002bac`](https://github.com/itzune/po2dataset/commit/4002bac02edfcbf5c2278606b6ed729bf8071e15))

* Merge branch 'main' of github.com:urtzai/po2dataset into dev ([`f60531c`](https://github.com/itzune/po2dataset/commit/f60531c38e0a427bb865f7f532ae79f157b608f4))

* Merge pull request #15 from urtzai/dev

Release test ([`a27158f`](https://github.com/itzune/po2dataset/commit/a27158f61ab078dc582d7514883dde8920d52da9))

* Merge branch 'main' of github.com:urtzai/po2dataset into dev ([`a1d84c2`](https://github.com/itzune/po2dataset/commit/a1d84c2a4820cdba3e6386d7cb633c1a7d39e419))

* Merge pull request #14 from urtzai/dev

fix: Semantic release workflow ([`8ed9d24`](https://github.com/itzune/po2dataset/commit/8ed9d24b23df9651d1b16bc72ee6c3c02f6d20ad))

* remove releaser ([`8891f66`](https://github.com/itzune/po2dataset/commit/8891f66027e25e6f522d668c3b941980246210ac))

* Workflow changes ([`6816e93`](https://github.com/itzune/po2dataset/commit/6816e932790c927e36f72643414c1a1d3aaf3d63))

* Merge pull request #13 from urtzai/dev

Semantic releaser fix ([`8af7254`](https://github.com/itzune/po2dataset/commit/8af7254e7868e73f41ebd71a0ad6688dd5678333))

* Changelog modified again ([`4a9f339`](https://github.com/itzune/po2dataset/commit/4a9f339d8f45b16f0dc9cd12a9cdfdc708c61496))

* Merge branch 'main' of github.com:urtzai/po2dataset into dev ([`bc85e42`](https://github.com/itzune/po2dataset/commit/bc85e42e73aec8557eac9b689453bb050fa8068d))

* Merge pull request #12 from urtzai/dev

Updated changelog to current state ([`cffdc6e`](https://github.com/itzune/po2dataset/commit/cffdc6e5550f0dcf4542418c98bd19b6db1ab158))

* changed: Semantic release workflow changed + releaser code added ([`95caf52`](https://github.com/itzune/po2dataset/commit/95caf52daac223ce5d2971c09e441c8332e67d37))

* Updated changelog to current state ([`8e906f4`](https://github.com/itzune/po2dataset/commit/8e906f4a92fbabbea8fb1b9c6363459679a5bf8a))

* Merge pull request #11 from urtzai/dev

fix: use pypa/gh-action-pypi-publish@release/v1 as publisher ([`fe86c4a`](https://github.com/itzune/po2dataset/commit/fe86c4a9a1ca48b57b6d5a911eb3a866bc11861c))

* Merge pull request #8 from urtzai/dev

Added semantic release workflow ([`4feca71`](https://github.com/itzune/po2dataset/commit/4feca717447092190867b6870cd7e1dcb3481543))

* Delete python-publish.yml ([`c98dfb0`](https://github.com/itzune/po2dataset/commit/c98dfb07ab8cce3d9187a443ea83ee143b445c07))

* Create semantic-release.yml ([`2a12c8b`](https://github.com/itzune/po2dataset/commit/2a12c8b8f35af5d33d568858631f977232f757f6))

* Merge pull request #9 from urtzai/urtzai-patch-1

fix: Tests are launched in dev branch ([`2558572`](https://github.com/itzune/po2dataset/commit/2558572b28a2aebc50af1d66539fced1f255d8dc))


## v0.1.0 (2024-10-09)

### Features

* feat: Make po2dataset executable from command line + added an argument to add open licence file automatically ([`45a22be`](https://github.com/itzune/po2dataset/commit/45a22be3046f37c66e83e9c4d4bb03f9792f03fa))

* feat: Generic tests included in the project ([`d9068fd`](https://github.com/itzune/po2dataset/commit/d9068fdcfb8247efcbcd94026af9aba517e35ebf))

### Fixes

* fix: requests dependency added to requeriments.txt file ([`714bc49`](https://github.com/itzune/po2dataset/commit/714bc49d53df4ea226a120ea8ae4c82befec7370))

* fix: typo error in README file ([`e6c7bd9`](https://github.com/itzune/po2dataset/commit/e6c7bd94b9976e334bb87d6cef5a3648c75719ba))

* fix: #1 Write the first README doc ([`8ed55d1`](https://github.com/itzune/po2dataset/commit/8ed55d1b18b2e88a8738ccb233e8ddabc4215cbe))

* fix: #6 Filter translated strings from the po file ([`25d6eaf`](https://github.com/itzune/po2dataset/commit/25d6eaf6cf9f80ef3d8afe14525533998a6c1c67))

### Unknown

* Bump version ([`d196b6d`](https://github.com/itzune/po2dataset/commit/d196b6d49c879eef059c22a6e9abad9710f44420))

* change: Update README ([`dc9af69`](https://github.com/itzune/po2dataset/commit/dc9af69095fa46dd1393e322fca7b61cb6789a6d))

* add: Some badgets added ([`28399e1`](https://github.com/itzune/po2dataset/commit/28399e133e752726f0d96b8d55aaceefdce49a26))

* change: Changed to tox.ini configuration file for better compatibility ([`743b805`](https://github.com/itzune/po2dataset/commit/743b80555a43270620374f96df439b7318b1c2df))

* fix cache dependency and project root directory ([`4082100`](https://github.com/itzune/po2dataset/commit/40821009c139acdd9df93aa6e85b366ea6b8fa0a))

* Create dependabot.yml ([`1d0a20f`](https://github.com/itzune/po2dataset/commit/1d0a20fe77fc312160ca66ea9ee2f3098502da27))

* Delete .github/workflows/dependabot.yml ([`ab4a56a`](https://github.com/itzune/po2dataset/commit/ab4a56a9e412784fce6ddf33e9cd47b267c8e7d6))

* Update dependabot.yml ([`15abe0e`](https://github.com/itzune/po2dataset/commit/15abe0e8c23ac017aec449390e327ab37c24dd72))

* first dependabot workflow ([`e7819da`](https://github.com/itzune/po2dataset/commit/e7819da74dbc09c997c35afc342d9b834b6ad2e3))

* Update python-publish.yml ([`7ec9a89`](https://github.com/itzune/po2dataset/commit/7ec9a89dc82c1903db4e89fb2401434990b9653c))

* Update python-publish.yml ([`a3e923e`](https://github.com/itzune/po2dataset/commit/a3e923e479fcb75018a2699ae28b1cc474e4e308))

* Publishing with a Trusted Publisher ([`19b4151`](https://github.com/itzune/po2dataset/commit/19b41515b69d60a513d8ec9f2b7d698ff31412e3))

* Update pyproject.toml ([`f8b58d6`](https://github.com/itzune/po2dataset/commit/f8b58d6ce9be7ef6a2090f1f11ec7c5c474e0a8b))

* Bump version ([`01fc8c8`](https://github.com/itzune/po2dataset/commit/01fc8c860c5d2ca68a773041b6a42d4b099eac0e))

* First python-publish workflow ([`76ca593`](https://github.com/itzune/po2dataset/commit/76ca59367fb4ef5b4655808caa29e06a69adab59))

* First functional command line tool ([`ed32337`](https://github.com/itzune/po2dataset/commit/ed32337d87e364b896b20d10894b53e67aa164f1))

* change: fine tunning project metadata ([`bfdbd51`](https://github.com/itzune/po2dataset/commit/bfdbd51d46cfc4335c239a1438b65b46656a131d))

* Merge branch 'main' of github.com:urtzai/po2dataset ([`739e1e1`](https://github.com/itzune/po2dataset/commit/739e1e121e72fed40aa24ade385c348ba52c2d49))

* Initial commit ([`66c2b7a`](https://github.com/itzune/po2dataset/commit/66c2b7a38f1138cbf176ef7a2c82fda67240b01e))

* add: First package structure ([`55e0049`](https://github.com/itzune/po2dataset/commit/55e0049ebb258a77037964b15e8e6a274c3900f1))
