# For Runners

Runners are not intended to be on GitHub to get mods. If you cannot find a mod on <https://mods.tildejustin.dev/>, it isn't legal. If a newer mod became legal, the best way to get it would be from <https://mods.tildejustin.dev/> or [ModCheck](https://github.com/tildejustin/modcheck/releases).

<https://github.com/Minecraft-Java-Edition-Speedrunning/legal-mods> is the true source of legal mods, and <https://mods.tildejustin.dev/> will always reflect that. Any other GitHub page that is called `legal-mods` is what's called a "fork", a "fork" is just a copy of the original `legal-mods` made by another developer so that they can make and then request changes to the original `legal-mods`. If the URL of the page you are looking at is not <https://github.com/Minecraft-Java-Edition-Speedrunning/legal-mods>, then you are not looking at the official `legal-mods` repository page. Additionally, URLs that start with <https://github.com/Minecraft-Java-Edition-Speedrunning/legal-mods> still might not reference mods that are legal, and may reference external commits from pull requests or branches other than `main`, and mods found through these URLs would not yet be legal, or might never be legal. Runners are not expected to be able to understand and navigate these GitHub features, so the easiest way to tell if a mod is legal is if it appears on <https://mods.tildejustin.dev/>.

# MCSR Legal Mods

This repository acts as a central authority for legal mods for the Minecraft Java Edition Speedrunning community. This means runs can be done using the mods found in this repository and be submitted and verified on https://speedrun.com/mc & https://speedrun.com/mcce.

## What mods are legal for what Minecraft versions?

Each mod has its own directory, and in that directory are more directories named after the legal Minecraft version ranges. For example, Sodium for 1.16.5 can be found in `legal-mods/sodium/1.16.2-1.16.5/`.

Possible directory formats:

- `1.x.x` - The mod is legal and works for this specific version.
- `1.x.x-1.x.x` - The mod is legal and works for all versions in this range (inclusive).
- `1.x.x+` - The mod is legal and works for this specific version and is legal for all Minecraft versions released after the specified version given that it functions correctly.

Sometimes there will be missing Minecraft versions for a mod. If you really need a mod for a specific Minecraft version that isn't available in this repository, please read the following:

> If there is no listed jar for a specific MC subversion, a jar from within the same major MC version can be used if it functions correctly.
> For example, if Lithium for MC 1.15.2 works for MC 1.15.1, it may be used for MC 1.15.1, but Lithium for MC 1.16.5 may not be used for MC 1.17 since it falls under a different major version (1.16 vs 1.17).

## Conditional Mods

Certain mods are only allowed under certain conditions.

Set seed categories only:

- `setspawnmod`
- `chunkcacher`

For developers, these conditions can be found in the `conditional-mods.json` file found in the root of this repository.

## Internal Mod Files

Most mods included in this repository are mods made by the community, these mods are included in this repository as .jar files. For example: `legal-mods/sodium/1.16.2-1.16.5/sodium-1.16.5-v1.jar`.

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
