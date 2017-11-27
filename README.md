# gacs-qip
GACS Quality Improvement Project (2017) data and utilities

Backend for https://agrisemantics.github.io/gacs-qip/

#### Build the website using MkDocs

* Install [mkdocs](http://mkdocs.org) on your machine (see [installation instructions](http://www.mkdocs.org/#installation)).
* Run the command `mkdocs gh-deploy` (or use [deploy.sh](https://github.com/agrisemantics/gacs-qip/blob/master/deploy.sh)).  
    * This command creates (or refreshes) the website at [https://agrisemantics.github.io/gacs-qip/](https://agrisemantics.github.io/gacs-qip/).  
    * The command must be run from the root directory of this repo.  
    * Behind the scenes, `mkdocs gh-deploy` builds HTML docs from the Markdown sources, uses the `ghp-import` tool to commit them to the `gh-pages` branch, and pushes the `gh-pages` branch to GitHub.

