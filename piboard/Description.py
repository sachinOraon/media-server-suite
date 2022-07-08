from Container import container

class Description:
    def __init__(self):
        self.map = {
            container.h5ai: {
                'desc': 'h5ai is a modern file indexer for HTTP web servers with focus on your files. Directories are displayed in a appealing way and browsing them is enhanced by different views, a breadcrumb and a tree overview.',
                'color': 'icon-box-green',
                'icon': 'bx-folder-open'
            },
            container.qbit: {
                "desc": 'The qBittorrent project aims to provide an open-source software alternative to uTorrent. It is based on the Qt toolkit and libtorrent-rasterbar library.',
                "color": "icon-box-yellow",
                "icon": "bx-cloud-download"
            },
            container.portainer: {
                "desc": 'Portainer is a universal container management tool. It works with Kubernetes, Docker, Docker Swarm and Azure ACI and allows you to manage containers without needing to know platform-specific code.',
                "color": "icon-box-cyan",
                "icon": "bx-package"
            },
            container.filebrowser: {
                "desc": 'File Browser provides a file managing interface within a specified directory and it can be used to upload, delete, preview, rename and edit your files.',
                "color": "icon-box-blue",
                "icon": "bx-file"
            }
        }

description = Description()
