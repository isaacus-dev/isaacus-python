# Changelog

## 0.10.1 (2026-02-03)

Full Changelog: [v0.10.0...v0.10.1](https://github.com/isaacus-dev/isaacus-python/compare/v0.10.0...v0.10.1)

### Documentation

* **api:** added examples to 200 response codes ([a92b0d7](https://github.com/isaacus-dev/isaacus-python/commit/a92b0d79fad4552d3be5442dec404791f08040e1))

## 0.10.0 (2026-02-03)

Full Changelog: [v0.9.1...v0.10.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.9.1...v0.10.0)

### Features

* **api:** add min max ([50ece81](https://github.com/isaacus-dev/isaacus-python/commit/50ece81e21c605fd2801e2037f52046afe32a7f4))
* **api:** switch to span objects for enrichment, note closed beta ([326b7dc](https://github.com/isaacus-dev/isaacus-python/commit/326b7dca713b9240bb6ea825f5361de804ca300b))
* **sdk:** add enrichments ([eb4057b](https://github.com/isaacus-dev/isaacus-python/commit/eb4057b54a26158aded93e0b943e9828c5457b39))


### Bug Fixes

* **client:** close streams without requiring full consumption ([13eb93f](https://github.com/isaacus-dev/isaacus-python/commit/13eb93fea611507de440a4418b82de3aa8a06500))
* compat with Python 3.14 ([89ef152](https://github.com/isaacus-dev/isaacus-python/commit/89ef152681673c408e217ad44f51dba229f9d371))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([4d7b71d](https://github.com/isaacus-dev/isaacus-python/commit/4d7b71de78bdd83f00d16ec409c57cbe4dd01ebb))
* ensure streams are always closed ([c2ae554](https://github.com/isaacus-dev/isaacus-python/commit/c2ae554fd73a5f0d4c0f7eb9a2fa652669d38f2e))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([b89d4ce](https://github.com/isaacus-dev/isaacus-python/commit/b89d4ce184708ad0737ba7fc77f1afe270a8eb50))
* use async_to_httpx_files in patch method ([30ffab2](https://github.com/isaacus-dev/isaacus-python/commit/30ffab28e37d4f940e69f2afe199fad830f57ba0))


### Chores

* add missing docstrings ([0c4e7d4](https://github.com/isaacus-dev/isaacus-python/commit/0c4e7d4039a6b60adccc39be7a98b9efdbbc3df4))
* add Python 3.14 classifier and testing ([083d4b6](https://github.com/isaacus-dev/isaacus-python/commit/083d4b600ddba22fc81c33da7dee079c97088c81))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([9612e35](https://github.com/isaacus-dev/isaacus-python/commit/9612e35c83634a774c507349b4cd211d4d8c2c84))
* **docs:** use environment variables for authentication in code snippets ([ac22598](https://github.com/isaacus-dev/isaacus-python/commit/ac2259872f666a3c0cdb57695623aa980e5bdf36))
* **internal/tests:** avoid race condition with implicit client cleanup ([871fa54](https://github.com/isaacus-dev/isaacus-python/commit/871fa54adcd54f3f5ffde794e4ae703e7913e6b7))
* **internal:** add missing files argument to base client ([669f50a](https://github.com/isaacus-dev/isaacus-python/commit/669f50a93bc5868ff80a48e0a29c4a53e362fa99))
* **internal:** grammar fix (it's -&gt; its) ([84145f2](https://github.com/isaacus-dev/isaacus-python/commit/84145f233adddf8b55a24b0443a2f9c9dc5a4cbd))
* **package:** drop Python 3.8 support ([556d5d0](https://github.com/isaacus-dev/isaacus-python/commit/556d5d07c941f4e2c4b6e523756723ce5661c4b3))
* speedup initial import ([2d500ed](https://github.com/isaacus-dev/isaacus-python/commit/2d500ed45248bf120cd21236644d9573d563120b))
* update lockfile ([b53392a](https://github.com/isaacus-dev/isaacus-python/commit/b53392a51c7b7e8605880af51e53db044ad14d94))


### Documentation

* **sdk:** specify example params ([f617346](https://github.com/isaacus-dev/isaacus-python/commit/f617346d3262a45594d34357e97fc616f5ddf9e9))

## 0.9.1 (2025-10-19)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/isaacus-dev/isaacus-python/compare/v0.9.0...v0.9.1)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([7a85243](https://github.com/isaacus-dev/isaacus-python/commit/7a85243fcfb9d5b78d522d336310dcd1f009e904))

## 0.9.0 (2025-10-14)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.8.0...v0.9.0)

### ⚠ BREAKING CHANGES

* **api:** reduce max length of embeddings input
* **sdk:** add `_response` to response models to finally fix duplicated names

### Features

* **api:** added embedding endpoint ([88190d6](https://github.com/isaacus-dev/isaacus-python/commit/88190d6d33c8d5e3cf59dfd3c488b5ae9abec93b))
* **api:** reduce max length of embeddings input ([0ad7114](https://github.com/isaacus-dev/isaacus-python/commit/0ad7114b5fec2fde9aaa830a6ba6163ad3b6fccc))
* **api:** rename embedding -&gt; embeddings ([204a05d](https://github.com/isaacus-dev/isaacus-python/commit/204a05d7b1504901766db3c0d0d8ea47a22a16ed))
* **api:** revert embedding -&gt; embeddings ([b934279](https://github.com/isaacus-dev/isaacus-python/commit/b9342795e50374817b8e3dc2e2f1163a2ff0805a))
* **client:** support file upload requests ([2ab398d](https://github.com/isaacus-dev/isaacus-python/commit/2ab398dde07e98411c9b6efd76f7b7120a9633a8))
* improve future compat with pydantic v3 ([5a20497](https://github.com/isaacus-dev/isaacus-python/commit/5a20497a9c4bbf88056df12a0c686566dc9bd162))
* **sdk:** add embeddings endpoint ([920ae0b](https://github.com/isaacus-dev/isaacus-python/commit/920ae0b65f2362ac098f8b94979b1e821f5143d8))
* **sdk:** toggle to force regen ([cf60482](https://github.com/isaacus-dev/isaacus-python/commit/cf60482ba0dd3933daee477fa9bd4ae29d900fb4))
* **sdk:** untoggle to force regen ([25d2067](https://github.com/isaacus-dev/isaacus-python/commit/25d2067fad4bb46ca595001f6e82458fd3d24a23))
* **types:** replace List[str] with SequenceNotStr in params ([d2733a9](https://github.com/isaacus-dev/isaacus-python/commit/d2733a9d0f16531537a9db017a8e29d2c8fb3912))


### Bug Fixes

* **api:** typo ([5d4a1b9](https://github.com/isaacus-dev/isaacus-python/commit/5d4a1b99e8a6ac2a1c3cc4e83e7b65108eea335a))
* avoid newer type syntax ([10253fe](https://github.com/isaacus-dev/isaacus-python/commit/10253fe93ed8142b52cf5199486221e81ac6ce5a))
* **sdk:** add `_response` to response models to finally fix duplicated names ([5c7462d](https://github.com/isaacus-dev/isaacus-python/commit/5c7462dd25c67c44126eb946a656a6b841dc6a50))


### Chores

* **api:** try to force regen SDK ([2fafb55](https://github.com/isaacus-dev/isaacus-python/commit/2fafb555c1a20d7c359c91c35fd1f54868cffe54))
* do not install brew dependencies in ./scripts/bootstrap by default ([57b055e](https://github.com/isaacus-dev/isaacus-python/commit/57b055ed56fdcc58b4663e4ddad32afac25e7ec1))
* improve example values ([35b03bd](https://github.com/isaacus-dev/isaacus-python/commit/35b03bdbf4ceaccd00102e23d639a01d5bea136a))
* **internal:** add Sequence related utils ([5a2287e](https://github.com/isaacus-dev/isaacus-python/commit/5a2287ef854d250048c070f3fd88b00ca84b0d3c))
* **internal:** change ci workflow machines ([f86cbce](https://github.com/isaacus-dev/isaacus-python/commit/f86cbcef2583658466e95eaba4aba61f79646ef9))
* **internal:** codegen related update ([22b520b](https://github.com/isaacus-dev/isaacus-python/commit/22b520b3c67e570f9267135111a89542ee2bdf7f))
* **internal:** fix ruff target version ([889d576](https://github.com/isaacus-dev/isaacus-python/commit/889d576cdc28d06404c6ee3ce0c67bf4d3be75c4))
* **internal:** move mypy configurations to `pyproject.toml` file ([d5732d5](https://github.com/isaacus-dev/isaacus-python/commit/d5732d5e0145763723e8be24cbd8296f9a385264))
* **internal:** update comment in script ([7af966e](https://github.com/isaacus-dev/isaacus-python/commit/7af966e1677b44d412eda96c5ee8e9866f77ccfb))
* **internal:** update pydantic dependency ([68a7057](https://github.com/isaacus-dev/isaacus-python/commit/68a70578a2e269fa3b2c46e3c29e82ba770090d6))
* **internal:** update pyright exclude list ([6f0ae86](https://github.com/isaacus-dev/isaacus-python/commit/6f0ae86899883fe77aa669d595c623bedc2dc5c8))
* remove custom code ([491dbdc](https://github.com/isaacus-dev/isaacus-python/commit/491dbdcd82984d099b8ee11e94894ad450b2424d))
* **sdk:** restore original example ([079645e](https://github.com/isaacus-dev/isaacus-python/commit/079645e85259c2e4d3f6aa86b2ca2c21ce97367a))
* **tests:** simplify `get_platform` test ([e00ccd0](https://github.com/isaacus-dev/isaacus-python/commit/e00ccd0c41c3751eb3fae880223ebb05eae0f154))
* **types:** change optional parameter type from NotGiven to Omit ([38d13e0](https://github.com/isaacus-dev/isaacus-python/commit/38d13e0514b001d1a34446b881783d559e246865))
* update @stainless-api/prism-cli to v5.15.0 ([a3141f5](https://github.com/isaacus-dev/isaacus-python/commit/a3141f59b0ff6334fde2a9740fd2f86824fe5083))
* update github action ([0518028](https://github.com/isaacus-dev/isaacus-python/commit/05180288265bc111dba1c62fbfcd90139a6299ad))


### Documentation

* **sdk:** make embeddings example first ([caa70f7](https://github.com/isaacus-dev/isaacus-python/commit/caa70f7acf6ce910d8cf80425437ca51970cd255))

## 0.8.0 (2025-07-25)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.7.0...v0.8.0)

### Features

* clean up environment call outs ([3ee6948](https://github.com/isaacus-dev/isaacus-python/commit/3ee69481b6a6198503d06c6aa137ba69f7940db6))
* **client:** add support for aiohttp ([fba17e9](https://github.com/isaacus-dev/isaacus-python/commit/fba17e98279aa6d93dd3c9b6f9b95246b4fac813))


### Bug Fixes

* **ci:** correct conditional ([53c81d9](https://github.com/isaacus-dev/isaacus-python/commit/53c81d9e14882ae83a72c15481c8933226e668fa))
* **ci:** release-doctor — report correct token name ([3cb8672](https://github.com/isaacus-dev/isaacus-python/commit/3cb8672052edf1d1c4e72a5866fde3776d43a4e2))
* **client:** correctly parse binary response | stream ([5e316fe](https://github.com/isaacus-dev/isaacus-python/commit/5e316feaf5270e54321a917a9cd59efb2c42fcb3))
* **client:** don't send Content-Type header on GET requests ([2a5d531](https://github.com/isaacus-dev/isaacus-python/commit/2a5d531e7553aa012352d9dd85d280f4374b7ae7))
* **parsing:** correctly handle nested discriminated unions ([c5d5715](https://github.com/isaacus-dev/isaacus-python/commit/c5d571569cdafad9bd1392baf232287dca72855d))
* **parsing:** ignore empty metadata ([dd88d17](https://github.com/isaacus-dev/isaacus-python/commit/dd88d179302966445c63831f4b6f20491fe5632e))
* **parsing:** parse extra field types ([ba334c7](https://github.com/isaacus-dev/isaacus-python/commit/ba334c75676c37da235abfddd7c9746f89307c22))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([638c7c4](https://github.com/isaacus-dev/isaacus-python/commit/638c7c4df7ecbc189480a0cba2d93125f9b97d2f))


### Chores

* **ci:** change upload type ([e79525c](https://github.com/isaacus-dev/isaacus-python/commit/e79525c4ffe9601c3b7c5e39a94c93c248cfbf33))
* **ci:** enable for pull requests ([29244fd](https://github.com/isaacus-dev/isaacus-python/commit/29244fdb33a5706480e1c7314099a14ae177ee06))
* **ci:** only run for pushes and fork pull requests ([94ed1eb](https://github.com/isaacus-dev/isaacus-python/commit/94ed1ebf9fc4111236f1db2a5d326f081079bdc8))
* **internal:** bump pinned h11 dep ([5836163](https://github.com/isaacus-dev/isaacus-python/commit/58361635226de79f5ff27e953ec03dfeb392b3e0))
* **internal:** codegen related update ([cdfe0be](https://github.com/isaacus-dev/isaacus-python/commit/cdfe0beceeeaa21e4a24b6cdc86264dcaa3808f1))
* **internal:** update conftest.py ([e4a5936](https://github.com/isaacus-dev/isaacus-python/commit/e4a59368bd7d42d65fd368b03a208b2aa32a9144))
* **package:** mark python 3.13 as supported ([0f7b5d1](https://github.com/isaacus-dev/isaacus-python/commit/0f7b5d1c588adf28b502727948dceaa9ed54ee86))
* **project:** add settings file for vscode ([d6435b0](https://github.com/isaacus-dev/isaacus-python/commit/d6435b09a03f202867843ee83737b319ccef4ea6))
* **readme:** fix version rendering on pypi ([b09f1ad](https://github.com/isaacus-dev/isaacus-python/commit/b09f1ad5ce2624d23a32fc1d966f7d9703cd4ad3))
* **readme:** update badges ([cd48569](https://github.com/isaacus-dev/isaacus-python/commit/cd485693063d03f092d5be7f024b0f7e23da0897))
* **tests:** add tests for httpx client instantiation & proxies ([5d2c5b9](https://github.com/isaacus-dev/isaacus-python/commit/5d2c5b9e20bd80acd05240217b6be3991b46aae2))
* **tests:** run tests in parallel ([3f0e6da](https://github.com/isaacus-dev/isaacus-python/commit/3f0e6da6d9c6d9cd46cfa382da55a0b6a07d9d49))
* **tests:** skip some failing tests on the latest python versions ([b2b3fa8](https://github.com/isaacus-dev/isaacus-python/commit/b2b3fa82b87e9cc7e23164cc5589b3e157e635df))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([b68d394](https://github.com/isaacus-dev/isaacus-python/commit/b68d3944df0ca58b7df3e89e06e90799f7ade25b))

## 0.7.0 (2025-06-03)

Full Changelog: [v0.6.1...v0.7.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.6.1...v0.7.0)

### Features

* **client:** add follow_redirects request option ([40221d5](https://github.com/isaacus-dev/isaacus-python/commit/40221d56d887dcfb693d67883a47403c680f6062))


### Chores

* **ci:** fix installation instructions ([157308b](https://github.com/isaacus-dev/isaacus-python/commit/157308b71eefc75af2e76acd10664eb5633b9110))
* **ci:** upload sdks to package manager ([9f9915c](https://github.com/isaacus-dev/isaacus-python/commit/9f9915ce18a288ab157b8f75c21de724507267d7))
* **docs:** grammar improvements ([eb2766f](https://github.com/isaacus-dev/isaacus-python/commit/eb2766f59d477222ae93c06c32e06ab1ff94645f))
* **docs:** remove reference to rye shell ([96a0239](https://github.com/isaacus-dev/isaacus-python/commit/96a0239f103261c69ead957c62fdee27497192ed))

## 0.6.1 (2025-05-10)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/isaacus-dev/isaacus-python/compare/v0.6.0...v0.6.1)

### Bug Fixes

* **client:** fix bug where types occasionally wouldn't generate ([e1bec40](https://github.com/isaacus-dev/isaacus-python/commit/e1bec4066b30cfefa004cdddc620c4c8131bd0de))
* **package:** support direct resource imports ([46ada4d](https://github.com/isaacus-dev/isaacus-python/commit/46ada4d158767a9dc03f19222009a853c5626cc7))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([e4ffb62](https://github.com/isaacus-dev/isaacus-python/commit/e4ffb62a053ec88a60667a8a1e149a15d5f61a86))
* **internal:** codegen related update ([ed8951f](https://github.com/isaacus-dev/isaacus-python/commit/ed8951f3943af3be84ea11a363e6ac3c23e37b2b))


### Documentation

* **api:** fixed incorrect description of how extraction results are ordered ([4c6ee63](https://github.com/isaacus-dev/isaacus-python/commit/4c6ee63ab3b274ee76cb56f526004f2f63dbb0ac))
* remove or fix invalid readme examples ([71a39ed](https://github.com/isaacus-dev/isaacus-python/commit/71a39ed2e5608d44fec4c1c5d83f97af6eaa4527))

## 0.6.0 (2025-04-30)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** introduced extractive QA ([7b9856c](https://github.com/isaacus-dev/isaacus-python/commit/7b9856c7a64fd4694d0fe8436934fa520faa38cc))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([40be0d5](https://github.com/isaacus-dev/isaacus-python/commit/40be0d5d7bb0c4d5187c0207e6470800e9827216))


### Chores

* broadly detect json family of content-type headers ([ef18419](https://github.com/isaacus-dev/isaacus-python/commit/ef18419dc26bba05aec8f5e29711bcc6fe329e9e))
* **ci:** add timeout thresholds for CI jobs ([f0438ce](https://github.com/isaacus-dev/isaacus-python/commit/f0438cebcfc587af81d967e610dc33ea5a53bb32))
* **ci:** only use depot for staging repos ([869c0ff](https://github.com/isaacus-dev/isaacus-python/commit/869c0ff5824ccfd63a4123a026530df11352db44))
* **internal:** codegen related update ([8860ae0](https://github.com/isaacus-dev/isaacus-python/commit/8860ae0393429d660038ce1c8d15020a42141979))
* **internal:** fix list file params ([6dc4e32](https://github.com/isaacus-dev/isaacus-python/commit/6dc4e32ab00e83d2307bfb729222f66f24a1f45f))
* **internal:** import reformatting ([57473e2](https://github.com/isaacus-dev/isaacus-python/commit/57473e25e03b551ab85b4d2ec484defdcc2de09d))
* **internal:** refactor retries to not use recursion ([513599c](https://github.com/isaacus-dev/isaacus-python/commit/513599ce261e2ec9a034715e20ec150025186255))

## 0.5.0 (2025-04-19)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.4.0...v0.5.0)

### ⚠ BREAKING CHANGES

* **api:** changed how end offsets are computed

### Features

* **api:** changed how end offsets are computed ([3c96279](https://github.com/isaacus-dev/isaacus-python/commit/3c962792d88ec5abd6ee71d9388cc1a1ba6a80dd))

## 0.4.0 (2025-04-19)

Full Changelog: [v0.3.3...v0.4.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.3.3...v0.4.0)

### ⚠ BREAKING CHANGES

* **api:** made universal classification endpoint multi-input only

### Features

* **api:** made universal classification endpoint multi-input only ([4fb2535](https://github.com/isaacus-dev/isaacus-python/commit/4fb2535407d88d51c1db1e9a37c9ea767cdf06c0))


### Chores

* **internal:** bump pyright version ([2f992e7](https://github.com/isaacus-dev/isaacus-python/commit/2f992e788860d16739438a021bd8825a7999b1e4))
* **internal:** update models test ([bb3df78](https://github.com/isaacus-dev/isaacus-python/commit/bb3df7823dd27e6482b5e97ef17019ee0a1e596c))

## 0.3.3 (2025-04-16)

Full Changelog: [v0.3.2...v0.3.3](https://github.com/isaacus-dev/isaacus-python/compare/v0.3.2...v0.3.3)

### Bug Fixes

* **perf:** optimize some hot paths ([eee757b](https://github.com/isaacus-dev/isaacus-python/commit/eee757ba44a895fcf2052b9981783b6cf233653f))
* **perf:** skip traversing types for NotGiven values ([7705a99](https://github.com/isaacus-dev/isaacus-python/commit/7705a99e0efd9724eb3260550b4b58081af85878))


### Chores

* **client:** minor internal fixes ([a8dad58](https://github.com/isaacus-dev/isaacus-python/commit/a8dad5881d0f3f5d1929574efba483a8fcdbc322))
* **internal:** codegen related update ([93cdfa0](https://github.com/isaacus-dev/isaacus-python/commit/93cdfa0c0dfc947ec76f10291887b90324301b32))
* **internal:** expand CI branch coverage ([cc5df77](https://github.com/isaacus-dev/isaacus-python/commit/cc5df7771a9ea699b0e37533070e1cb5569d7ad9))
* **internal:** reduce CI branch coverage ([2cb8fb8](https://github.com/isaacus-dev/isaacus-python/commit/2cb8fb81f4cea76d12ae3feeb09e4b43b743e8c4))
* **internal:** slight transform perf improvement ([6f47eaf](https://github.com/isaacus-dev/isaacus-python/commit/6f47eafa0ebcd31741f24bea539a4c54e88a758e))
* **internal:** update pyright settings ([7dd9ad4](https://github.com/isaacus-dev/isaacus-python/commit/7dd9ad4a4a25825929a4916168a07d74bcc52fbe))


### Documentation

* **api:** removed description of certain objects due to Mintlify bug ([9099926](https://github.com/isaacus-dev/isaacus-python/commit/90999261a360fef3ba92c52e4ad5361b79b499e6))

## 0.3.2 (2025-04-04)

Full Changelog: [v0.3.1...v0.3.2](https://github.com/isaacus-dev/isaacus-python/compare/v0.3.1...v0.3.2)

### Chores

* **internal:** remove trailing character ([#53](https://github.com/isaacus-dev/isaacus-python/issues/53)) ([1074f1e](https://github.com/isaacus-dev/isaacus-python/commit/1074f1e6817381f31f4f6b7329f596be19b0e918))

## 0.3.1 (2025-04-01)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/isaacus-dev/isaacus-python/compare/v0.3.0...v0.3.1)

### Bug Fixes

* **stainless:** added missing reranking endpoint to SDK API ([#50](https://github.com/isaacus-dev/isaacus-python/issues/50)) ([65bcc7c](https://github.com/isaacus-dev/isaacus-python/commit/65bcc7c274dc5609c1537e417c75e6b9942ac8fc))

## 0.3.0 (2025-04-01)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** added reranking endpoint ([#47](https://github.com/isaacus-dev/isaacus-python/issues/47)) ([71ef52b](https://github.com/isaacus-dev/isaacus-python/commit/71ef52b1d23c2ea924f4d178aa1201d980030fe4))

## 0.2.0 (2025-03-30)

Full Changelog: [v0.1.6...v0.2.0](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.6...v0.2.0)

### ⚠ BREAKING CHANGES

* **api:** started sorting chunks by score and added `index` field ([#45](https://github.com/isaacus-dev/isaacus-python/issues/45))

### Features

* **api:** started sorting chunks by score and added `index` field ([#45](https://github.com/isaacus-dev/isaacus-python/issues/45)) ([c9999cd](https://github.com/isaacus-dev/isaacus-python/commit/c9999cd77abfe0101a3d30536261a43404cfef6d))


### Chores

* fix typos ([#43](https://github.com/isaacus-dev/isaacus-python/issues/43)) ([0667577](https://github.com/isaacus-dev/isaacus-python/commit/066757702f47e403a06cf057f20faa5fa955b135))

## 0.1.6 (2025-03-18)

Full Changelog: [v0.1.5...v0.1.6](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.5...v0.1.6)

### Chores

* update SDK settings ([#40](https://github.com/isaacus-dev/isaacus-python/issues/40)) ([6423efc](https://github.com/isaacus-dev/isaacus-python/commit/6423efc8ef532dabfe1f7213da5a9e27860a63a9))

## 0.1.5 (2025-03-17)

Full Changelog: [v0.1.4...v0.1.5](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.4...v0.1.5)

### Bug Fixes

* **ci:** ensure pip is always available ([#36](https://github.com/isaacus-dev/isaacus-python/issues/36)) ([36a0c57](https://github.com/isaacus-dev/isaacus-python/commit/36a0c57afe1ebeab214bd06072ece3710472a591))
* **ci:** remove publishing patch ([#38](https://github.com/isaacus-dev/isaacus-python/issues/38)) ([ff4ced3](https://github.com/isaacus-dev/isaacus-python/commit/ff4ced35d19f34c531b25eef905133f4489e265c))

## 0.1.4 (2025-03-15)

Full Changelog: [v0.1.3...v0.1.4](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.3...v0.1.4)

### Features

* **api:** added latest OpenAPI specification ([#29](https://github.com/isaacus-dev/isaacus-python/issues/29)) ([411d83f](https://github.com/isaacus-dev/isaacus-python/commit/411d83f2da5913573e8e09c281a5dfb949670bf9))
* **api:** added latest OpenAPI specification ([#33](https://github.com/isaacus-dev/isaacus-python/issues/33)) ([b053a4a](https://github.com/isaacus-dev/isaacus-python/commit/b053a4a60f48d9d3197d384fe6e3a57723216ac9))
* **api:** added latest OpenAPI specification ([#34](https://github.com/isaacus-dev/isaacus-python/issues/34)) ([d9aef7f](https://github.com/isaacus-dev/isaacus-python/commit/d9aef7fa1d6f5283bdd3afd1962f52d2ed072499))


### Bug Fixes

* **types:** handle more discriminated union shapes ([#32](https://github.com/isaacus-dev/isaacus-python/issues/32)) ([0644ad3](https://github.com/isaacus-dev/isaacus-python/commit/0644ad39f602b43ee03e4eb4ec58b05cb5ff28aa))


### Chores

* **internal:** bump rye to 0.44.0 ([#31](https://github.com/isaacus-dev/isaacus-python/issues/31)) ([371c249](https://github.com/isaacus-dev/isaacus-python/commit/371c2490695cd773b8202c8cd016360535609923))

## 0.1.3 (2025-03-15)

Full Changelog: [v0.1.2...v0.1.3](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.2...v0.1.3)

### Chores

* update SDK settings ([#26](https://github.com/isaacus-dev/isaacus-python/issues/26)) ([242ae3a](https://github.com/isaacus-dev/isaacus-python/commit/242ae3acecf25b93e5f7ca824926778196c95490))

## 0.1.2 (2025-03-14)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.1...v0.1.2)

### Features

* **api:** added latest OpenAPI specification ([#20](https://github.com/isaacus-dev/isaacus-python/issues/20)) ([a9c1c23](https://github.com/isaacus-dev/isaacus-python/commit/a9c1c2342202dd0fc29fbc350104a8a0a70e8592))


### Chores

* **internal:** codegen related update ([#22](https://github.com/isaacus-dev/isaacus-python/issues/22)) ([6c913e4](https://github.com/isaacus-dev/isaacus-python/commit/6c913e4dd83b070f7796f535e22cbe5b82287115))
* **internal:** remove extra empty newlines ([#23](https://github.com/isaacus-dev/isaacus-python/issues/23)) ([39adf10](https://github.com/isaacus-dev/isaacus-python/commit/39adf10b15bf5e03d6554a37d1b5181a32088624))
* update SDK settings ([#24](https://github.com/isaacus-dev/isaacus-python/issues/24)) ([914555c](https://github.com/isaacus-dev/isaacus-python/commit/914555c31d1317220c574a274c1b2ae9eae6f4dc))

## 0.1.1 (2025-03-08)

Full Changelog: [v0.1.0-alpha.1...v0.1.1](https://github.com/isaacus-dev/isaacus-python/compare/v0.1.0-alpha.1...v0.1.1)

### Features

* **api:** added latest OpenAPI specification ([#16](https://github.com/isaacus-dev/isaacus-python/issues/16)) ([219c568](https://github.com/isaacus-dev/isaacus-python/commit/219c5681bb2ad9219d66fc4d14f6787744ddd221))


### Chores

* update SDK settings ([#18](https://github.com/isaacus-dev/isaacus-python/issues/18)) ([a6f6958](https://github.com/isaacus-dev/isaacus-python/commit/a6f69580dd65ee3d6f1ba4f9cf6406e8cfed0998))

## 0.1.0-alpha.1 (2025-03-04)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/isaacus-dev/isaacus-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* added latest OpenAPI specification ([#1](https://github.com/isaacus-dev/isaacus-python/issues/1)) ([ee4cdd8](https://github.com/isaacus-dev/isaacus-python/commit/ee4cdd8df312a81d4a46da568ff2a37d55127f28))
* added latest OpenAPI specification ([#3](https://github.com/isaacus-dev/isaacus-python/issues/3)) ([e6234c7](https://github.com/isaacus-dev/isaacus-python/commit/e6234c71a201beb74666d0ef7f7077a686f4a690))
* **api:** added latest OpenAPI specification ([#13](https://github.com/isaacus-dev/isaacus-python/issues/13)) ([822a5b5](https://github.com/isaacus-dev/isaacus-python/commit/822a5b561b88de0a7aaca05f786bffaeab16371a))
* **api:** added latest OpenAPI specification ([#4](https://github.com/isaacus-dev/isaacus-python/issues/4)) ([8841b6a](https://github.com/isaacus-dev/isaacus-python/commit/8841b6a28bde24db83c08a864ab3d8aef9007cfa))
* **api:** added latest OpenAPI specification ([#5](https://github.com/isaacus-dev/isaacus-python/issues/5)) ([36f1cd8](https://github.com/isaacus-dev/isaacus-python/commit/36f1cd8f3ebb1abaedbe8b0a4e19c8747011f9f3))
* **api:** added latest OpenAPI specification ([#8](https://github.com/isaacus-dev/isaacus-python/issues/8)) ([0ba3728](https://github.com/isaacus-dev/isaacus-python/commit/0ba3728aa0c7509e344f1c5029ecc54ade403266))
* **api:** update via SDK Studio ([2863c6c](https://github.com/isaacus-dev/isaacus-python/commit/2863c6c6f72258b53649f63cc8cb2e4f480f4818))
* **client:** allow passing `NotGiven` for body ([#6](https://github.com/isaacus-dev/isaacus-python/issues/6)) ([539267b](https://github.com/isaacus-dev/isaacus-python/commit/539267b95ab1a193db15ba46dd2fed6d67b994c9))


### Bug Fixes

* asyncify on non-asyncio runtimes ([268752f](https://github.com/isaacus-dev/isaacus-python/commit/268752f5baa48fff9ebd30ed739cc5765f43dab1))
* **client:** mark some request bodies as optional ([539267b](https://github.com/isaacus-dev/isaacus-python/commit/539267b95ab1a193db15ba46dd2fed6d67b994c9))


### Chores

* **docs:** update client docstring ([#11](https://github.com/isaacus-dev/isaacus-python/issues/11)) ([bb860bc](https://github.com/isaacus-dev/isaacus-python/commit/bb860bc18a916cd707b709bff17e2510973623b5))
* **internal:** fix devcontainers setup ([#7](https://github.com/isaacus-dev/isaacus-python/issues/7)) ([23046c4](https://github.com/isaacus-dev/isaacus-python/commit/23046c49e639ee760e9206e99c3e13baaf5d6b30))
* **internal:** properly set __pydantic_private__ ([#9](https://github.com/isaacus-dev/isaacus-python/issues/9)) ([16c7d5e](https://github.com/isaacus-dev/isaacus-python/commit/16c7d5e011fbb479ff0ba5bc850fc76cabd682cd))
* **internal:** remove unused http client options forwarding ([#12](https://github.com/isaacus-dev/isaacus-python/issues/12)) ([af1ee9e](https://github.com/isaacus-dev/isaacus-python/commit/af1ee9e77d51cbd053d3e48e9adf80f243fb19a5))
* **internal:** update client tests ([ac65c8f](https://github.com/isaacus-dev/isaacus-python/commit/ac65c8f3b45159cd75f14466249e524679c1481d))
* update SDK settings ([#14](https://github.com/isaacus-dev/isaacus-python/issues/14)) ([4d87849](https://github.com/isaacus-dev/isaacus-python/commit/4d878496b4ae774ec92e4bc08f26a708b698685d))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#10](https://github.com/isaacus-dev/isaacus-python/issues/10)) ([7e625b2](https://github.com/isaacus-dev/isaacus-python/commit/7e625b262c4e480379ddbe5bd2ca983f83c90988))
