#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 maifengqiang                                                  #
#                                                                              #                                            #
#                                                                              #
#                                                                              #
################################################################################

import textwrap

import setuptools

version = "0.0.1"

if __name__ == "__main__":
    setuptools.setup(
        name="git_get_github_by_user",
        version=version,
        description="Use the full maifengqiang github API v1",
        author="maifengqiang",
        author_email="445044628@qq.com",
        url="http://pygithub.readthedocs.io/en/latest/",
        long_description=textwrap.dedent(
            """\
            (Very short) Tutorial
            =====================
            First create a Github instance::
                from github import Github
                # using username and password
                g = Github("user", "password")
                # or using an access token
                g = Github("access_token")
            Then play with your Github objects::
                for repo in g.get_user().get_repos():
                    print(repo.name)
                    repo.edit(has_wiki=False)
            Reference documentation
            =======================
            See http://pygithub.readthedocs.io/en/latest/"""
        ),
        packages=["github"],
        package_data={},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development",
        ],
        test_suite="tests.AllTests",
        python_requires=">=3.5",
        install_requires=["pygithub", "gitpython"],
        # extras_require={"integrations": ["cryptography"]},
        # tests_require=["cryptography", "httpretty>=0.9.6", "parameterized>=0.7.0"],
    )
