#!/usr/bin/python2.7
# encoding:utf-8
# pip install GitPython

import os
import git
#repo.is_dirty()


path='C:/cg-Package'

# clone
#new_repo = git.Repo.clone_from(url='git@git.ccc.net:coco-code/package.git', to_path='../new')

# init
#repo = git.Repo.init(path='./new')
#repo = git.Repo.init(path='C:/Users/wangxu/Documents/GitHub/alpine-docker')
#print(u"已连接到库")

# pull
#print(u"正在拉取更新中...")
#remote = repo.remote()
#remote.pull() # remote.push()
#print(u"更新完毕.")

# for archive.tar
#with open('archive.tar', 'wb') as fp:
#    repo.archive(fp)

if os.path.exists(path):
    repo = git.Repo.init(path)
    print(u"正在拉取更新中...")
    remote = repo.remote()
    remote.pull() # pull or push:remote.push()
    print(u"更新完毕.")
else:
    repo = git.Repo.clone_from(url='git@git.ccc.net:coco-code/package.git', to_path=path)
    print(u"正在获取更新中...")
    remote = repo.remote()
    remote.pull()
    print(u"更新完毕.")
