const shell = require("../../.init/lib-shell");
const messages = require("../helper/messages");

module.exports = class SinglePorts {

    singlePortScan(request, response) {
        if (shell.exec(`python3 ${__dirname}/../libs/testport.py --type single_port`).stderr) {
            return response.status(200).json({status: false});
        } else {
            return response.status(200).json({status: true});
        }                    
    }

    checkHistoryPorts(request, response) {
        if (shell.exec(`python3 ${__dirname}/../libs/testport.py --type check_history_ports`).stderr) {
            return response.status(200).json({status: false});
        } else {
            return response.status(200).json({status: true});
        }
    }

    checkHistoryPortsAdvanced(request, response) {
        if (shell.exec(`python3 ${__dirname}/../libs/testport.py --type complex_ports`).stderr) {
            return response.status(200).json({status: false})
        } else {
            return response.status(200).json({status: true});
        }
    }
}