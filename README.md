# Leah’s birthday card ♡

This repository is set up to publish Zac’s finished birthday card through GitHub Pages **without changing the card design**.

## Publish

1. Download the file **Leah-Interactive-Birthday-Card.zip** from the ChatGPT conversation. Do not unzip it.
2. Open [Upload files](https://github.com/posnerzac-debug/Leah-Birthday-Card/upload/main) and drag in the ZIP. Keep the filename exactly `Leah-Interactive-Birthday-Card.zip`. Select **Commit changes**.
3. In [Settings → Pages](https://github.com/posnerzac-debug/Leah-Birthday-Card/settings/pages), select **GitHub Actions** as the Build and deployment source if it is not already selected.
4. Check the [Publish Leah's birthday card workflow](https://github.com/posnerzac-debug/Leah-Birthday-Card/actions/workflows/deploy-pages.yml). Once it succeeds, the public site should be at `https://posnerzac-debug.github.io/Leah-Birthday-Card/`.

The workflow extracts the ZIP and serves the exact `index.html` and image assets bundled inside it. The card contains personal photos and a letter; everything in this public repository and on GitHub Pages is publicly accessible.
