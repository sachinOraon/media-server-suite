# media-server-suite
It's a combination of various applications to build a complete media server solution based on the multi-container Docker applications.

### Following applications are included:
- `portainer` : It is an open source tool for managing containerized applications.
- `qBittorrent-nox` :  It aims to provide an open-source software alternative to µTorrent.
- `sonarr` : It is a PVR for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them.
- `radarr` :  It is a movie collection manager for Usenet and BitTorrent users.
- `jellyfin` :  It is the volunteer-built media solution that puts _you_ in control of your media. Stream to any device from your own server, with no strings attached.
- `jackett` :  It works as a proxy server: it translates queries from apps ([Sonarr](https://github.com/Sonarr/Sonarr), [Radarr](https://github.com/Radarr/Radarr), etc.) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software.
- `flaresolverr` :  It is an addon for `jackett`. It is a proxy server to bypass Cloudflare protection.
- `filebrowser` :  It provides a file managing interface within a specified directory.
---
### Steps to setup
1. Install `git`, `docker` and `docker-compose`.
    - Note : `media-server.yml` file has been tested with the `docker-compose` version `1.29.1`
2. Clone this repository.
3. Give `rw` permissions to the `downloads` directory.
4. Execute `docker-compose -f media-server.yml up -d` It'll setup the containers.
5. Once completed, navigate to `localhost:8080` for accessing the home page.
    - You have to manually complete the initial setup for all applications.
6. To remove the containers, execute `docker-compose -f media-server.yml down --volumes --remove-orphans`
---
### Port numbers assigned to each application
If deployed on personal cloud server, then open the following ports. Also make sure they don't conflict with other running services. Well, you can set different port numbers as per your choice in the `media-server.yml` file.
| Apps | Port |
| --- | ----------- |
| homepage | 8080 |
| qBittorrent-nox | 8010 |
| filebrowser | 8020 |
| jackett | 8030 |
| flaresolverr | 8040 |
| sonarr | 8050 |
| radarr | 8060 |
| jellyfin | 8070 |
| portainer | 9000 |