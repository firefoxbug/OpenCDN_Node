clean:
	@rm -f *.rpm
rpm:
	rpmbuild -bb opencdn-node.spec

.PHONY:rpm
