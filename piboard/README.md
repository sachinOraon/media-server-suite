## Steps to setup PiBoard
It's a dashboard that displays the running docker containers in one place.

 1. Clone this repository and navigate to piboard directory.
    - `git clone https://github.com/sachinOraon/media-server-suite.git`
    - `cd media-server-suite/piboard`

 2. Create virtual environment for installing python modules[`root` permission is required].
    - `sudo -s`
    - `virtualenv envname`
    - `source envname/bin/activate`
    - `pip3 install flask-restx flask-cors docker gunicorn`

 3. (Optional) Change the flask's default port number(5000) by modifying [this line](https://github.com/sachinOraon/media-server-suite/blob/23e75c96653928b2d4488c542ecfed8a48bc8335/piboard/api.py#L82) For example:
    `app.run(debug=True, host='0.0.0.0', port=8080)`

 4. (Optional) Change the port number value as per step 3 by modifying [this line](https://github.com/sachinOraon/media-server-suite/blob/23e75c96653928b2d4488c542ecfed8a48bc8335/piboard/html/index.html#L102)

 5. Add and entry for your running container name in the file `piboard/Container.py` and also add the details for it as mentioned in `piboard/Description.py`

 6. Start the flask server as root and change the path and port number in the given command accordingly:
    - `sudo /home/sachin/media-server-suite/piboard/envname/bin/gunicorn --chdir /home/sachin/media-server-suite/piboard --daemon --workers 1 --bind 0.0.0.0:5000 --user 0 --group 0 --umask 007 api:app`

 7. Set this command in crontab to run after system reboot:
    - `sudo crontab -e`
    - Add this entry and save the file: `@reboot /home/sachin/media-server-suite/piboard/envname/bin/gunicorn --chdir /home/sachin/media-server-suite/piboard --daemon --workers 1 --bind 0.0.0.0:5000 --user 0 --group 0 --umask 007 api:app`

 8. Open new terminal and navigate to `piboard/html` and start the apache server using command:
    - `sudo docker run -d --restart=unless-stopped --name piboard -p 80:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:latest`
