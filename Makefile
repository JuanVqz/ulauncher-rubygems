EXT_NAME:=com.github.juanvqz.ulauncher-rubygems
EXT_DIR:=$(shell pwd)

link:
	ln -s ${EXT_DIR} ~/.local/share/ulauncher/extensions/${EXT_NAME}

dev:
	ulauncher --dev -v | grep "ulauncher-rubygems"

.PHONY:link dev
