const shell = require("./../../.init/lib-shell");

module.exports = class MenController {

    memInfo(request, response, next) {
        return response.status(200).json({
            MemTotal: shell.exec(`cat /proc/meminfo |grep MemTotal | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            MemFree: shell.exec(`cat /proc/meminfo |grep MemFree | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            MemAvailable: shell.exec(`cat /proc/meminfo |grep MemAvailable | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            Buffers: shell.exec(`cat /proc/meminfo |grep Buffers | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            Cached: shell.exec(`cat /proc/meminfo |grep Cached: | head -1 | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            SwapCached: shell.exec(`cat /proc/meminfo |grep SwapCached | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            Active: shell.exec(`cat /proc/meminfo |grep Active: | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            Inactive: shell.exec(`cat /proc/meminfo |grep "Inactive(anon)" | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            SwapTotal: shell.exec(`cat /proc/meminfo |grep SwapTotal | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
            SwapFree: shell.exec(`cat /proc/meminfo |grep SwapFree | cut -d':' -f2 | sed -e "s/ //g" |sed "s/kB//g"`),
        });
    }
}