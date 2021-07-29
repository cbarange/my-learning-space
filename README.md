# my-learning-space

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

## Installation

```console
yarn install
```

## Local Development

```console
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```console
yarn build
npx http-server ./build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

```console
GIT_USER=<Your GitHub username> USE_SSH=true yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.



  yarn start
    Starts the development server.

  yarn build
    Bundles your website into static files for production.

  yarn serve
    Serve the built website locally.

  yarn deploy
    Publish the website to GitHub pages.


```bash
# Remove node, if your version is 12-
sudo apt-get purge --auto-remove nodejs
sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* /usr/local/lib/dtrace/node.d ~/.npm ~/.node-gyp /opt/local/bin/node /opt/local/include/node /opt/local/lib/node_modules
sudo rm -rf /usr/local/lib/node*
sudo rm -rf /usr/local/include/node*
sudo rm -rf /usr/local/bin/node*
sudo rm -rf /etc/apt/sources.list.d/nodesource.list*
sudo apt-get update

# Install node
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
nvm -v # You may restart terminal, check node installation with nvm ls
nvm install node
nvm ls # Check for node installation
node --version # Should be 12+
npm --version

# Install Docusaurus
npx @docusaurus/init@latest init my-learning-space classic

# Look for local search bar :
# https://github.com/easyops-cn/docusaurus-search-local
# https://github.com/lelouch77/docusaurus-lunr-search


yarn add @cmfcmf/docusaurus-search-local

yarn add @easyops-cn/docusaurus-search-local

yarn add docusaurus-lunr-search
yarn run swizzle docusaurus-lunr-search SearchBar -- --danger # reset : yarn run swizzle @docusaurus/theme-classic SearchBar
```
