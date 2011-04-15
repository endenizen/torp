# Makefile
# Copyright 2008, Sean B. Palmer, inamidst.com
# Licensed under the Eiffel Forum License 2.

# archive - Create torp.tar.bz2 using git archive
archive: ;
	# hg archive -t tbz2 torp-hg.tar.bz2
	git archive --format=tar --prefix=torp/ HEAD | bzip2 > torp.tar.bz2

# ci - Check the code into git and push to github
ci: ;
	# hg ci
	git commit -a && git push origin master

# log - Show a log of recent updates
log: ;
	# git log --date=short --format='%h %ad %s'
	git graph

# sync - Push torp to pubble:opt/torp/
sync: ;
	rsync -avz ./ pubble:opt/torp/

help: ;
	@egrep '^# [a-z]+ - ' Makefile | sed 's/# //'
