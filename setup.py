#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = "Bottle plugin acl, api access control"
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='bottle-aclPlugin',  # 上传的包名
    version="0.1.0",  # 上传的版本
    packages=find_packages(),  # 导入目录下所有__init__.py包
    install_requires=REQUIREMENTS,  # 需要引入的第三方库
    description=description,  # 一段描述的话
    author="Xu_beixiong",
    author_email='17610739793@163.com',
    license='MIT',
    url='https://github.com/bottlepy/bottle-beaker',
    py_modules=['bottle-aclPlugin'],
    requires=['bottle (>=0.9)'],
    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
