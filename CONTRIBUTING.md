# Contributing Guide

Thank you for contributing to the **Trainee Journey - Python** repository.

Please follow the workflow below for every practical assignment.

## Contribution Workflow

1. Pull the latest changes from `main`.
2. Create a new feature branch.
3. Complete the assigned practical.
4. Commit your changes.
5. Push your branch to GitHub.
6. Open a Pull Request.
7. Address review comments, if any.
8. Merge the Pull Request after approval.

## Step 1: Update Your Local Repository

```bash
git checkout main
git pull origin main
```

## Step 2: Create a Feature Branch

Use the following naming convention:

```text
week-NN-topic-slug
```

Example:

```bash
git checkout -b week-02-control-flow
```

## Step 3: Complete the Practical

* Work only on your assigned task.
* Follow PEP 8 coding standards.
* Test your code before committing.

## Step 4: Commit Your Changes

```bash
git add .
git commit -m "Add Week 02 control flow practical"
```

Use descriptive commit messages.

## Step 5: Push Your Branch

```bash
git push origin week-02-control-flow
```

## Step 6: Create a Pull Request

Create a Pull Request from your feature branch into `main`.

Include:

* Week number
* Topic
* Summary of changes
* Testing performed
* Additional notes (if applicable)

## Pull Request Review

Before requesting a review, ensure that:

* Your code builds and runs successfully.
* There are no merge conflicts.
* Only relevant files are included.
* Documentation has been updated if necessary.

## Branch Protection

The `main` branch is protected.

* Direct pushes to `main` are not allowed.
* All changes must be submitted through a Pull Request.
* A Pull Request must be reviewed before merging.

## Coding Guidelines

* Follow PEP 8.
* Keep functions small and reusable.
* Use descriptive names.
* Remove unused imports and files.
* Keep commits focused on a single task.

Thank you for helping maintain a clean, organized, and collaborative repository.
