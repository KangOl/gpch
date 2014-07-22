# GPCH - Git Pre-Commit Hook

gpch is a git pre-commit hook that will check your current diff against the following

 - search for trealing spaces
 - search for remaining conflits marks
 - search for leftover debugging instructions
 - validate your code through flake8 (if installed)

gpch is mainly used to validate python and js code.
 
## Install
Simply link the `pre-commit` file into the `.git/hooks` directory of **your** git repository.

## Colored output
If gpch find [colout](https://github.com/nojhan/colout), it will be used to color the ouput of flake8.

## TODO
 - validate the correctness of newly commited js code (via a stripped output of jshint)
 - validate sass/scss/less files
 - validate xml files (via xmllint?)