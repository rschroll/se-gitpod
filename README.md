[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/rschroll/se-gitpod) 

# Standard Ebooks + Gitpod

This repo is testing developing [Standard Ebooks](https://standardebooks.org) on [Gitpod](https://gitpod.io).  It provides a Gitpod workspace with the [Standard Ebooks tools](https://github.com/standardebooks/tools) installed.  To test this out, the [step-by-step instructions](https://standardebooks.org/contribute/producing-an-ebook-step-by-step) for creating an ebook for *Dr. Jekyll and Mr. Hyde* have been followed.  The focus has been on testing the Standard Ebooks tools, so proofreading and manual markup have not been done.  The resulting product does not live up to the standards of Standard Ebooks.

All of the steps described in the instructions work, with the following exceptions:

- The `se create-draft` command will create a sub-repo.  The resultant files were moved to and added to the top-level repo.
- Cropping and resizing bitmap images for the cover cannot be done within the Gitpod workspace.  However, tools like [Pixlr](https://pixlr.com/x) allow web-based image editing, and the resultant files can be uploaded to the workspace.  (Use `File > Upload Files...`, or just drag-and-drop to the file pane.)
- The `se build` tool is only able to produce EPUB and EPUB3 files.  This is because Calibre is not installed in the workspace.
- The `se build --check` command wrongly claims that `epubcheck` has failed when it actually succeeded.  It appears that this command looks at the output of `epubcheck` instead of its return code, and gets confused by a message about Java options.
- The `.gitignore` file includes the `dist/` directory, allowing `se build` to output within the repo, for convenience on Gitpod.
- `se lint` will complain about the `dist/` folder and the `README.md` file.

## What is Standard Ebooks?

[Standard Ebooks](https://standardebooks.org) is a project to create high-quality ebooks of notable public-domain texts.  The project has built a number of tools to help in the process of creating these ebooks, but the [installation process](https://github.com/standardebooks/tools#installation) is non-trivial.

## What is Gitpod?

[Gitpod](https://gitpod.io) allows you to spin up a cloud-based development environment from any Github (or Gitlab) repo.  This repo includes settings that install the Standard Ebooks tools, to allow a user to build ebooks without installing the tools locally.  To try it out, click the badge at the top of this file.  Gitpod gives all user 50 hours usage free each month.

## Can I use this to produce my own books?

Yes, but not terribly easily yet.  The next step would be to build a skeleton repo with the Gitpod settings.  This could be cloned as a base for producing new books.  Several changes to the tools will be needed to make this a smooth operation.
