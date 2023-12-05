## External Mod Files

This repository contains "link files", which are files with the `.json` extension instead of `.jar` extension.

Link files are a solution to the problem of including jars from developers that did not intend their mods to be used for speedrunning.

Link files are json formatted files containing two values, the link, and the hash.
- The `link` value is a direct download link, usually a modrinth cdn link.
- The `hash` value is a sha512 hash of the file provided by modrinth.

The purpose of the link file is to provide a way for tools, such as modcheck, to find legal versions of mods not directly stored in the repository and still deliver the mods to the users, while also doing so securely by being able to check the sha512 hash of the downloaded file.