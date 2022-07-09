from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource
from Container import container
from Description import description
import logging
import subprocess
import docker
import json
import requests

app = Flask(__name__)
CORS(app)
api = Api(app)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


@api.route('/services/info')
class DockerContainer(Resource):
    def get(self):
        conmap = {}
        con_port = {}
        response = {}
        try:
            dclient = docker.DockerClient(base_url="unix://var/run/docker.sock")
            conlist = dclient.containers.list(filters={'status': 'running'})
            for cont in conlist:
                conmap[cont.short_id] = cont.name
        except (docker.errors.APIError, docker.errors.DockerException) as err:
            errmsg = f"Failed to get containers list: {str(err)}"
            logging.error(errmsg)
            return {'status': 'ERR', 'msg': errmsg}
        if len(conmap) == 0:
            return {'status': 'ERR', 'msg': 'No service found'}
        for id in conmap:
            try:
                logging.info(f"Getting port details for {conmap[id]} : {id}")
                out = subprocess.run(args=["docker", "inspect", "--format='{{json .NetworkSettings.Ports}}'", id],
                                     check=True, capture_output=True).stdout.decode().replace("\n", "").replace("'", "")
                port_map = json.loads(out)
                for exp in port_map:
                    if port_map[exp] is None:
                        continue
                    for val in port_map[exp]:
                        hostport = int(val["HostPort"])
                        logging.info(f"Checking the port: {hostport}")
                        try:
                            resp = requests.head(url=f"http://127.0.0.1:{hostport}")
                            if resp.status_code == 200 or conmap.get(id) == container.filebrowser:
                                con_port[id] = hostport
                                logging.info(f"Container: {conmap[id]} HostPort: {hostport}")
                            resp.close()
                        except requests.exceptions.ConnectionError:
                            pass
            except subprocess.CalledProcessError:
                logging.error(f"Failed to execute inspect command for: {conmap[id]}")
            except json.JSONDecodeError as err:
                logging.error(f"Failed to parse command output for: {conmap[id]}: {str(err)}")
            except FileNotFoundError:
                return {'status': 'ERR', 'msg': 'Unable to find and execute docker command'}
        if len(con_port) > 0:
            service_list = []
            for id in con_port:
                try:
                    port = con_port.get(id)
                    name = conmap.get(id)
                    desc = description.map.get(name)['desc']
                    icon = description.map.get(name)['icon']
                    color = description.map.get(name)['color']
                except (KeyError, TypeError):
                    logging.error(f"Unable to get details for: {id}")
                    continue
                else:
                    service_list.append({"name": name, "port": port, "desc": desc, "icon": icon, "color": color})
            response["services"] = service_list
            response["status"] = "SUCCESS"
        else:
            response["status"] = "ERR"
            response["msg"] = "Unable to find any eligible service"
        return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
