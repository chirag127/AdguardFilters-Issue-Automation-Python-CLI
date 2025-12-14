# Contributing to AdguardFilters-Issue-Automation-Python-CLI

First off, thank you for considering contributing. It's people like you that make this project such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, [make one](https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI/issues/new)! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

### Fork & create a branch

If this is something you think you can fix, then [fork the repo](https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI/fork) and create a branch with a descriptive name.

A good branch name would be (where issue #33 is the ticket you're working on):

```bash
git checkout -b 33-add-new-feature
```

### Get the test suite running

Make sure you're running the tests before you make any changes, to ensure that everything is working correctly.

### Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first :smile_cat:

### Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with the latest upstream changes.

```bash
git remote add upstream git@github.com:chirag127/AdguardFilters-Issue-Automation-Python-CLI.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```bash
git checkout 33-add-new-feature
git rebase master
git push --force-with-lease origin 33-add-new-feature
```

Finally, go to GitHub and [make a Pull Request](https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI/compare)

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing and merging, check out this guide on [merging vs. rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing).

## Merging a PR (for maintainers)

A PR can only be merged by a maintainer if:

- It is passing CI.
- It has been approved by at least one maintainer.
- It has no requested changes.
- It is up to date with the `master` branch.

Any maintainer who merges a PR is responsible for fixing any bugs that it introduces.
