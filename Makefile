PREFIX = /usr/local

.PHONY: install
install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp influx-bmp085.py $(DESTDIR)$(PREFIX)/bin/influx-bmp085.py
	cp influx-bmp085.service /etc/systemd/system/influx-bmp085.service
	systemctl daemon-reload
	systemctl restart influx-bmp085
