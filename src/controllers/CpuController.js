const shell = require("../../.init/lib-shell");
const messages = require("../helper/messages");

module.exports = class CpuController {

    loadCpuInfo(request, response) {
        return response.status(200).json({
            modelName: shell.exec(`cat /proc/cpuinfo |grep 'model name' | cut -d ':' -f 2 | sed 's/^ //g'`),
            cpuMHz: shell.exec(`cat /proc/cpuinfo |grep 'cpu MHz' | cut -d ':' -f 2 | sed 's/^ //g'`),
            cacheSize: shell.exec(`cat /proc/cpuinfo |grep 'cache size' | cut -d ':' -f 2 | sed 's/^ //g' | sed 's/KB//g'`)            
        });
    }

    cpuUsed() {
        console.log('teste');
    }
}

/// echo senha |sudo -S cat /etc/shadow - Sem precisar digitar a senha...