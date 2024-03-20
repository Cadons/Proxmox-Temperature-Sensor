# Proxmox cooling automation system
![Proxmox](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.3nxRhxpUGnXvzRngQLRuMwHaHa%26pid%3DApi&f=1&ipt=da43677035b8b8c1e36c5b9402d5fe2ceeb1d9da0755fa32db3a9674ec462431&ipo=images)

This project offers a temperature sensor solution tailored for Proxmox servers, which actively monitors the server's temperature and dispatches notifications upon reaching critical levels.

In the setup, a firewall PC with passive dissipation running Proxmox is aimed to be cooled using a laptop desktop fan, lacking speed control features. To overcome this, a smart USB socket has been added, set to trigger via Alexa routines when the temperature surpasses a predetermined limit.

The sensor boasts various configurations: it can solely log temperature data while delegating alerts to external tools like Grafana, activate the cooling system autonomously, or combine both functionalities.

Originally, the plan involved the sensor sending data to a Flask server responsible for managing the fan. However, after further analysis, it was decided to consolidate this functionality within the sensor itself. This approach facilitated a more thorough analysis of needs and requirements, resulting in viable solutions without over-engineering.

## Features

- Server temperature monitoring
- Sending notifications when temperature reaches a critical level
- Stopping cooling when the temperature falls below the critical level
- Sending data to influxdb for tracking
- Use of webhook when the temperature is above or below the tolerance threshold
## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/yourusername/Proxmox-Temperature-Sensor.git
    ```

2. Install dependences:
    ```shell
    pip install -r requirements.txt
    ```

3. Edit the configuration file `config.json` with your data
4. Install the service
```shell
./install.sh