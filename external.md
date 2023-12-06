## External Mod Files

This repository contains "link files", which are files with the `.json` extension instead of `.jar` extension.

Link files are a solution to the problem of including jars from developers that did not intend their mods to be used for speedrunning.

Link files are json formatted files containing two values, the link, and the hash.
- The `link` value is a direct download link, usually a modrinth cdn link.
- The `hash` value is a sha512 hash of the file provided by modrinth.

The purpose of the link file is to provide a way for tools, such as modcheck, to find legal versions of mods not directly stored in the repository and still deliver the mods to the users, while also doing so securely by being able to check the sha512 hash of the downloaded file.


Example (LazyDFU):
```json
{
  "link": "https://cdn.modrinth.com/data/hvFnDODi/versions/0.1.2/lazydfu-0.1.2.jar",
  "hash": "20b1cd3e62051c7d7498ecdc49912acb918fc4748d469c67c078cc97197289760e64b9339a4d4a03d175f648c8be8601d131776a9a6bdb8832cecdda6fc46498"
}
```

A python script is included in this repository (MCSRExternalModCompiler.py) to help generate these link files. Usage still involves manual intervention since it will generate link files for versions that are already covered by internal mods, and modrinth may not report the correct version range.