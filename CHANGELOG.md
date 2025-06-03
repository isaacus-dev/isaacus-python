# Changelog

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
