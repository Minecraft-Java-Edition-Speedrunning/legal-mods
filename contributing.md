# Contributing

Generally, requests for mod legalization are expected to be initiated via a #help thread in the [official Discord](https://discord.com/invite/jmdFn3C).

All mods and mod updates require legalization before they are allowed for use. Legalization is effectuated by a PR merge into this repository. To merge, a PR requires Leaderboard Mod approval and Technical Advisor approval. Leaderboard Mods decide on whether on not to allow the concept of a mod or update and Technical Advisors review the code of the mod or update to ensure it does not have any unwanted effects and minimally affects the game.

Typically mod updates are been done by Tech Advisors because the process requires a lot of communication with the Mod Team and anyone sufficiently invested in the process we typically onboard, but anyone is welcome to propose updates or new mods. However, be aware that all proposed mods and updates are highly scrutinized for purpose and method, and using a mod for something will only be accepted if every other avenue is deemed insufficient.

## What mods are legal

Mod legalization is considered on a case-by-case basis, however there are general principles allowed mods are expected to adhere to. These include:
- Not unnecessarily affecting the visuals of the run ("visual parity", keeping the game looking and feeling vanilla)
- Not affecting the mechanics of the run (new resetting tech)
- Decreasing, rather than increasing, the hardware gap
- Maintaining consistency with the rules (no autoresetters)

Allowed mods can generally be put into the following categories:
- Performance / optimization / crash fixes
  - Performance mods that increase the performance of the game but do not change any significant aspect of it are generally allowed. This includes Sodium, Lithium, Krypton, LazyDFU, BiomeThreadLocalFix, Starlight, etc. We also generally allow fixes for crashes and freezes that are impossible or impractical to avoid, such as ghost nether.
- Reset / macro replacement
  - Mods that aid in resetting are allowed outside the gameplay segment, in order to decrease the hardware gap and make the game more fun. Many of the most popular mods fall under this category, such as Atum, StandardSettings, SeedQueue, WorldPreview, FastReset, SetSpawn, etc. Compared to performance mods, these mods are not allowed to be interacted with during the run itself as they are considered to alter the game in some significant way.
- Verification
    - Some mods provide positive benefit for verification, such as anticheat capabilities. SpeedRunIGT is the most significant mod of this group.
- Hardware parity
    - Attitudes towards hardware parity have changed over time, but historically standardizing behaviors across hardware were allowed, such as MC-4647 fix, planar fog, and gamma 5. Macro replacement mods are sometimes also considered hardware parity as resetting techniques that are possible with external programs on Windows or Linux might not be possible on macOS, for example.
- Accessibility
  - Accessibility mods modify a non-trivial aspect of the game for accessibility reasons. These need a very compelling reason for legalization and the benefit they serve must be weighed against how they can change the run. Currently, the only allowed accessibility mod is Extra Options, which backports the FOV and Distortion Effects sliders.

For some background on the classification system, see [this discord message](https://discord.com/channels/83066801105145856/416677682290491403/939517613107720232).

Generally quality of life changes are not allowed, however there have been exceptions to this for when not in a run.

The standards for mods have increased significantly since the days of OptiFine. It is not necessarily a good assumption that because you want is like something that is allowed, that new thing will be allowed. We commonly apply tighter scrutiny to new changes over old ones because of what past decisions have taught us.

## Development process

A primary goal of the organization infrastructure is to archive the source code for mods that are legal. This is done in two ways.
1) Development is done in personal repositories. At the time of legalization, a copy of the source code for that build is pushed to an archive repository.
2) Development is done on an organization repository.

"Org repos" as they are known are mostly for long-established internal projects that have been worked on by multiple people and are relatively inactive or get contributions from many people. Notable org repos are sodium and set-spawn. It is entirely up to the developer whether they would like to do development on an org repo, and we can create them on request.

Generally we work via a maintainer model, where most updates are advocated for by the same individual who assumes responsibility for the mod, so if you have a patch we ask that you try to coordinate with whoever manages the repository that is being most actively maintained instead of trying to get something legalized standalone. If you do not know how to find the person / repository, feel free to open a #help ticket and a Tech Advisor is likely to be able to get you in contact or at least know the situation best.

If original author is not active or not interested in hosting your change then you can choose to use an org repo or personal repo. Mods can even be split between an org repo and personal repo depending on if someone wants to re-adopt an org repo or only work on ports for some set of versions or similar.

As a final reminder, contact with the staff team is encouraged early and often. We don't want someone to work hard on a mod or update that has no chance of being legalized, or have to request significant changes. Do not be afraid to come to us with just an intention, we are more than happy to work with you.

## Legalization process

Final legalization, after prs are approved by Tech Advisors and the concept and implementation is signed off on, is often done in waves for convenience's sake. When it's time for a mod wave, a couple of things have to happen.

1) Draft and get final approval for a mini-changelog - anyone, typically a Tech Advisor + multiple Leaderboard Mods
2) Merge associated PRs - staff, typically a Tech Advisor
3) Update legal-builds - staff, typically a Tech Advisor
4) Update metadata - tildejustin or Duncan
5) Distribute changelogs in the official Discord and https://speedrun.com/mc - Leaderboard Mod

Additionally, at some point a staff member must update releases on org repos and archives for non org repos, however this can be done asynchronously and doesn't have a strict timeline. Legality is established after step 3 but in the interest of fairness the other steps must happen reasonably quickly after to avoid an information asymmetry in the community, which is perceived as unfair.
